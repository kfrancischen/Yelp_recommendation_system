import convertJson
import statsVisualize
import validating 

allRestaurants = convertJson.readRestaurants(['business_id','name','stars','review_count'])

goodRestaurants = convertJson.readGoodRestaurants(800)

trueRating = convertJson.trueRatings(goodRestaurants)
#print trueRating
alpha = [0.2*(i+1) for i in range(10)]
scores = []
bins = [1,1.5,2,2.5,3,3.5,4,4.5,5]

for i in range(len(alpha)):
	textualRating = convertJson.textualRatings(goodRestaurants,alpha[i])
	scores.append(validating.errorTesting(textualRating, trueRating, bins))
print scores

#print trueRating, textualRating

#textualRating = convertJson.textualRatings(goodRestaurants,1)
#statsVisualize.visualizing(textualRating,trueRating,5)

