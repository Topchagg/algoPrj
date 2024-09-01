from timeDeltaIntoHumanize import *
from checkIsInDiapasone import *
from TimeStrIntoTimeDelta import *

def addCutsToList(listOfCuts, possibleCuts, possibleTimeTaskStart):
    isAbleToOrder = True

    for subCut in listOfCuts:
        cutTimeStart = timeStrIntoTimeDelta(subCut["orderTimeStart"])
        cutTimeEnd = timeStrIntoTimeDelta(subCut["orderTimeEnd"])

        if checkIsInDiapasone([possibleTimeTaskStart[0], possibleTimeTaskStart[1]], [cutTimeStart, cutTimeEnd]):
            isAbleToOrder = False

    if isAbleToOrder:
        possibleCuts.append({"orderTimeStart":timeDeltaIntoHumanize(possibleTimeTaskStart[0]),
                             "orderTimeEnd":timeDeltaIntoHumanize(possibleTimeTaskStart[1])})