import logging
import os

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

# Create a directory in a known location to save uploaded files to.
utils.__set_files_dir(backend.instance_path)


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


# @backend.route("/tagWithFile", methods=["POST"])
@backend.route("/tagWithFile", methods=["GET"])
def tag_with_file():
    logging.info("{__method} tagWithFile".format(__method=request.method))
    return "Hi file"


@backend.route("/exportToCsv/<int:file_id>", methods=["GET"])
def export_to_csv(file_id):
    logging.info("{__method} exportToCsv {__id}".format(__method=request.method, __id=file_id))
    return "Hi " + str(file_id)


def get_file_handler(file_id=None):
    return utils.FileHandler(file_id)


if __name__ == "__main__":
    backend.run(host="0.0.0.0")
