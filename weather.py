#!/usr/bin/env python

import os
import sys
try:
    import requests
except ImportError:
    raise ImportError('You need to install requests: `pip install requests`')
import json
import logging
import datetime
import pprint

logging.basicConfig(format='%(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class WeatherChecker(object):
    _WUNDERGROUND_API_KEY = os.environ['WUNDERGROUND_API_KEY']
    _WUNDERGROUND_STATE = os.environ['WUNDERGROUND_STATE']
    _WUNDERGROUND_CITY = os.environ['WUNDERGROUND_CITY']
    _WUNDERGROUND_ENDPOINT_TEMPLATE = \
        'http://api.wunderground.com/api/{}/hourly/q/{}/{}.json'

    def __init__(self):
        self._api_key = self._WUNDERGROUND_API_KEY
        self._state = self._WUNDERGROUND_STATE
        self._city = self._WUNDERGROUND_CITY

    def _get_today_weekday(self):
        day_initials = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur',
                        'Sun']
        weekday_name = day_initials[datetime.datetime.today().weekday()] + 'day'
        return weekday_name

    def _avg(self, list):
        return sum(list, 0.0) / len(list)

    def get_today_rain_probability_avg(self):
        url = self._WUNDERGROUND_ENDPOINT_TEMPLATE.format(self._api_key,
                self._state, self._city)
        res = requests.get(url)
        json_data = json.loads(res.text)
        today_weekday_name = self._get_today_weekday()
        weekday_data = [obj for obj in json_data['hourly_forecast'] if
                        (obj['FCTTIME']['weekday_name'] == today_weekday_name)]
        # pprint.pprint(weekday_data)
        rain_probabilities = [float(obj['pop']) for obj in weekday_data]

        return self._avg(rain_probabilities)


if __name__ == '__main__':
    weather_checker = WeatherChecker()
    rain_probability = weather_checker.get_today_rain_probability_avg()

    if rain_probability > 5:
        logger.info('Rain probability: {:0.2f} %'.format(rain_probability))

    sys.exit(0)

