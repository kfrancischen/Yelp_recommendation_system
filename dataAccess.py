#!/usr/bin/python

# Open the Yelp dataset
#<<<<<<< HEAD
fileDir= 'yelp_dataset_challenge_academic_dataset/'
fileName = 'yelp_academic_dataset_checkin.json'
filePath = fileDir+fileName
maxlines = 1

import json

with open(filePath) as f:
# 'with' statement can automatically close the file
	counter = 0
	for line in f:
		if counter > maxlines:
			break
		while True:
			counter +=1
			try:
				json_data = json.loads(line) 
				print(json_data)
				break
			except ValueError:
				line += next(f)
f.close()
	
