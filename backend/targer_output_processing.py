import json
import logging
import os

from utils import determine_delimiter

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_root.log")


targer_output_dir_path = "./targer_instance/data/out/"


def transform_output_into_csv(file_id, file_dir):
    out_results = process_targer_output_data(file_id, file_dir)
    if out_results.__len__() > 1:
        raise RuntimeError("Found multiple out files in request folder {0}!".format(file_id))
    if out_results.__len__() < 1:
        raise RuntimeError("Found no out files in request folder {0}! Perform a tagging request first.".format(file_id))

    csv_list = [["clause_index", "text", "label"]]
    blocks = out_results[0]["blocks"]
    for idx, block in enumerate(blocks):
        label = ""
        text = ""
        for word_obj in block:
            word_label = word_obj["label"]
            if word_label in ["Claim", "Premise"]:
                label = word_label
                word = word_obj["token"]
                text += "%s%s" % (determine_delimiter(word), word)
        if label in ["Claim", "Premise"]:
            csv_list.append([idx + 1, text.strip(), label])  # user-friendly 1-based indexing
    return csv_list


def processing_helper(stack, clause_counter):
    if stack[0]["label"].split("-")[0] == "O":
        curr_label = "O"
    else:
        curr_label = stack[0]["label"].split("-")[1]
    clause = {
        "text": "",
        "label": curr_label,
        "idx": clause_counter
    }

    # Split clauses based on switching label.
    prev_label = curr_label
    while curr_label == prev_label:
        clause["text"] += "%s%s" % (determine_delimiter(stack[0]["token"]), stack[0]["token"])

        stack.pop(0)
        if not len(stack):
            break
        if stack[0]["label"].split("-")[0] == "O":
            curr_label = "O"
        else:
            curr_label = stack[0]["label"].split("-")[1]
    clause["text"] = clause["text"].strip()
    return clause, stack


def process_targer_output_data(doc_id, doc_path):
    print('Output_dir:' + str(doc_path))
    dir_contents = os.listdir(doc_path)
    dir_contents.sort()  # TODO: optional, may be performance relevant
    output_files = [file for file in dir_contents if file[-4:] == ".out"]

    results = []
    for file in output_files:
        file_dict = {
            "doc_id": doc_id,
            "premises": [],
            "claims": [],
            "blocks": []
        }

        with open(os.path.join(doc_path, file)) as corpus_file:
            # Load and parse data from json file to dictionary.
            raw_data = json.load(corpus_file)
            stack = raw_data["results"][0]

            clause_counter = 1  # user-friendly 1-based indexing
            while len(stack):
                # Retrieve clauses of tokens with consecutive label.
                clause, stack = processing_helper(stack, clause_counter)
                clause_counter += 1

                if clause["label"] == "Premise":
                    file_dict["premises"].append(clause)
                elif clause["label"] == "Claim":
                    file_dict["claims"].append(clause)
                file_dict["blocks"].append(clause)

            results.append(file_dict)
    return results


if __name__ == "__main__":
    logging.info(process_targer_output_data(1, targer_output_dir_path))
