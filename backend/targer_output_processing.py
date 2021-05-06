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
            csv_list.append([idx, text.strip(), label])
    return csv_list


def processing_helper(stack, counter):
    block_list = []

    if stack[0]['label'].split('-')[0] == 'O':
        curr_tag = 'O'
    else:
        curr_tag = stack[0]['label'].split('-')[1]
    clause = {
        'text': '',
        'tag': curr_tag,
        'idx': counter
    }
    prev_tag = curr_tag
    while curr_tag == prev_tag:
        clause['text'] = clause['text'] + ' ' + stack[0]['token']
        counter = counter + 1
        block_dict = {
            'token': stack[0]['token'],
            'label': curr_tag,
            'idx': counter
        }
        block_list.append(block_dict)
        stack.pop(0)
        if not len(stack):
            break
        if stack[0]['label'].split('-')[0] == 'O':
            curr_tag = 'O'
        else:
            curr_tag = stack[0]['label'].split('-')[1]
    return block_list, clause, stack, counter


def process_targer_output_data(doc_id, doc_path=targer_output_dir_path):
    dir_contents = os.listdir(doc_path)
    dir_contents.sort()  # TODO: optional, may be performance relevant
    output_files = [file for file in dir_contents if file[-4:] == ".out"]

    results = []
    for file in output_files:
        file_dict = {
            'doc_id': doc_id,
            'text': '',
            'premises': [],
            'claims': [],
            'blocks': []
        }
        with open(os.path.join(doc_path, file)) as corpus_file:
            # ========== load and parse data from json file to dictionary ==========
            raw_data = json.load(corpus_file)
            stack = raw_data['results'][0]
            word_counter = 0
            while len(stack):
                block_list, clause, stack, word_counter = processing_helper(stack, word_counter)
                file_dict['text'] = file_dict['text'] + clause['text']
                if clause['tag'] == 'Premise':
                    file_dict['premises'].append(clause)
                elif clause['tag'] == 'Claim':
                    file_dict['claims'].append(clause)
                file_dict['blocks'].append(block_list)
            results.append(file_dict)
    return results


if __name__ == "__main__":
    logging.info(process_targer_output_data(1))
