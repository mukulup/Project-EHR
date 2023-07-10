"""
In this file we are following the date conventions like as follows:
    for ex:  Start Date (YYYY-MM-DD HH:MM:SS): 2016-03-1 00:00:00
             End Date (YYYY-MM-DD HH:MM:SS): 2016-03-15 23:59:59
End date need to follow the convention of 23:59:59 as hours, minutes and seconds convention to it.
"""
import calendar
from datetime import timedelta
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
from dateutil.tz import gettz
from django.utils import timezone


def now_local(only_date=False):
    """
    In this method takes only date is true or false. If true means return the date with time (2016-03-15 13:09:08).
    If false means return the date (2016-03-15)
    :param only_date: true / false
    :return: date with time (2016-03-15 13:09:08) and date (2016-03-15)
    """
    if only_date:
        return (timezone.localtime(timezone.now())).date()
    else:
        return timezone.localtime(timezone.now())