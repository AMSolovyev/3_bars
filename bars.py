import json
from math import sqrt
import os
import sys


def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            decoded_json_file = json.load(json_file)
            json_bars = decoded_json_file['features']
            return json_bars
    except json.decoder.JSONDecodeError:
        return None


def get_biggest_bar(json_bars):
    biggest_bar = max(
        json_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(json_bars):
    smallest_bar = min(
        json_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(json_bars, longitude, latitude):
    distance = min(
            json_bars, key=lambda bar: (
                    (bar['geometry']['coordinates'][0] - latitude)**2 -
                    (bar['geometry']['coordinates'][1] - longitude)**2))

    return distance


def enter_coordinate():
    try:
        latitude = float(input('Input coordinate latitude:'))
        longitude = float(input('Input coordinate longitude:'))
        return longitude, latitude
    except ValueError:
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('You do not input the path to the file')
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('There is not any file like this')

    json_bars = load_data_from_json(file_path)

    biggest_bar = get_biggest_bar(json_bars)
    print(
        'The biggest bar: {}'.format(
            biggest_bar['properties']['Attributes']['Name']))

    smallest_bar = get_smallest_bar(json_bars)
    print(
        'The smallest bar: {}'.format(
            smallest_bar['properties']['Attributes']['Name']))

    latitude, longitude = enter_coordinate()

    print(
        'The closest bar: {}'.format(
            get_closest_bar(
                json_bars, latitude,
                longitude)['properties']['Attributes']['Name']))
