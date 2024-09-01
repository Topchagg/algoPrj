from datetime import datetime,timedelta

from findTimeCut import findTimeCut
from timeDeltaIntoHumanize import timeDeltaIntoHumanize
from TimeStrIntoTimeDelta import timeStrIntoTimeDelta

cleaners = [
    {
        "ID":"1",
        "orders": [
            {
                "id":1,
                "timeStart": "09:00",
                "possibleStartNew": "13:00"
            },
            {
                "id":2,
                "timeStart":"13:45",
                "possibleStartNew":"22:10"
            },
        ]
    },
    {
        "ID":"2",
        "orders": [
            {
                "id":4,
                "timeStart":"14:00",
                "possibleStartNew":"22:30"
            }
        ]
    },
    {
        "ID":"3",
        "orders": [
            {
                "id":5,
                "timeStart":"07:30",
                "possibleStartNew":"22:10"
            }
        ]
    },
]



def canOrderOnThisTime(cleaners, timeStartCleaningObject, timeEndCleaningObject,approximateCleanTime):
    if timeEndCleaningObject > timeStartCleaningObject:
        cleanerThatCanClean = []
        globalTimes = []

        for cleaner in cleaners:
            localTimes = []
            isPossibleToBookThisCleaner = True

            for order in cleaner["orders"]:
                if len(cleaner["orders"]) < 3:
                    orderTimeStart = timeStrIntoTimeDelta(order["timeStart"])
                    orderTimeEnd = timeStrIntoTimeDelta(order["possibleStartNew"])

                    orderTimings = {"orderTimeStart": order['timeStart'], "orderTimeEnd": order['possibleStartNew']}
                    localTimes.append(orderTimings)

                    if (orderTimeStart < timeEndCleaningObject and timeStartCleaningObject < orderTimeEnd):
                        isPossibleToBookThisCleaner = False

            if isPossibleToBookThisCleaner:
                cleanerThatCanClean.append(cleaner["ID"])
            globalTimes.append(localTimes)

        if len(cleanerThatCanClean) > 0:
            return cleanerThatCanClean
        else:
            result = findTimeCut(globalTimes, approximateCleanTime)
            return result
    else:
        print("Time-end cannot be less than time-start")
        return False

if __name__ == "__main__":

    timeStart = timedelta(hours=7,minutes=0)
    approximateTimeWork = timedelta(hours=6)
    approximateTimeEnd = timeStart+approximateTimeWork

    result = canOrderOnThisTime(cleaners, timeStart, approximateTimeEnd,approximateTimeWork)

    print(result)

    # Проверить оставшиеся исключения
    # Есть небольшая недоработка с границами, нужно брать +1 час к timeEnd