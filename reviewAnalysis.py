import convertJson
import statsVisualize
import validating 

allRestaurants = convertJson.readRestaurants(['business_id','name','stars','review_count'])

goodRestaurants = convertJson.readGoodRestaurants(800)

trueRating = convertJson.trueRatings(goodRestaurants)
#print trueRating
# alpha = [0.05*i+1.05 for i in range(8)]
# alpha = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1]
alpha = [1.15, 1.2, 1.25, 1.3]
scores = []
bins = [1,1.5,2,2.5,3,3.5,4,4.5,5]

#for i in range(len(alpha)):
#	textualRating = convertJson.textualRatings(goodRestaurants,alpha[i])
#	scores.append(validating.errorTesting(textualRating, trueRating, bins))
textualRating = convertJson.textualRatings(goodRestaurants, 0.85)
# print validating.errorTesting(textualRating, trueRating, bins)
print 'The scores are ',scores
#optimalAlpha = scores.index(min(scores))
#print 'The best alpha is ', alpha[optimalAlpha], 'with minimum score', min(scores)
#textualRating = convertJson.textualRatings(goodRestaurants, alpha[optimalAlpha])
#print trueRating, textualRating
statsVisualize.visualizing(textualRating,trueRating,bins)

