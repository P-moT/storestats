from flask import redirect
from datetime import timedelta, date

def fiscalday(data):
    currentdate = date(data["year"], data['month'], data['day'])
    year = currentdate.year
    lastDay = date(year, 12, 31)
    dayOfWeek = lastDay.weekday()
    daysToSubtract = (dayOfWeek - 5) % 7
    lastFiscalDay = (lastDay - timedelta(days=daysToSubtract))
    prevYear = year - 1
    lastDay = date(prevYear, 12, 31)
    dayOfWeek = lastDay.weekday()
    daysToSubtract = (dayOfWeek - 5) % 7
    lastFiscalDayPrevYear = (lastDay - timedelta(days=daysToSubtract))
    print(lastFiscalDay, lastFiscalDayPrevYear)
    length = lastFiscalDay - lastFiscalDayPrevYear
    currentFiscalDay = length.days - ((lastFiscalDay - currentdate).days)
    print(currentFiscalDay)

