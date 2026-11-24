from datetime import date

def isItWhopperWednesday(day=None):
    if day is None:
        day = date.today()
    if day.weekday() == 2: 
        return True
    else:
        return False