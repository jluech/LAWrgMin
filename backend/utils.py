import itertools
import json
import os

files_dir = ""
frontend_host = "http://localhost:3000"


def __retrieve_frontend_host():
    return frontend_host


# --- Currently in charge of handling the file ids for uploaded files of different tagging runs ---
class FileHandler:
    new_id = itertools.count().__next__

    def __init__(self, file_id=None):
        if file_id is None:
            self.file_id = FileHandler.new_id()
        else:
            self.file_id = file_id


# --- File and path handling commands ---
def get_uploaded_files_path(file_id):
    return os.path.join(files_dir, str(file_id))


def get_uploaded_files_dict(file_id):
    files_dict = {}
    directory = get_uploaded_files_path(file_id)
    files = os.listdir(directory)
    for filename in files:
        name = filename.split(".")[0]
        json_dict = json.load(os.path.join(directory, filename))
        json_dict["_filename"] = filename
        files_dict[name] = json_dict
    return files_dict


def get_filename_from_path(file_path):
    if file_path.__contains__("\\"):
        filename = file_path.split("\\")[-1].split(".")[0]
    else:
        filename = file_path.split("/")[-1].split(".")[0]
    return filename


def create_tagging_subdir(file_id):
    os.makedirs(os.path.join(files_dir, str(file_id)))


def remove_dir_tree(dir_path):
    if os.path.exists(dir_path):
        dir_contents = os.listdir(dir_path)
        if os.path.isdir(dir_path) and len(dir_contents) > 0:
            for entity in dir_contents:
                entity_path = "/".join([dir_path, entity])
                if os.path.isdir(entity_path):
                    remove_dir_tree(entity_path)
                    os.rmdir(entity_path)
                else:
                    os.remove(entity_path)


def __set_files_dir(path):
    global files_dir
    files_dir = os.path.join(path, 'files')
    os.makedirs(files_dir, exist_ok=True)
