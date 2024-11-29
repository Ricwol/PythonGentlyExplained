"""Exercise #21: Validate Date

Write an `isValidDate()` function with parameters `year`, `month`, 
and `day`. The function should return `True` if the integers provided
for these parameters represent a valid date. Otherwise, the function
returns `False`. Months are represented by the integers `1` (for January)
to `12` (for December) and days are represented by integers `1` up to `28`,
`29`, `30`, or `31` depending on the month and year. 

Your solution should import your leapyear.py program from Exercise #20 for
its `isLeapYear()` function, as February 29th is a valid date on leap years.

September, April, June, and November have 30 days. The rest have 31, except
February which has 28 days. On leap years, February has 29 days.
"""

from .leap_year import isLeapYear


def isValidDate(year: int, month: int, day: int) -> bool:
    """Return True if date is valid. False otherwise."""
    return False
