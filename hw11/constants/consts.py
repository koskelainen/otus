#!/usr/bin/env python
# -*- coding: utf-8 -*-
JSON_SRC_FILE = 'Habr.json'
CSV_FILE = 'Habr.csv'
BASIC_URL = 'https://habrahabr.ru/all/'
URL_PATTERN = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s|(?!"<>)]{2,}\/|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}\/|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]|(?!"<>)]{2,}\/|www\.[a-zA-Z0-9]\.[^\s|(?!"<>)]]{2,}\/)'
URL_POSTS_PATTERN = 'https?:\/\/habrahabr.ru\/post\/(\d{2,})\/'

ALLOWED_DOMAINS = ['habrahabr.ru']
START_URLS = [('https://habrahabr.ru/all/' + top + post)
                    for top in ['top100/', 'top50/', 'top25/', 'top10/']
                    for post in [''] + ['page' + str(num) for num in range(2, 100)]]

ALLOWED_PATTERNS = ('/post/(\d{2,})/?$',)

RU_MONTH = {'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12
            }

PREVIOUS_DAYS = {
    'сегодня': 0,
    'вчера': 1
}


