import json
import sys


def load_data():
    with open('bars.json', 'r', encoding='UTF-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data_bars):
    biggest_bar = max(data_bars['features'], key=lambda seats: seats['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(data_bars):
    smallest_bar = min(data_bars['features'], key=lambda seats: seats['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(data_bars, longitude, latitude):
    gps = [float(longitude), float(latitude)]
    closest_bar = min(data_bars['features'], key=lambda coord: (gps[0]-coord['geometry']['coordinates'][0])**2 +
                                                               (gps[1]-coord['geometry']['coordinates'][1])**2)
    return closest_bar


def pprint_bar(bar_dict):
    print(bar_dict['properties']['Attributes']['Name'])


if __name__ == '__main__':
    data = load_data()
    print('Самый большой:')
    pprint_bar(get_biggest_bar(data))
    print('Самый маленький:')
    pprint_bar(get_smallest_bar(data))
    print('Самый близкий:')
    pprint_bar(get_closest_bar(data, sys.argv[1], sys.argv[2]))
