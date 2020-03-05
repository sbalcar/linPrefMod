#!/usr/bin/python3

# ratingsPredicted:list<float>, ratingsOriginal:list<float>
def fitnessRecall(ratingsPredicted, ratingsOriginal, compliantRating=0.9):

    # itemIDsPredicted:list<int>
    predictedElement = [i for i in range(len(ratingsPredicted)) if ratingsPredicted[i] >= compliantRating]
    relevantElement = [i for i in range(len(ratingsOriginal)) if ratingsOriginal[i] >= compliantRating]

    # truePositiveElements:list<int>
    truePositiveElements = set(predictedElement).intersection(relevantElement)

    if len(relevantElement) == 0:
        return None

    return float(len(truePositiveElements)) / float(len(relevantElement))
