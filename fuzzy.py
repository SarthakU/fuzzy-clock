import datetime
import random

TENS_DICT = [
    '', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety'
]

ONES_DICT = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

TEENS = [
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen'
]


def n2a(number):
    if number == 0:
        return 'zero'
    elif number < 10:
        return ONES_DICT[number % 10]
    elif number < 20 and number > 9:
        return TEENS[number - 10]
    elif number % 10 == 0:
        return TENS_DICT[number // 10]
    else:
        return TENS_DICT[number // 10] + ' ' + ONES_DICT[number % 10]


def next(n):
    return 12 if n == 11 else n + 1


def fuzzyTime(hour, minutes):
    cond = ((minutes + 2) % 60) // 5
    hour = hour % 12
    if minutes > 33:
        hour = next(hour)
    print(cond)
    if cond == 0:
        return n2a(hour) + ' o\'clock'
    elif cond == 3:
        return 'quarter' + ' past ' + n2a(hour)
    elif cond == 6:
        return 'half' + ' past ' + n2a(hour)
    elif cond == 9:
        return 'quarter' + ' to ' + n2a(hour)
    elif 0 < cond < 6:
        return n2a(cond * 5) + ' past ' + n2a(hour)
    else:
        return n2a(60 - cond * 5) + ' to ' + n2a(hour)


# time = datetime.datetime.now().timetuple()
# hour = time[3]
# minutes = time[4]
# fuzzyTime(hour, minutes)
