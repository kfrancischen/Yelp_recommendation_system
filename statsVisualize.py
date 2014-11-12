import numpy
import matplotlib.pyplot as plt

def visualizing(textualRating, trueRatings, bins):
	textR = textualRating.values()
	trueR = trueRatings.values()
	plt.figure(1)
	plt.hist(textR, bins, color = 'green')
	plt.xlabel('Ratings')
	plt.ylabel('Rating distribution')
	plt.title(r'Histogram for textual based ratings')
	plt.figure(2)
	plt.hist(trueR, bins, color = 'blue')
	plt.xlabel('Ratings')
	plt.ylabel('Rating distribution')
	plt.title(r'Histogram for true ratings')
	plt.show()
	return 

#ratings={'a':1,'b':1,'c':2,'d':3}
#visualizing(ratings, 3)
