from random import randint as r
from random import choice as c
import requests
from requests.exceptions import HTTPError
from key import key
import datetime as dt
from datetime import timedelta as td
from calendar import monthrange as mr
import json

YEARS = [2019]
MONTHS = [10, 11]

NAMES = ['Jesper', 'Michael', 'Mads', 'Magnus', 'Rasmus', 'Mathias',
         'Esben', 'Kim', 'Bjarne', 'Casper', 'Dennis', 'Daniel']

MAX_USERS_PER_DAY = 7
MIN_USERS_PER_DAY = 1

TAGS = ['greeting', 'goodbye', 'name', 'hours', 'contact', 'thanks', 'default']


def ip_generator():
    first = r(1, 255)
    second = r(0, 255)
    third = r(0, 255)
    fourth = r(1, 255)
    return '{}.{}.{}.{}'.format(first, second, third, fourth)


def get_country_from_ip(ip):
    try:
        url = 'http://api.ipstack.com/{}?access_key={}'.format(ip, key)
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        json = response.json()
        return json['country_name']
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success: {}'.format(ip))
    return 'Err'


def generate_lines(count):
    lines = []
    for i in range(count):
        lines.append(
            {
                'user_msg': 'This is just test data!',
                'tag': c(TAGS)
            }
        )
    return lines


def generate_single_data(year, month, day):
    name = c(NAMES)
    ip = ip_generator()
    country = get_country_from_ip(ip)
    fileno = r(500, 800)
    date = dt.datetime(year, month, day, r(0, 23), r(0, 59), r(0, 59))
    start = date.strftime('%d/%m/%Y %H:%M:%S')
    end = (date + td(seconds=r(45, 500))).strftime('%d/%m/%Y %H:%M:%S')
    rating = r(1, 5)
    lines = generate_lines(r(1, 10))
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        name, ip, country, fileno, start, end, rating, lines)) # TODO: Don't print, buuuut create Objec'tós! PLEASE!


def generate_data(persons_per_day_max=1):
    data = {}
    for year in YEARS:
        if year not in data.keys():
            data[year] = {}
        print(year)
        for month in MONTHS:
            if month not in data[year].keys():
                data[year][month] = {}
            print(month)
            for day in range(1, mr(year, month)[1]+1):
                if day not in data[year][month].keys():
                    data[year][month][day] = []
                print(day)
                for i in range(persons_per_day_max):
                    print(i)
                    #generate_single_data(year, month, day) #TODO Added to array

    with open('intern/data_test.json', 'w') as outfile:
        json.dump(data, outfile)


generate_data()
