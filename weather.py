#!/usr/bin/env python

import os
import requests
import json
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class WeatherChecker(object):
    _WUNDERGROUND_API_KEY = os.environ['WUNDERGROUND_API_KEY'],
    _WUNDERGROUND_STATE = os.environ['WUNDERGROUND_STATE'],
    _WUNDERGROUND_CITY = os.environ['WUNDERGROUND_CITY'],
    _WUNDERGROUND_ENDPOINT_TEMPLATE = 'http://api.wunderground.com/api/{}/hourly/q/{}/{}.json'

    def __init__(self):
        self._api_key = ''.join(self._WUNDERGROUND_API_KEY)
        self._state = ''.join(self._WUNDERGROUND_STATE)
        self._city = ''.join(self._WUNDERGROUND_CITY)


    def get_rain_probability(self):
        url = self._WUNDERGROUND_ENDPOINT_TEMPLATE.format(self._api_key, self._state, self._city)
        print url
        response = requests.get(url)
        return response


if __name__ == '__main__':
    weather_checker = WeatherChecker()
    rain_probability = weather_checker.get_rain_probability()

    print rain_probability.text
    if rain_probability > 0.05:
        logger.info('Rain probability: {}'.format(rain_probability))

