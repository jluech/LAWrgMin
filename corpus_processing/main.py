import json

echr_corpus_path = "/datasets/echr_corpus/ECHR_Corpus.json"  # local linux path, not repo specific


def parse_corpus_data():
    with open(echr_corpus_path) as corpus_file:
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

        # for key in keys:
        #     print(key, first_entry.get(key))
        # print("\n")

        text = corpus_entry["text"]
        # print(type(text))
        # print(text)
        trimmed = text.replace("  ", "").replace("\r", "").replace("\n\n", "\n").strip()
        print(trimmed)
        print()
        print(repr(trimmed))

        clauses = corpus_entry["clauses"]
        print()
        print(clauses.__len__(), "clauses")
        for clause in clauses:
            print("clause", clause)

        arguments = corpus_entry["arguments"]
        print()
        print(arguments.__len__(), "arguments")
        for argument in arguments:
            print("argument", argument)

        # to extract individual sections:
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
