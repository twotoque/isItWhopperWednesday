from datetime import date
from whopperWednesday import isItWhopperWednesday

WED = date(2026, 11, 25)
MON = date(2026, 11, 23)

def test_wednesday():
    assert isItWhopperWednesday(WED) is True

def test_not_wednesday():
    assert isItWhopperWednesday(MON) is False

def test_supported_countries():
    for c in ["US", "uk", "Canada", "usa", "GB", " ca "]:
        assert isItWhopperWednesday(WED, c) is True
        assert isItWhopperWednesday(MON, c) is False

def test_unsupported_country():
    assert isItWhopperWednesday(WED, "France") is False

def test_today_returns_bool():
    assert isinstance(isItWhopperWednesday(), bool)
    assert isinstance(isItWhopperWednesday(country="CA"), bool)