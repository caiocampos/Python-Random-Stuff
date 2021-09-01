from datetime import datetime
from datetime import timedelta

GIGASECOND = timedelta(seconds=1000000000)

def add(moment):
    return moment + GIGASECOND
