# -*- coding: utf-8 -*-

import glob
import time
import json
import os
import warnings

warnings.filterwarnings("ignore")


def process(file):
	# ===== load file =====
	filename = "data/in/{0}.txt".format(file)
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
	from Model import Model
	model = Model("IBM.h5")
	# from ModelNewES import ModelNewES
	# model = ModelNewES()
	# from ModelNewSciArg import ModelNewSciArg
	# model = ModelNewSciArg()
	# from Model import Model
	# model = Model()

	# ===== process and label input text =====
	# raw_results = model.label(input_text)
	raw_results = model.label_with_probs(input_text)

	# ===== merge fragments with same label - losing probability =====
	merged_results = []
	for sentence in raw_results:
		current_label = ""
		words = []
		for word in sentence:
			if float(word["prob"]) < 0.9:
				print("prob < 0.9 in", word)
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
	out_dir = "data/out"
	out_path = "/".join([out_dir, file + ".out"])
	if not os.path.exists(out_dir):
		os.mkdir(out_dir)
	if os.path.exists(out_path):
		os.remove(out_path)

	# ===== write output to file =====
	# output = {"results": raw_results}
	output = {"results": merged_results}
	# output = {"results": text_only}

	print("\n> Writing output to file...")
	with open(out_path, "x") as f:
		json.dump(output, f)


if __name__ == "__main__":
	# ===== collect input files =====
	files = glob.glob("data/in/*.txt")
	# print("initial glob", files)
	files = [f.split("/")[-1].split('.')[0] for f in files]
	# print("split", files)
	files.sort()
	# print("sorted", files)
	print("=== Found files:", files, "===")

	# ===== process files and measure execution time =====
	times = []
	for file in files:
		print("\n=== Processing", file, "===")
		start_time = time.time()
		process(file)
		end_time = time.time()
		print("= Done processing file")
		times.append(end_time - start_time)
	
	# ===== write stats to file =====
	nr_files = len(files)
	timed = sum(times)
	avg_time = timed / nr_files

	print("\n> Writing overall stats to file...")
	stats_path = "data/out/stats.txt"
	if os.path.exists(stats_path):
		os.remove(stats_path)

	with open(stats_path, "x") as f:
		f.write("Nr. files:\t" + str(nr_files) + "\n")
		f.write("Total time:\t" + str(round(timed, 2)) + "\n")
		for idx, file in enumerate(files):
			f.write(file + ":\t" + str(round(times[idx], 2)) + "\n")

	print("=== Done ===")
