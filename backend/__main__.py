import logging
import os
import sys

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

import utils

logging.basicConfig(level=logging.INFO)


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

    request_data = request.get_json()
    text = request_data["text"]

    # Retrieve file data and prepare storage folder.
    file_handler = get_file_handler()
    file_id = file_handler.file_id
    files_dir = utils.get_uploaded_files_path(file_id)

    if not os.path.exists(files_dir):
        utils.create_tagging_subdir(file_id)
    os.chdir(files_dir)

    file_name = secure_filename("tagging_req_{__id}.txt".format(__id=file_id))
    if os.path.exists(file_name):
        os.remove(file_name)

    # Write provided text to .txt file for further processing
    with open(file_name, "x") as file:
        file.write(text)

    # Prepare return in json format.
    return jsonify({
        "id": file_handler.file_id,
        "status": "created"
    })


# @backend.route("/api/tagWithFile", methods=["POST"])
@backend.route("/api/tagWithFile", methods=["GET"])
def tag_with_file():
    logging.info("{__method} tagWithFile".format(__method=request.method))

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
        cleanup_instance_files()

    # Create a directory in a known location to save uploaded files to.
    utils.__set_files_dir(backend.instance_path)

    backend.run(host="0.0.0.0")
