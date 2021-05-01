import json
import logging
import os

from utils import ClauseHandler

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_root.log")


targer_output_dir_path = "./backend/targer_instance/data/out/"


def process_single_block(block, word_index):
    word_index_beginning = word_index
    text = ''
    tag = None
    word_tag = None
    block_list = []
    for tagged_word in block:
        if tagged_word['label'] == 'B-Premise':
            tag = 'premise'
            word_tag = 'premise'
        elif tagged_word['label'] == 'B-Claim':
            tag = 'claim'
            word_tag = 'claim'
        elif tagged_word['label'] == 'O':
            word_tag = 'O'
        text = ' '.join([text, tagged_word['token']])
        block_dict = {
            'token': tagged_word['token'],
            'label': word_tag,
            'idx': word_index
        }
        block_list.append(block_dict)
        word_index = word_index + 1
    clause_dict = {
        'text': text,
        'tag': tag,
        'idx': word_index_beginning
    }
    return text, clause_dict, tag, block_list, word_index


def process_single_block_with_prob(block, word_index):
    word_index_beginning = word_index
    total_prob = 0
    i = 0
    text = ''
    tag = None
    word_tag = None
    block_list = []
    for tagged_word in block:
        if tagged_word['label'] == 'B-Premise':
            tag = 'premise'
            word_tag = 'premise'
        elif tagged_word['label'] == 'B-Claim':
            tag = 'claim'
            word_tag = 'claim'
        elif tagged_word['label'] == 'O':
            word_tag = 'O'
        text = ' '.join([text, tagged_word['token']])
        total_prob = float(tagged_word['prob']) + total_prob
        block_dict = {
            'token': tagged_word['token'],
            'label': word_tag,
            'prob': tagged_word['prob'],
            'idx': word_index
        }
        block_list.append(block_dict)
        word_index = word_index + 1
        i = i + 1
    clause_dict = {
        'text': text,
        'tag': tag,
        'prob': total_prob/i,
        'idx': word_index_beginning
    }
    return text, clause_dict, tag, block_list, word_index


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
            'claims': [],
            'blocks': []
        }

        with open(os.path.join(doc_path, file)) as corpus_file:
            # ========== load and parse data from json file to dictionary ==========
            word_index = 0
            raw_data = json.load(corpus_file)
            for block in raw_data['results']:
                label_dict = block[0]
                if 'prob' in label_dict.keys():
                    text, clause_dict, tag, block_list, word_index = process_single_block_with_prob(block, word_index)
                else:
                    text, clause_dict, tag, block_list, word_index = process_single_block(block, word_index)
                file_dict['text'] = file_dict['text'] + text
                if tag == 'premise':
                    file_dict['premises'].append(clause_dict)
                elif tag == 'claim':
                    file_dict['claims'].append(clause_dict)
                file_dict['blocks'].append(block_list)
            results.append(file_dict)
    print(results[0]['blocks'][0])
    return results


if __name__ == "__main__":
    logging.info(process_targer_output_data(1))
