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

def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar

def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar

def get_closest_bar(data,Latitude,Longitude):
    closest_bar = min(data, key=lambda x: hypot(float(x['Longitude_WGS84']) \
                  - Longitude, float(x['Latitude_WGS84']) - Latitude))
    return closest_bar

if __name__== '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска!  Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
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
print('Самый большой бар: {}'.format(biggest_bar['Name']))

smallest_bar = get_smallest_bar(data_from_json)
print('Самый маленький бар: {}'.format(smallest_bar['Name']))

Longitude = float(input('Введите longitude:'))
Latitude = float(input('Введите latitude:'))
closest_bar = get_closest_bar(data_from_json, Longitude, Latitude)

print('Ближайший объект')
print(closest_bar)