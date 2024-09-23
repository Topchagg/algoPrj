from datetime import timedelta


from addCutsToList import *
from TimeStrIntoTimeDelta import *

def findTimeCut(timeLines, approximateCleanTime):
    possibleCuts = [] # Тут сохраняются нужные временные отрезки которые могут одойти заказчику
    possibleEarlest = timedelta(hours=6, minutes=0) # Самый ранний заказ в 6 утра
    possibleLatest = timedelta(hours=22, minutes=0) # Самый поздний до 10 вечера


    # listOfCuts -> Это массив временных отрезков работы клинера
    for listOfCuts in timeLines: 
        for cut in listOfCuts: # cut представляет из себя время начала и конца работы
            operateOrderTimeStart = timeStrIntoTimeDelta(cut["orderTimeStart"]) # Время модифицруется в нужный объект который можно сравнивать < = >


            operateOrderTimeEnd = timeStrIntoTimeDelta(cut["orderTimeEnd"]) # Время модифицруется в нужный объект который можно сравнивать < = >


            # Находит ПСЕВДО ближайшее время путём отступов от границы в лево т.е - и право т.е + 
            possibleEarlestTaskStart = operateOrderTimeStart - approximateCleanTime 
            possibleEarlestTaskEnd = possibleEarlestTaskStart + approximateCleanTime

            possibleLatestTaskStart = operateOrderTimeEnd + timedelta(hours=1)
            possibleLatestTaskEnd = possibleLatestTaskStart + approximateCleanTime

            # Сравнивает диапазоны и если диапазоны подходят то добавляет время, сначала проверяется левая граница потом правая
            if possibleEarlest <= possibleEarlestTaskStart < possibleLatest:
                addCutsToList(listOfCuts, possibleCuts,[possibleEarlestTaskStart, possibleEarlestTaskEnd])

            if possibleEarlest <= possibleLatestTaskStart < possibleLatest:
                addCutsToList(listOfCuts, possibleCuts,[possibleLatestTaskStart, possibleLatestTaskEnd])

    return possibleCuts

