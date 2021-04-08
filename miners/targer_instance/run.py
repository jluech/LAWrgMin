# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings("ignore")
import glob
import time
import json
import os

def process(file):
	filename = 'data/in/' + file +'.txt'

	# load file
	with open(filename, 'r', encoding='utf-8') as f:
		inputtext = f.read()

	from Model import Model
	model = Model('IBM.h5')
	#We must call this cause of a keras bug
	#https://github.com/keras-team/keras/issues/2397
	model.label('Therefore fixed punishment will')
	result = model.label_with_probs(inputtext)

	from ModelNewES import ModelNewES
	model = ModelNewES()
	# model = ModelNewSciArg()
	# from ModelNewSciArg import ModelNewSciArg
	# from Model import Model
	# model = Model()
	result = model.label(inputtext)
	res = result

	"""
	#print(result)
	#print('======================')
	res = []
	for sentence in result:
		for word in sentence:
			token = word['token']
			label = word['label'][::-1]
			res.append(token + '\t' + label)
				
	# merge parts for single label
	out = []
	for sentence in result:
		out.append([])
		curr = ''
		for word in sentence:
			#print(word)
			#if float(word['prob']) < 0.9:
			#	curr = ''
			#	continue
			if not curr == word['label'][0]:
				curr = word['label'][0]
				out[-1].append({curr : []})
			out[-1][-1][curr].append(word['token'])

	#out = [o for sub in out for o in sub]
	res = []
	for o in out:
		for i in o:
			key = list(i.keys())[0]
			if not key == 'O':
				res.append(key + '\t' + ' '.join(list(i.values())[0]))
	"""
	
	#[print(o) for o in out]
	#print(out)
	#[print(o) for o in res]
	#print(res)
	out_dir = 'data/out'
	out_path = '/'.join([out_dir, file+'.out'])
	if not os.path.exists(out_dir):
		os.mkdir(out_dir)
	if os.path.exists(out_path):
		os.remove(out_path)
	# if not os.path.exists(out_path):
		# new = open(out_path, "x")
		# new.close()

	# f = open(out_path, 'w+')
	# with open(out_path, 'w+') as f:
	with open(out_path, 'x') as f:
		json.dump(res, f)
	"""
	for r in res[:-1]:
		f.write(r + '\n')
	r = res[-1]
	f.write(r)
	"""
	

if __name__ == "__main__":
	files = glob.glob('data/in/*.txt')
	# print("initial glob", files)
	files = [f.split('/')[-1].split('.')[0] for f in files]
	# print("split", files)
	files.sort()
	# print("sorted", files)
	print("Found files:", files)
	#files = ['A01']
	
	times = []
	for file in files:
		print('\nProcessing ' + file)
		start_time = time.time()
		process(file)
		end_time = time.time()
		times.append(end_time - start_time)
	
	no_files = len(files)
	timed = sum(times)
	avg_time = timed / no_files

	print("\nWriting stats to file...")
	stats_path = 'data/out/stats.txt'
	if os.path.exists(stats_path):
		os.remove(stats_path)
	# f = open(stats_path, 'w+')
	f = open(stats_path, 'x')
	f.write('No. files:\t' + str(no_files) + '\n')
	f.write('Total time:\t' + str(round(timed, 2)) + '\n')
	for i, file in enumerate(files):
		f.write(file + ':\t' + str(round(times[i], 2)) + '\n')
	print("=== Done ===")
