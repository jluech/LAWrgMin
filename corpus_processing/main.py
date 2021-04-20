import json
import numpy as np
from operator import itemgetter
import os
import sys
from shutil import copyfile
import bconv


echr_corpus_path = "/home/adrian/Desktop/FS2021/AI/Project/LAWrgMin/corpus_processing/datasets/echr_corpus/ECHR_Corpus.json"  # local linux path, not repo specific


def find_clause_from_id(clauses, id):
    for clause in clauses:
        if clause['_id'] == id:
            return clause


def is_major_argument(argument, case):
    for premise_id in argument['premises']:
        for other_arguments in case['arguments']:
            if other_arguments['conclusion'] == premise_id:
                print('MAJOR_CLAIM_FOUND')
                return True
    return False


def get_start_end_trimmed(trimmed, sentence):
    trimmed_sentence = sentence.replace("  ", "").replace("\r", "").replace("\n", " ").strip()
    start = trimmed.find(trimmed_sentence)
    end = start + len(trimmed_sentence)
    return start, end, trimmed_sentence


def parse_corpus_data():
    with open(echr_corpus_path) as corpus_file:
        # ========== load and parse data from json file to dictionary ==========
        data = json.load(corpus_file)  # corpus yields list of 42 decision entries as json-dicts
        # print(data)
        # print(type(data))
        # print(data.__len__())

        # for decision in data:
        #     print(decision["name"])

        corpus_entry = data[1]  # 0 to 41
        keys = corpus_entry.keys()
        # name: string
        # text: string (long, multiline, pdf-formatted)
        # clauses: dict
        # arguments: dict
        print(keys)
        print()
        owd = os.getcwd()

        for index, case in enumerate(data):
            os.chdir(owd)

            text = case['text']
            trimmed = text.replace("  ", "").replace("\r", "").replace("\n", " ").strip()

            clauses = case['clauses']

            case_annotated = ''

            #tag counter
            tag_counter = 1

            #relation-counter
            relation_counter = 1

            for argument in case['arguments']:
                premises = argument['premises']

                claim_id = 0

                if is_major_argument(argument, case):
                    clause = find_clause_from_id(clauses, argument['conclusion'])
                    start, end, trimmed_sentence = get_start_end_trimmed(trimmed, text[clause['start']:clause['end']])
                    case_annotated = case_annotated + '\nT' + str(tag_counter) + '\tMajorClaim' + ' ' + str(start) + ' ' + str(end) + '\t' + trimmed_sentence
                    claim_id = tag_counter
                    tag_counter = tag_counter + 1
                else:
                    clause = find_clause_from_id(clauses, argument['conclusion'])
                    start, end, trimmed_sentence = get_start_end_trimmed(trimmed, text[clause['start']:clause['end']])
                    case_annotated = case_annotated + '\nT' + str(tag_counter) + '\tClaim' + ' ' + str(start) + ' ' + str(end) + '\t' + trimmed_sentence
                    claim_id = tag_counter
                    tag_counter = tag_counter + 1

                for premise_id in premises:
                    clause = find_clause_from_id(clauses, premise_id)
                    start, end, trimmed_sentence = get_start_end_trimmed(trimmed, text[clause['start']:clause['end']])
                    case_annotated = case_annotated + '\nT' + str(tag_counter) + '\tPremise ' + str(start) + ' ' + str(end) + '\t' + trimmed_sentence

                    case_annotated = case_annotated + '\nR' + str(relation_counter) + '\tsupports Arg1:T' + str(tag_counter) + ' Arg2:T' + str(claim_id)
                    tag_counter = tag_counter + 1

            out_dir = "./out/" + case['name'].replace('.txt', '')
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            ann_filename = "/".join([out_dir, case["name"].replace('.txt', '')]) + ".ann"
            if os.path.exists(ann_filename):
                os.remove(ann_filename)

            casefile = open(ann_filename, "x")
            casefile.write(case_annotated)
            casefile.close()

            filename = ann_filename.replace('.ann', '.txt')
            if os.path.exists(filename):
                os.remove(filename)

            casefile = open(filename, "x")
            casefile.write(trimmed)
            casefile.close()

            copyfile('annotation.conf', out_dir+'/annotation.conf')

            path = './standoff2conll'
            if not os.path.exists(path):
                clone = 'git clone https://github.com/spyysalo/standoff2conll'
                os.system(clone)
            os.chdir(path)
            cwd = os.getcwd()
            new_path = cwd.replace(path.replace('.', '', 1), '')
            os.system('python standoff2conll.py ' + new_path + out_dir.replace('.', '', 1) + ' ' + new_path + out_dir.replace('.', '', 1))
            print(path)
            print(new_path)

        # ========== extract trimmed text from each case and write to txt file ==========
        # out_dir = "./out"
        # if not os.path.exists(out_dir):
        #     os.mkdir(out_dir)
        # for index, case in enumerate(data):
        #     # filename = "/".join([out_dir, "case-"+str(index)+".txt"])
        #     filename = "/".join([out_dir, case["name"]])
        #     if os.path.exists(filename):
        #         os.remove(filename)
        #
        #     text = case["text"]
        #     trimmed = text.replace("  ", "").replace("\r", "").replace("\n\n", "\n").strip()
        #
        #     casefile = open(filename, "x")
        #     casefile.write(trimmed)
        #     casefile.close()

        # ========== further inspect specific first entry of corpus ==========
        # for key in keys:
        #     print(key, first_entry.get(key))
        # print("\n")

        # text = corpus_entry["text"]
        # print(type(text))
        # print(text)
        # trimmed = text.replace("  ", "").replace("\r", "").replace("\n\n", "\n").strip()
        # print(trimmed)
        # print()
        # print(repr(trimmed))

        # clauses = corpus_entry["clauses"]
        # print()
        # print(clauses.__len__(), "clauses")
        # for clause in clauses:
        #     print("clause", clause)

        # arguments = corpus_entry["arguments"]
        # print()
        # print(arguments.__len__(), "arguments")
        # for argument in arguments:
        #     print("argument", argument)

        # TODO: to extract individual sections (rough sketch, needs verification):
        # - instantiate sections_array=[] and last_index=0
        # - split string on blanks into array of words
        # - traverse words and check for all uppercase
        # - when finding uppercase word then save the current index
        #   add all previous words (since last saved index or 0) to temporary array (e.g., with concat() or join(" "))
        # - while traversed word is uppercase, add word to local key variable (join(" "))
        # - once traversed word is no longer uppercase, add dictionary containing key
        #   and concatenated words from last saved index to right before current saved index to sections array
        #   update saved index to current position for next key iteration
        # - decide if newlines are required within section text
        # - be mindful of properly trimming strings


if __name__ == "__main__":
    parse_corpus_data()
