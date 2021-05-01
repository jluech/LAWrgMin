import logging
import os
import sys

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

import examples
from targer_output_processing import process_targer_output_data
import utils

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_root.log")


# App initialization.
frontend_host = utils.__retrieve_frontend_host()
backend = Flask(__name__)
cors = CORS(backend, resources={
    r"/status": {"origins": frontend_host},
    r"/api/*": {"origins": frontend_host}
})


@backend.route("/status", methods=["GET"])
def status():
    logging.info("{__method} status - OK".format(__method=request.method))
    return "OK"


@backend.route("/api/tagWithText", methods=["POST"])
def tag_with_text():
    logging.info("{__method} tagWithText".format(__method=request.method))

    # Retrieve file data and prepare storage folder.
    file_handler = get_file_handler()
    file_id = file_handler.file_id
    files_dir = utils.get_uploaded_files_path(file_id)
    logging.info("starting tagWithText for request %d", file_id)

    orig_wd = os.getcwd()
    if not os.path.exists(files_dir):
        utils.create_tagging_subdir(file_id)

    os.chdir(files_dir)
    file_name = secure_filename("tagging_req_{__id}.txt".format(__id=file_id))
    if os.path.exists(file_name):
        os.remove(file_name)

    # Write provided text to .txt file for further processing
    request_data = request.get_json()
    text = request_data["text"]

    with open(file_name, "x") as file:
        file.write(text)

    # Call targer for labelling the new .txt file
    os.chdir("/".join([orig_wd, "targer_instance"]))
    os.system("python labelling.py -i {__in_dir} -o {__out_dir}".format(__in_dir=files_dir, __out_dir=files_dir))
    os.chdir(orig_wd)

    # Read results from targer .out file
    labelled_results = process_targer_output_data(file_id, files_dir)
    if labelled_results.__len__() > 1:
        raise RuntimeError("Tagging multiple out files in request folder %d", file_id)
    # keys: "doc_id", "blocks", "claims", "premises"
    # TODO: currently "text" instead of "blocks"

    print(labelled_results[0].keys())

    # Prepare return in json format.
    return jsonify({
        "id": file_handler.file_id,
        "blocks": examples.example_blocks,
        "claims": examples.example_claims,
        "premises": examples.example_premises,
        "status": "created"
    })


@backend.route("/api/tagWithFile", methods=["POST"])
def tag_with_file():
    logging.info("{__method} tagWithFile".format(__method=request.method))

    request_data = request.get_json()
    print(request_data)

    # Saves all the files that were uploaded with the request.
    file_handler = get_file_handler()
    file_id = file_handler.file_id
    files_dir = utils.get_uploaded_files_path(file_id)

    file_keys = [*request.files]
    file_names = []
    for file_key in file_keys:
        file = request.files[file_key]
        file_name = secure_filename(file.filename)
        file_names.append(file_name)
        file.save(os.path.join(files_dir, file_name))

    # Prepare return in json format.
    return jsonify({
        "id": file_handler.file_id,
        "blocks": examples.example_blocks,
        "claims": examples.example_claims,
        "premises": examples.example_premises,
        "status": "created"
    })


@backend.route("/api/exportToCsv/<int:file_id>", methods=["GET"])
def export_to_csv(file_id):
    logging.info("{__method} exportToCsv {__id}".format(__method=request.method, __id=file_id))
    return "Hi " + str(file_id)


def get_file_handler(file_id=None):
    return utils.FileHandler(file_id)


def cleanup_instance_files():
    files_path = os.path.join(backend.instance_path, 'files')
    utils.remove_dir_tree(files_path)


if __name__ == "__main__":
    args = sys.argv[1:]  # ignore first arg as it's the script
    if args.__len__() > 0 and args.__contains__("--cleanup-files"):
        logging.info("Cleaning up files from previous runs")
        cleanup_instance_files()

    # Create a directory in a known location to save uploaded files to.
    utils.__set_files_dir(backend.instance_path)

    backend.run(host="0.0.0.0")
