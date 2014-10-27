import convertJson

allRestaurants = convertJson.readRestaurants(['business_id','name','stars','review_count'])

goodRestaurants = convertJson.readGoodRestaurants(800)

trueRating = convertJson.trueRatings(goodRestaurants)
print trueRating
#textualRating = convertJson.textualRatings(goodRestaurants)
