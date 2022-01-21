import random
from datetime import date


def get_nums():
    rand_int = random.randint(0, 9)
    return f"XXX-{rand_int}"


def get_day_name():
    return date.today().strftime('%a')


def get_nums_day_name():
    first = get_nums()
    second = get_day_name().upper()
    return f"{first}-{second}"
