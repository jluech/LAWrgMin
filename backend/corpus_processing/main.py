import json
import os

from shutil import copyfile


echr_corpus_path = os.path.join(os.getcwd(), "datasets/echr_corpus/ECHR_Corpus.json")


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
    trimmed_sentence = sentence.replace("  ", "").replace("\r", "").replace("\n", " ").replace("\t", " ").strip()
    start = trimmed.find(trimmed_sentence)
    end = start + len(trimmed_sentence)
    return start, end, trimmed_sentence


def conll_to_pe_file_level(file):
    pe_string = ''
    index = 1
    with open(file) as f:
        content = f.readlines()
        for line in content:
            if line != '\n' and line != '' and line != ' ':
                pe_string = pe_string + str(index) + '\t' + line.replace(' ', '\t')
                index = index + 1
    return pe_string


def conll_to_pe_sentence_level(file):
    pe_string = ''
    words_in_sentence = 1
    with open(file) as f:
        content = f.readlines()
        for line in content:
            if line != '\n' and line != '' and line != ' ':
                pe_string = pe_string + str(words_in_sentence) + '\t' + line.replace(' ', '\t')
                if line[0] == '.' or line[0] == '!' or line[0] == '?':
                    words_in_sentence = 1
                else:
                    words_in_sentence = words_in_sentence + 1
    return pe_string


def parse_corpus_data():
    print('Transforming ECHR dataset to brat standoff format...')
    with open(echr_corpus_path) as corpus_file:
        # ========== load and parse data from json file to dictionary ==========
        data = json.load(corpus_file)  # corpus yields list of 42 decision entries as json-dicts
        # data dict keys and types:
        # name: string
        # text: string (long, multiline, pdf-formatted)
        # clauses: dict
        # arguments: dict

        orig_wd = os.getcwd()

        for index, case in enumerate(data):

            text = case['text']
            trimmed = text.replace("  ", "").replace("\r", "").replace("\n", " ").replace("\t", " ").strip()

            clauses = case['clauses']

            case_annotated = ''

            tag_counter = 1
            relation_counter = 1

            for argument in case['arguments']:
                premises = argument['premises']

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
            ann_filename = os.path.join(out_dir, case["name"].replace('.txt', '.ann'))
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

            copyfile('annotation.conf', out_dir + '/annotation.conf')

            path = 'standoff2conll'
            if not os.path.exists(path):
                os.system('git clone https://github.com/spyysalo/standoff2conll')
            os.chdir(path)
            new_path = os.getcwd().replace(path.replace('.', '', 1), '')
            file_out_dir = new_path + out_dir.replace('.', '', 1)

            print('Converting standoff format into .connl for case ' + case['name'] + '...')

            # Run command with disabled output
            os.system('python standoff2conll.py {__file_out_dir} >/dev/null 2>&1'.format(__file_out_dir=file_out_dir))

            os.chdir(orig_wd)
            print('Converting .connl format into pe_conll for case ' + case['name'] + '...')
            # for sentence level tagging
            # pe_text = conll_to_pe_sentence_level(ann_filename.replace('.ann', '.conll'))
            pe_text = conll_to_pe_file_level(ann_filename.replace('.ann', '.conll'))

            pe_filename = ann_filename.replace('.ann', '_pe.conll')
            if os.path.exists(pe_filename):
                os.remove(pe_filename)

            pe_casefile = open(pe_filename, 'x')
            pe_casefile.write(pe_text)
            pe_casefile.write('')
            pe_casefile.close()

            print('Case ' + case['name'] + ' finished')
    print('Done!')


if __name__ == "__main__":
    parse_corpus_data()
