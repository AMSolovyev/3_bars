import csv
import json
from math import hypot
import os
import sys

DEFAULT_FILE_NAME = 'bars.json'
DEFAULT_FILE_ENCODING = 'utf-8'


def load_data_from_json(filepath, file_encoding):
        with open(filepath, 'r', encoding=file_encoding) as file_handler:
            return json.load(file_handler)


def load_from_csv(filepath):
        with open(filepath, 'r') as file_handler:
            return list(csv.reader(file_handler))


def get_biggest_bar(content_json):
    biggest_bar = max(content_json, key=lambda x: x['SeatsCount'])
    return biggest_bar


def get_smallest_bar(content_json):
    smallest_bar = min(content_json, key=lambda x: x['SeatsCount'])
    return smallest_bar


def get_closest_bar(content_json, latitude, longitude):
    closest_bar = min(content_json, key=lambda x: hypot(float(x['longitude_WGS84']) -
                      longitude, float(x['latitude_WGS84']) - latitude))
    return closest_bar

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска! '
              'Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))
            work_file = sys.argv[1]

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)

    data_from_json = load_data_from_json(work_file, DEFAULT_FILE_ENCODING)

biggest_bar = get_biggest_bar(data_from_json)
print('The biggest bar: {}'.format(biggest_bar['Name']))

smallest_bar = get_smallest_bar(data_from_json)
print('The smallest bar: {}'.format(smallest_bar['Name']))

longitude = float(input('Input coordinate longitude:'))
latitude = float(input('Input coordinate latitude:'))
closest_bar = get_closest_bar(data_from_json, Longitude, Latitude)

print('The closest bar is  ')
print(closest_bar)
