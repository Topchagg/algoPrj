from datetime import timedelta


def timeStrIntoTimeDelta(timeStr):
    hrs,mints = map(int,timeStr.split(":"))
    valueToReturn = timedelta(hours=hrs,minutes=mints)

    return valueToReturn