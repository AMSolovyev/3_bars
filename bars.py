import json
from math import sqrt
import os
import sys


def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            decoded_json = json.load(json_file)
            json_bars = decoded_json['features']
            return json_bars
    except json.decoder.JSONDecodeError:
        return None


def get_biggest_bar(bars):
    biggest_bar = max(
        bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(
        bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars, longitude, latitude):
    distance = min(
        bars, key=lambda bar: (
                (bar['geometry']['coordinates'][0] - latitude)**2 -
                (bar['geometry']['coordinates'][1] - longitude)**2))

    return distance


def get_coordinates():
    try:
        latitude = float(input('Input coordinate latitude:'))
        longitude = float(input('Input coordinate longitude:'))
        return longitude, latitude
    except ValueError:
        return None


def print_bars():
    bars = load_data_from_json(file_path)
    biggest_bar = get_biggest_bar(bars)
    print(
        'The biggest bar: {}'.format(
            biggest_bar['properties']['Attributes']['Name']))
    smallest_bar = get_smallest_bar(bars)
    print(
        'The smallest bar: {}'.format(
            smallest_bar['properties']['Attributes']['Name']))
    latitude, longitude = get_coordinates()
    closest_bar = get_closest_bar(bars, longitude, latitude)
    print(
        'The closest bar: {}'.format(
            closest_bar['properties']['Attributes']['Name']))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('You do not input the path to the file')
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('There is not any file like this')

    print_bars()
