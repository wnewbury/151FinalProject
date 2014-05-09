import random
import util

def RL(character, weights, baseEvaluationScore, endEvaluationScore, features, reward, learningRate, discountFactor):

	difference = (reward + discountFactor*endEvaluationScore) - baseEvaluationScore

	weightKeys = weights.keys()
	featureKeys = features.keys()

	newWeights = util.Counter()

	for key in weightKeys:
		weight = weights[key]
		newWeight = weight + learningRate*difference*features[key]
		if newWeight > 100000:
			newWeight = 100000
		if newWeight < -100000:
			newWeight = -100000
		newWeights[key] = newWeight

	newWeights.normalize()

	return newWeights