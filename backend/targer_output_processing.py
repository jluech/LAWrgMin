import itertools
import json
import os
from utils import ClauseHandler

targer_output_dir_path = "../miners/targer_instance/data/out"


def determine_delimiter(token):
    if token.__len__() > 1:
        return " "
    if token.isalnum() or token in "({":
        return " "
    return ""


def process_single_block(block):
    # clause : {'clause_id: , 'text': , 'tag': ''}
    clause_handler = ClauseHandler()
    text = ''
    tag = None
    for tagged_word in block:
        if tagged_word['label'] == 'B-Premise':
            tag = 'premise'
        if tagged_word['label'] == 'B-Claim':
            tag = 'claim'
        text = text + ' ' + tagged_word['token']
    dict = {
        'clause_id': clause_handler.clause_id,
        'text': text,
        'tag': tag
    }
    type = tag
    return text, dict, type


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
        if tagged_word['label'] == 'B-Claim':
            tag = 'claim'
        text = text + ' ' + tagged_word['token']
        total_prob = float(tagged_word['prob']) + total_prob
        i = i + 1
    dict = {
        'clause_id': clause_handler.clause_id,
        'text': text,
        'tag': tag,
        'prob': total_prob/i
    }
    type = tag
    return text, dict, type

def process_targer_output_data(doc_id, doc_path=targer_output_dir_path):
    dir_contents = os.listdir(doc_path)
    dir_contents.sort()  # TODO: optional, may be performance relevant
    # print(dir_contents)
    output_files = [file for file in dir_contents if file[-4:] == ".out"]
    print(output_files)
    print("====================")
    results = []
    # for file in output_files:
    for file in output_files:
        file_dict = {
            'doc_id': doc_id,
            'text': '',
            'premises': [],
            'claims': []
        }
        with open("/".join([targer_output_dir_path, file])) as corpus_file:
            # ========== load and parse data from json file to dictionary ==========
            raw_data = json.load(corpus_file)
            for block in raw_data['results']:
                print('floating through space')
                label_dict = block[0]
                if 'prob' in label_dict.keys():
                    text, clause_dict, type = process_single_block_with_prob(block)
                else:
                    text, clause_dict, type = process_single_block(block)
                file_dict['text'] = file_dict['text'] + text
                if type == 'premise':
                    file_dict['premises'].append(clause_dict)
                else:
                    file_dict['claims'].append(clause_dict)
            results.append(json.dumps(file_dict))
    return results

if __name__ == "__main__":
    print(process_targer_output_data(1))
