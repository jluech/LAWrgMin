import json
import logging
import os

from utils import ClauseHandler

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_root.log")


targer_output_dir_path = "./targer_instance/data/out"


def process_single_block(block):
    # block : [{token, label}]
    # clause : {'clause_id: , 'text': , 'tag': ''}
    clause_handler = ClauseHandler()
    text = ''
    tag = None
    for tagged_word in block:
        if tagged_word['label'] == 'B-Premise':
            tag = 'premise'
        elif tagged_word['label'] == 'B-Claim':
            tag = 'claim'
        text = ' '.join([text, tagged_word['token']])
    clause_dict = {
        'clause_id': clause_handler.clause_id,
        'text': text,
        'tag': tag
    }
    return text, clause_dict, tag


def process_single_block_with_prob(block):
    # block : [{prob, token, label}]
    # clause : {'clause_id: , 'text': , 'tag': '', 'probability': }
    clause_handler = ClauseHandler()
    total_prob = 0
    i = 0
    text = ''
    tag = None
    for tagged_word in block:
        if tagged_word['label'] == 'B-Premise':
            tag = 'premise'
        elif tagged_word['label'] == 'B-Claim':
            tag = 'claim'
        text = ' '.join([text, tagged_word['token']])
        total_prob = float(tagged_word['prob']) + total_prob
        i = i + 1
    clause_dict = {
        'clause_id': clause_handler.clause_id,
        'text': text,
        'tag': tag,
        'prob': total_prob/i
    }
    return text, clause_dict, tag


def process_targer_output_data(doc_id, doc_path=targer_output_dir_path):
    dir_contents = os.listdir(doc_path)
    dir_contents.sort()  # TODO: optional, may be performance relevant
    output_files = [file for file in dir_contents if file[-4:] == ".out"]

    results = []
    # for file in output_files:
    for file in output_files:
        file_dict = {
            'doc_id': doc_id,
            'text': '',
            'premises': [],
            'claims': []
        }

        with open("/".join([doc_path, file])) as corpus_file:
            # ========== load and parse data from json file to dictionary ==========
            raw_data = json.load(corpus_file)
            for block in raw_data['results']:
                label_dict = block[0]
                if 'prob' in label_dict.keys():
                    text, clause_dict, tag = process_single_block_with_prob(block)
                else:
                    text, clause_dict, tag = process_single_block(block)
                file_dict['text'] = file_dict['text'] + text
                if tag == 'premise':
                    file_dict['premises'].append(clause_dict)
                elif tag == 'claim':
                    file_dict['claims'].append(clause_dict)
            results.append(file_dict)
    return results


if __name__ == "__main__":
    logging.info(process_targer_output_data(1))
