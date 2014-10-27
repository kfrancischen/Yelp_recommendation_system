
import json
import subprocess
from collections import defaultdict

# read the restaurant data sets, it will generate the dataset for all the restaurants with desired keys
# output is a list of dictionaries
def readRestaurants(keys):
	filePath = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json'
	outputData = []
	with open(filePath) as inputJson:
		for line in inputJson:
			while True:
				try:
					json_data = json.loads(line)
					#print json_data[u'name'], '\n'
					singleRestaurant = {}
					for key in keys:
						singleRestaurant[key] = json_data[key]
					outputData.append(singleRestaurant)
					break
				except ValueError:
					line += next(inputJson)
	inputJson.close()
	return outputData
	
# focus on the restaurants with at least minReivews
# output the same data structure, which is a list of dictionaries.
def readGoodRestaurants(minReview):
	allRestaurants = readRestaurants(['business_id','name','stars','review_count'])
	goodRestaurants = []
	for i in range(len(allRestaurants)):
		if allRestaurants[i]['review_count'] >= minReview:
			goodRestaurants.append(allRestaurants[i])
	return goodRestaurants

# calculate the true ratings (average over star rating) of all the input restaurants
def trueRatings(restaurants):
	filePath = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'
	trueRating = {}
	for i in range(len(restaurants)):
		trueRating[restaurants[i]['business_id']]=0
	with open(filePath) as inputJson:
		for line in inputJson:
			while True:
				try:
					json_data = json.loads(line)
					index = [i for i in range(len(restaurants)) if restaurants[i]['business_id'] == json_data['business_id']]
					if index != []:
						business_id = restaurants[index[0]]['business_id']
						trueRating[business_id] += json_data['stars']
					break
				except ValueError:
					line += next(inputJson)
	inputJson.close()
	for i in range(len(restaurants)):
		trueRating[restaurants[i]['business_id']] /= float(restaurants[i]['review_count'])
	return trueRating


# calculate the textural derived rating based on the online sentiment analysis
def textualRatings(restaurants):
	filePath = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'
	textualRating = {}
	positive = {}
	negative = {}
	for i in range(len(restaurants)):
		textualRating[restaurants[i]['business_id']] = 0
		positive[restaurants[i]['business_id']] = 0
		negative[restaurants[i]['business_id']] = 0
	with open(filePath) as inputJson:
		for line in inputJson:
			while True:
				try:
					json_data = json.loads(line)
					index = [i for i in range(len(restaurants)) if restaurants[i]['business_id'] == json_data['business_id']]
					if index != []:
						business_id = restaurants[index[0]]['business_id']
						onlineRequest = 'curl -d "text='+json_data['text']+'" http://text-processing.com/api/sentiment/'
						sentiment = subprocess.check_output(onlineRequest, shell=True)
						print sentiment
						sentiment = json.loads(sentiment)
						if sentiment['label'] == 'pos':
							positive[business_id] += 1
						elif sentiment['label'] == 'neg':
							negative[business_id] += 1
					break
				except ValueError:
					line += next(inputJson)
	inputJson.close()
	for i in range(len(restaurants)):
		P = positive[restaurants[i]['business_id']];
		N = negative[restaurants[i]['business_id']];
		textualRating[restaurants[i]['business_id']] = float(P)/(N+P)*4+1;
	return textualRating


# some tests
#allRestaurants=readRestaurants(['business_id','name','stars','review_count'])
# print allRestaurants
#goodRestaurants = readGoodRestaurants(800)
# print goodRestaurants
# trueRating = trueRatings(goodRestaurants)
# print trueRating
#textualRating = textualRatings(goodRestaurants)
#print textualRating

