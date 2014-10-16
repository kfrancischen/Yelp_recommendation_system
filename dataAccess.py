#!/usr/bin/python

# Open the Yelp dataset
fileDir= '/Users/jennifer/yelp_dataset_challenge_academic_dataset 2/'
fileName = 'yelp_academic_dataset_checkin.json'
filePath = fileDir+fileName
maxlines = 15

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

print(type(json_data))


#if __name__ == '__main__':

