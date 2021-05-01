# -*- coding: utf-8 -*-

import glob
import json
import logging
import os
import sys
import time
import warnings

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", filename="backend_targer.log")

in_dir = "data/in"
out_dir = "data/out"


def process(file):
    # ===== load file =====
    filename = "{__in_dir}/{__filename}.txt".format(__in_dir=in_dir, __filename=file)
    with open(filename, "r", encoding="utf-8") as f:
        input_text = f.read()

    # ===== address keras bug =====
    from Model import Model
    model = Model("IBM.h5")
    # We must call this because of a keras bug
    # https://github.com/keras-team/keras/issues/2397
    model.label("Therefore fixed punishment will")
    model.label_with_probs(input_text)

    # ===== select model =====
    # from Model import Model
    # model = Model("IBM.h5")
    # from ModelNewES import ModelNewES
    # model = ModelNewES()
    # from ModelNewSciArg import ModelNewSciArg
    # model = ModelNewSciArg()
    from ModelNewECHR import ModelNewECHR
    model = ModelNewECHR()
    # from Model import Model
    # model = Model()

    # ===== process and label input text =====
    raw_results = model.label(input_text)
    # raw_results = model.label_with_probs(input_text)
    print()  # targer has annoying prints with carriage sticking on same line

    # ===== merge fragments with same label - losing probability =====
    merged_results = []
    for sentence in raw_results:
        current_label = ""
        words = []
        for word in sentence:
            if word.keys().__contains__("prob") and float(word["prob"]) < 0.9:
                logging.debug("prob < 0.9 in %s", word)
                current_label = ""  # cut out unsure classification
                continue
            meta_label = word["label"][0]  # P or O
            if not current_label == meta_label:
                current_label = meta_label  # match following words with same meta label
                # instantiate new group for meta label not matching previous meta label
                words.append({"label": current_label, "text": []})
            words[-1]["text"].append(word["token"])  # add word to latest group's text
        merged_results.append(words)

    # ===== collect understandable text from merged results =====
    text_only = []
    for sentence in merged_results:
        for label_group in sentence:
            label = list(label_group.keys())[0]
            if not label == "O":
                text_only.append(label + "\t" + " ".join(label_group[label]))

    # ===== print any collected results =====
    # [print(raw_sentence) for raw_sentence in raw_results]
    # print(raw_results)
    # [print(merged_sentence) for merged_sentence in merged_results]
    # print(merged_results)
    # [print(nice_sentence) for nice_sentence in text_only]
    # print(text_only)

    # ===== prepare output directory =====
    out_path = "/".join([out_dir, file + ".out"])
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    if os.path.exists(out_path):
        os.remove(out_path)

    # ===== write output to file =====
    output = {"results": raw_results}
    # output = {"results": merged_results}
    # output = {"results": text_only}

    logging.info("> Writing output to file...")
    with open(out_path, "x") as f:
        json.dump(output, f)


def trigger_labelling_of_files():
    # ===== collect input files =====
    files = glob.glob(os.path.abspath("/".join([in_dir, "*.txt"])))
    files = [f.split(("/" if "/" in f else "\\"))[-1].split('.')[0] for f in files]
    files.sort()
    logging.debug("=== Found files: {__files} ===".format(__files=files))

    # ===== process files and measure execution time =====
    times = []
    for file in files:
        logging.info("=== Labelling %s ===", file)
        start_time = time.time()
        process(file)
        end_time = time.time()
        logging.info("= Done processing file")
        times.append(end_time - start_time)

    # ===== write stats to file =====
    nr_files = len(files)
    timed = sum(times)

    logging.debug("> Writing overall stats to file...")
    stats_path = "{0}/stats.txt".format(out_dir)
    if os.path.exists(stats_path):
        os.remove(stats_path)

    with open(stats_path, "x") as f:
        f.write("Nr. files:\t" + str(nr_files) + "\n")
        f.write("Total time:\t" + str(round(timed, 2)) + "\n")
        for idx, file in enumerate(files):
            f.write(file + ":\t" + str(round(times[idx], 2)) + "\n")


if __name__ == "__main__":
    args = sys.argv[1:]  # ignore first arg as it's the script
    if args.__len__() > 0:
        if args.__contains__("-i"):
            in_dir = os.path.abspath(args[args.index("-i") + 1])
            logging.debug("Reading labelling input from %s", in_dir)
        if args.__contains__("-o"):
            out_dir = os.path.abspath(args[args.index("-o") + 1])
            logging.debug("Saving labelling output to %s", out_dir)

    trigger_labelling_of_files()
    logging.info("=== Done ===")
