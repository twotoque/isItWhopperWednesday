# whopperWednesday

Zero dependencies. Tells you whether it's Whopper Wednesday.

```bash
pip install whopperWednesday
```

```python
from datetime import date
from whopperWednesday import isItWhopperWednesday

isItWhopperWednesday()                       # True on Wednesdays, else False
isItWhopperWednesday(country="CA")           # US, UK and Canada supported
isItWhopperWednesday(date(2026, 11, 25), "UK")  # True
isItWhopperWednesday(country="France")       # False (no Whopper Wednesday)
```

Country codes are case-insensitive and accept aliases (`USA`, `GB`, `Canada`, ...).
The day is checked using your computer's local date.
