# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings("ignore")
import glob
import time
import json

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

	#from ModelNewES import ModelNewES
	#model = ModelNewES()
	from ModelNewSciArg import ModelNewSciArg
	model = ModelNewSciArg()
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
	
	f = open('data/out/' + file +'.out', 'w+')
	json.dump(res, f)
	"""
	for r in res[:-1]:
		f.write(r + '\n')
	r = res[-1]
	f.write(r)
	"""
	

if __name__ == "__main__":
	files = glob.glob('data/in/*.txt')
	files = [f.split('/')[-1].split('.')[0] for f in files]
	files.sort()
	#files = ['A01']
	
	times = []
	for file in files:
		print('Processing ' + file)
		start_time = time.time()
		process(file)
		end_time = time.time()
		times.append(end_time - start_time)
	
	no_files = len(files)
	timed = sum(times)
	avg_time = timed / no_files
	
	f = open('data/out/stats.txt', 'w+')
	f.write('No. files:\t' + str(no_files) + '\n')
	f.write('Total time:\t' + str(round(timed, 2)) + '\n')
	for i, file in enumerate(files):
		f.write(file + ':\t' + str(round(times[i], 2)) + '\n')	
