import numpy as np

def errorTesting(textualRating, trueRating,bins):
	textR = textualRating.values()
	trueR = trueRating.values()
	textHist, _ = np.histogram(textR, bins)
	trueHist, _ = np.histogram(trueR, bins)
	#print textHist,trueHist
	weights=[]
	for i in range(len(bins)-1):
		weights.append((bins[i]+bins[i+1])/2)
#	print weights
	textHist = list(textHist)
	trueHist = list(trueHist)
	print textHist,trueHist
	textVariance = 0
	trueVariance = 0
	for i in range(len(textHist)):
		textHist[i] /= float(sum(textHist))
		trueHist[i] /= float(sum(trueHist))

	for i in range(len(textHist)):
		textVariance += (textHist[i]-np.average(textHist))**2
		trueVariance += (trueHist[i] -np.average(trueHist))**2
	score = (trueVariance - textVariance)**2 + (np.average(textHist,weights=weights) - np.average(trueHist,weights=weights))**2	
	return score

# print errorTesting({'a':1,'b':2},{'a':2,'b':1,'c':1},[0.5,1.5,2.5])
