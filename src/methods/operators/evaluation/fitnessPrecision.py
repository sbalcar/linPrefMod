#!/usr/bin/python3

# ratingsPredicted:list<float>, ratingsOriginal:list<float>
def fitnessPrecision(ratingsPredicted, ratingsOriginal, compliantRating=0.9):

    #print("Len: " + str(len(ratingsOriginal)))

    # itemIDsPredicted:list<int>
    predictedElement = [i for i in range(len(ratingsPredicted)) if ratingsPredicted[i] >= compliantRating]
    relevantElement = [i for i in range(len(ratingsOriginal)) if ratingsOriginal[i] >= compliantRating]

    # truePositiveElements:list<int>
    truePositiveElements = set(predictedElement).intersection(relevantElement)

    if len(predictedElement) == 0:
        return None

    #print("TruePositive:" + str(float(len(truePositiveElements))))
    #print("Neco: " + str(float(len(predictedElement))))

    return float(len(truePositiveElements)) / float(len(predictedElement))