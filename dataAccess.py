#!/usr/bin/python

# Open the Yelp dataset
<<<<<<< HEAD
fileDir= '/Users/jennifer/yelp_dataset_challenge_academic_dataset 2/'
fileName = 'yelp_academic_dataset_checkin.json'
filePath = fileDir+fileName
=======
#fileDir= '/Users/jennifer/yelp_dataset_challenge_academic_dataset 2/'
fileName = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_checkin.json'
filePath = fileName
>>>>>>> 884159304c57cbfbbea7dc1b7fb03d007e533442
maxlines = 15

import json

with open(filePath) as f:
<<<<<<< HEAD
# 'with' statement can automatically close the file
=======
>>>>>>> 884159304c57cbfbbea7dc1b7fb03d007e533442
	counter = 0
	for line in f:
		if counter > maxlines:
			break
		while True:
			counter +=1
			try:
<<<<<<< HEAD
				json_data = json.loads(line) 
				print(json_data)
				break
			except ValueError:
				line += next(f)

print(type(json_data))


#if __name__ == '__main__':

=======
					json_data = json.loads(line) 
					print(json_data)
					break
			except ValueError:
					line += next(f)

f.close( )
	
>>>>>>> 884159304c57cbfbbea7dc1b7fb03d007e533442
