import csv
import json
from math import hypot
import os
import sys


def load_data_from_json(filepath):
    with open(filepath, 'r') as file_handler:
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


def get_closest_bar(content_json, coordinate_lat, coordinate_long):
    closest_bar = min(
        content_json,
        key=lambda x: hypot(float(x['longitude_WGS84']) -
                            coordinate_long, float(x['latitude_WGS84']) -
                            coordinate_lat))
    return closest_bar


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('You do not input the path to the file')
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('There is not any file like this')

    data_from_json = load_data_from_json(file_path)

    if not os.path.exists(file_path):
        if data_from_json is None:
            exit('There is not any file in json-formate')


biggest_bar = get_biggest_bar(data_from_json)
print('The biggest bar: {}'.format(biggest_bar['Name']))

smallest_bar = get_smallest_bar(data_from_json)
print('The smallest bar: {}'.format(smallest_bar['Name']))

longitude = float(input('Input coordinate longitude:'))
latitude = float(input('Input coordinate latitude:'))
closest_bar = get_closest_bar(data_from_json, coordinate_lat,
                              coordinate_long)

print('The closest bar is  ')
print(closest_bar)
