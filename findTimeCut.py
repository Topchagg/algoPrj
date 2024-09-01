from datetime import timedelta


from addCutsToList import *
from TimeStrIntoTimeDelta import *

def findTimeCut(timeLines, approximateCleanTime):
    possibleCuts = []
    possibleEarlest = timedelta(hours=6, minutes=0)
    possibleLatest = timedelta(hours=22, minutes=0)

    approximateCleanTimeObject = timeStrIntoTimeDelta(approximateCleanTime)

    for listOfCuts in timeLines:
        for cut in listOfCuts:
            operateOrderTimeStart = timeStrIntoTimeDelta(cut["orderTimeStart"])


            operateOrderTimeEnd = timeStrIntoTimeDelta(cut["orderTimeEnd"])

            possibleEarlestTaskStart = operateOrderTimeStart - approximateCleanTimeObject
            possibleEarlestTaskEnd = possibleEarlestTaskStart + approximateCleanTimeObject

            possibleLatestTaskStart = operateOrderTimeEnd + timedelta(hours=1)
            possibleLatestTaskEnd = possibleLatestTaskStart + approximateCleanTimeObject

            if possibleEarlest <= possibleEarlestTaskStart < possibleLatest:
                addCutsToList(listOfCuts, possibleCuts,[possibleEarlestTaskStart, possibleEarlestTaskEnd])

            if possibleEarlest <= possibleLatestTaskStart < possibleLatest:
                addCutsToList(listOfCuts, possibleCuts,[possibleLatestTaskStart, possibleLatestTaskEnd])

    return possibleCuts

