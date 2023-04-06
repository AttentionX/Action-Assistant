from datetime import datetime

def getDatetime(isString=False):
    currentSecond= datetime.now().second
    currentMinute = datetime.now().minute
    currentHour = datetime.now().hour

    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    if isString:
        currentSecond = str(currentSecond)
        currentMinute = str(currentMinute)
        currentHour = str(currentHour)
        currentDay = str(currentDay)
        currentMonth = str(currentMonth)
        currentYear = str(currentYear)
        
    return [currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSecond]