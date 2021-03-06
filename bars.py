import json
from math import sqrt
import os
import sys


def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            decoded_json = json.load(json_file)
            bars = decoded_json['features']
            return bars
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
    closest_bar = min(
        bars, key=lambda bar: (
                (bar['geometry']['coordinates'][0] - latitude)**2 -
                (bar['geometry']['coordinates'][1] - longitude)**2))

    return closest_bar


def get_coordinates():
    try:
        latitude = float(input('Input coordinate latitude:'))
        longitude = float(input('Input coordinate longitude:'))
        return longitude, latitude
    except ValueError:
        return None


def print_bars(bar_results, msg):
    print(
        msg.format(
            bar_results['properties']['Attributes']['Name']))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('You do not input the path to the file')
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('There is not any file like this')

    bars = load_data_from_json(file_path)
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    latitude, longitude = get_coordinates()
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print_bars(biggest_bar,'The biggest bar: {}')
    print_bars(smallest_bar, 'The smallest bar: {}')
    print_bars(closest_bar, 'The closest bar: {}')
