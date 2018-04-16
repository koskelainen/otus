import datetime
from ..constants.consts import RU_MONTH, PREVIOUS_DAYS
import logging

logging.getLogger(__name__)


def get_time(time_str):
    hours, minutes = time_str.split(":")
    return int(hours), int(minutes)


def get_mouth(ru_name_month):
    ru_name_month = ru_name_month.replace(" ", "")
    for ru_name, num_month in RU_MONTH.items():
        if ru_name == ru_name_month:
            return num_month


def get_date(date_str):
    for day_name, delay in PREVIOUS_DAYS.items():
        if date_str == day_name:
            return [datetime.date.today().day - delay,
                    datetime.date.today().month,
                    datetime.date.today().year]
    return [None]*3


def parse_date(date_list):
    minutes = None
    hours = None
    day = None
    month = None
    year = None
    if isinstance(date_list, list):
        current_date = date_list[0]
        if isinstance(current_date, str):
            hours, minutes = get_time(current_date[-5:])
            date = current_date[:(len(current_date) - 8)]
            if (date[:2].replace(" ", "")).isdigit():
                day = int(date[:2])
                if len(date) >= 4 and date[-4:].isdigit():
                    month = get_mouth(date[3:len(date) - 5])
                    year = int(date[-4:])
                else:
                    month = get_mouth(date[3:])
                    year = datetime.datetime.today().year
            else:
                day, month, year = get_date(date)

        if day and month and year and hours is not None and minutes is not None:
            return datetime.datetime(year, month, day, hours, minutes)