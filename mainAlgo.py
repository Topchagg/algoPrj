from datetime import datetime,timedelta

from findTimeCut import findTimeCut
from timeDeltaIntoHumanize import timeDeltaIntoHumanize

cleaners = [
    {
        "ID":"1",
        "orders": [
            {
                "id":2,
                "timeStart":"13:45",
                "possibleStartNew":"22:10"
            },
             {
                "id":1,
                "timeStart": "09:00",
                "possibleStartNew": "13:00"
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



def canOrderOnThisTime(cleaners, startCleaningTime, endCleaningTime,approximateCleanTime):
    timeStartCleaningObject = datetime.strptime(startCleaningTime, "%H:%M").time()
    timeEndCleaningObject = datetime.strptime(endCleaningTime, "%H:%M").time()

    if timeEndCleaningObject > timeStartCleaningObject:
        cleanerThatCanClean = []
        globalTimes = []

        for cleaner in cleaners:
            localTimes = []
            isPossibleToBookThisCleaner = True

            for order in cleaner["orders"]:
                if len(cleaner["orders"]) < 3:
                    orderTimeStart = datetime.strptime(order['timeStart'], "%H:%M").time()
                    orderTimeEnd = datetime.strptime(order['possibleStartNew'], "%H:%M").time()

                    orderTimings = {"orderTimeStart": order['timeStart'], "orderTimeEnd": order['possibleStartNew']}
                    localTimes.append(orderTimings)

                    if (timeStartCleaningObject > orderTimeStart and timeStartCleaningObject < orderTimeEnd or
                        timeEndCleaningObject > orderTimeStart and timeEndCleaningObject < orderTimeEnd):

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

    timeStart = timedelta(hours=10,minutes=0)
    approximateTimeWork = timedelta(hours=4)
    approximateTimeEnd = timeStart+approximateTimeWork


    humanizeTimeStart = timeDeltaIntoHumanize(timeStart)
    humanizeTimeWork = timeDeltaIntoHumanize(approximateTimeWork)
    humanizeTimeEnd = timeDeltaIntoHumanize(approximateTimeEnd)

    result = canOrderOnThisTime(cleaners, humanizeTimeStart, humanizeTimeEnd,humanizeTimeWork)

    print(result)

    # Переписать функцию timeDeltaIntoHumanize 
    # Проверить оставшиеся исключения