import json
import os

targer_output_dir_path = "../miners/targer_instance/data/out"


def determine_delimiter(token):
    if token.__len__() > 1:
        return " "
    if token.isalnum() or token in "({":
        return " "
    return ""


def process_targer_output_data():
    dir_contents = os.listdir(targer_output_dir_path)
    dir_contents.sort()  # TODO: optional, may be performance relevant
    # print(dir_contents)
    output_files = [file for file in dir_contents if file[-4:] == ".out"]
    print(output_files)
    print("====================")

    # for file in output_files:
    for file in output_files:
        print(file)
        with open("/".join([targer_output_dir_path, file])) as corpus_file:
            # ========== load and parse data from json file to dictionary ==========
            raw_data = json.load(corpus_file)
            data = raw_data[0]  # raw data from output file has structure of array-of-array-of-elem = [[...elem]]
            # print(data)

            stats = {}
            sentences = []
            rolling_sentence_struct = {}
            in_sentence = False

            # TODO: might check out if we define sentences from-to P-B labels.
            # TODO: Catch initially mismatching labels in separate sentence.
            for elem in data:
                # print(elem)
                label = elem["label"]
                token = elem["token"]
                stats_labels = stats.keys()

                if label not in stats_labels:
                    stats[label] = [token]
                else:
                    stats[label].append(token)

                if label == "P-B":
                    in_sentence = True
                    rolling_sentence_struct["raw_sentence"] = token
                    rolling_sentence_struct["elems"] = [elem]
                else:
                    if in_sentence:
                        # print(token)
                        # delimiter = " " if token.__len__() > 1 else ""
                        delimiter = determine_delimiter(token)
                        rolling_sentence_struct["raw_sentence"] += delimiter + token
                        rolling_sentence_struct["elems"].append(elem)
                    else:
                        rolling_sentence_struct["raw_sentence"] = token
                        rolling_sentence_struct["elems"] = [elem]
                if label == "O":
                    in_sentence = False
                    # print(rolling_sentence_struct["raw_sentence"])
                    sentences.append(rolling_sentence_struct)
                    rolling_sentence_struct = {}

            for key in stats.keys():
                print(key, ":", stats[key].__len__())
            print("sentences:", sentences.__len__())
            print("====================")


if __name__ == "__main__":
    process_targer_output_data()
