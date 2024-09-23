from datetime import datetime,timedelta

from findTimeCut import findTimeCut
from timeDeltaIntoHumanize import timeDeltaIntoHumanize
from TimeStrIntoTimeDelta import timeStrIntoTimeDelta


# Таски

# 1. У каждого уборщика есть выходные это будет массив в котором будет 1 или 3 элемента

FreeDays = ["monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# 1.1 Соответственно такой клинер не сможет получить заказ на свой выходной (Соответственно функция так же будет принимать в себя нужные данные dayOfOrder)

# 2. Оптимизировать сам алгоритм поиска, тут есть некоторые моменты, к примеру не нужно продолжать собирать timeLines если есть хотя бы один клинер
# в cleanerThatCanClean[] и нужно будет уже проверять ТОЛЬКО на совпадение или несовпадение границ 

# 3. Обновить mock-данные соответственно добавить каждому юзеру рандомные выходные 

# 4. Псевдо поиск помогает в 70-80% случаях найти нужные тайминги для заказа, но бывает такое, что тайминги складываются очень неудачно, и для этого нужно сделать реальный поиск
# Этот поиск должен сохранить DurationOfWork + 1 hr и пройти ВСЕ свободные таймланы работника в которые помещяются DurationOfWork + 1 hr, и если находит 5 шт то возвращает преждевременно этот массив
# Если не находит вообще, то возвращает False (Сделай это отдельным алгоритмом т.к это будет вызываться со стороны клиента)



cleaners = [ #mockData - Можешь изменять в целом
    {
        "ID":"1",
        "orders": [
            {
                "id":1,
                "timeStart": "09:00",
                "possibleStartNew": "13:00" # possibleStartNew - это timeStart + durationOfWork + 1 hour
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


# Эта функция нужна для нахождения из множества уборщиков - свободных на именно определенное время
# Если нет свободных уборщиков - тогда этот алгоритм ищет ПСЕВДО ближайшее свободное время к запросу
def canOrderOnThisTime(cleaners, timeStartCleaningObject, timeEndCleaningObject,approximateCleanTime): 
    if timeEndCleaningObject > timeStartCleaningObject: # Проверяет время конца больше за время начала т.е 16:10 > 14:20 к примеру
        cleanerThatCanClean = [] # Здесь собираются уборщики, которые могут выйти работать на это время
        globalTimes = [] # Здесь собираются отрезки работы уборщиков (У которых уже есть заказы)

        for cleaner in cleaners: # Перебор массива уборщиков
            localTimes = [] # Создаётся массив, который собирает инфу именно ОПРЕДЕЛЕННОГО уборщика
            isPossibleToBookThisCleaner = True # По дефолту он может принять заказ

            for order in cleaner["orders"]:
                if len(cleaner["orders"]) < 3: # Заказы могут принимать уборщики у которых 0-1-2 заказа
                    orderTimeStart = timeStrIntoTimeDelta(order["timeStart"]) # Время модифицруется в нужный объект который можно сравнивать < = >
                    orderTimeEnd = timeStrIntoTimeDelta(order["possibleStartNew"]) # Время модифицруется в нужный объект который можно сравнивать < = >

                    orderTimings = {"orderTimeStart": order['timeStart'], "orderTimeEnd": order['possibleStartNew']} # сохраняются тайминги заказа
                    localTimes.append(orderTimings) # Добавляется время одного из заказов (В будущем это нужно для поиска ближайшего свободного времени)

                    if (orderTimeStart < timeEndCleaningObject and timeStartCleaningObject < orderTimeEnd): # Если один из его предыдущих заказов пересекается с новым - тогда этот уборщик не может принять заказ
                        isPossibleToBookThisCleaner = False # Соответственно - false
                else:
                    isPossibleToBookThisCleaner = False  # Если у уборщика >= 3 заказов, он не может принять заказ, соответственно = False

            if isPossibleToBookThisCleaner: # Если после цикла переменная всё ещё True значит этот уборщик может принять заказ
                cleanerThatCanClean.append(cleaner["ID"]) # Добавление ID нужного клинера
            globalTimes.append(localTimes) # Добавление времена заказа клинера в глобальные TimeCuts (Каждый массив отвечает за опредленного клинера)

        if len(cleanerThatCanClean) > 0: # Если есть хоть один клинер который может принять заказ он возвращается
            return cleanerThatCanClean
        else: # Иначе находятся timeCuts которые показывают на какое время можно заказать уборку
            result = findTimeCut(globalTimes, approximateCleanTime)
            return result
    else:
        print("Time-end cannot be less than time-start")
        return False

if __name__ == "__main__":

    timeStart = timedelta(hours=14,minutes=0) # Инициализация время начала уборки
    approximateTimeWork = timedelta(hours=6) # Инициализация предположительной длительности уборки
    approximateTimeEnd = timeStart+approximateTimeWork # Инициализация предположительного конца работы

    result = canOrderOnThisTime(cleaners, timeStart, approximateTimeEnd,approximateTimeWork)

    print(result)

