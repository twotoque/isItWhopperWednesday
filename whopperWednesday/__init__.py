from datetime import date

__version__ = "0.2.0"
__all__ = ["isItWhopperWednesday", "COUNTRIES"]

# Countries with Whopper Wednesday
COUNTRIES = {
    "US": "US", "USA": "US", "UNITED STATES": "US",
    "UK": "UK", "GB": "UK", "UNITED KINGDOM": "UK",
    "CA": "CA", "CAN": "CA", "CANADA": "CA",
}


def isItWhopperWednesday(day=None, country=None):
    '''
    Evaluates if it is Whopper Wednesday.

    Inputs:
        day -- a datetime.date (default today)
        country -- "US", "UK" or "CA" (default None)

    Outputs:
        True -- it is Whopper Wednesday
        False -- it is not Whopper Wednesday
    '''
    if day is None:
        day = date.today()
    if country is not None and country.strip().upper() not in COUNTRIES:
        return False
    if day.weekday() == 2:
        return True
    else:
        return False