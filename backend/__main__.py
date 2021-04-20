import logging
import os

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

import utils

logging.basicConfig(level=logging.INFO)


# App initialization.
backend = Flask(__name__)

# Create a directory in a known location to save uploaded files to.
utils.__set_files_dir(backend.instance_path)


@backend.route("/", methods=["GET"])
@backend.route("/status", methods=["GET"])
def status():
    logging.info("{__method} status - OK".format(__method=request.method))
    return "OK"


# @backend.route("/tagWithText", methods=["POST"])
@backend.route("/tagWithText", methods=["GET"])
def tag_with_text():
    logging.info("{__method} tagWithText".format(__method=request.method))

    # Saves all the files that were uploaded with the request.
    file_keys = [*request.files]
    file_handler = get_file_handler()
    file_id = file_handler.file_id
    files_dir = utils.get_uploaded_files_path(file_id)
    file_names = []
    for file_key in file_keys:
        file = request.files[file_key]
        file_name = secure_filename(file.filename)
        file_names.append(file_name)
        file.save(os.path.join(files_dir, file_name))

    # Prepares return in json format.
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
