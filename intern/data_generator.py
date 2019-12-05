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
MONTHS = [10, 11, 12]

NAMES = ['Jesper', 'Michael', 'Mads', 'Magnus', 'Rasmus', 'Mathias',
         'Esben', 'Kim', 'Bjarne', 'Casper', 'Dennis', 'Daniel']

ADDITIONAL_PERSONS_PER_DAY = 9
MIN_PERSONS_PER_DAY = 4

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
    try:
        lines = []
        for i in range(count):
            lines.append(
                {
                    'user_msg': 'This is just test data!',
                    'tag': c(TAGS)
                }
            )
        return lines
    except TypeError:
        return "Wrong input"


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
    data = {
        "user": {
            "name": name,
            "ip": ip,
            "country": country,
            "fileno": fileno
        },
        "start": start,
        "end": end,
        "rating": rating,
        "lines": lines
    }
    return data


def generate_data(persons_per_day_min=1, additional_persons_per_day=3):
    start_time = dt.datetime.now()
    data = {}
    for year in YEARS:
        if year not in data.keys():
            data[year] = {}
        for month in MONTHS:
            if month not in data[year].keys():
                data[year][month] = {}
            for day in range(1, mr(year, month)[1]+1):
                if day not in data[year][month].keys():
                    data[year][month][day] = []
                    persons_per_day_max = r(
                        persons_per_day_min, persons_per_day_min + additional_persons_per_day)
                for i in range(persons_per_day_max):
                    print('{}/{}/{}-{}'.format(year, month, day, i))
                    single_data = generate_single_data(year, month, day)
                    data[year][month][day].append(single_data)

    with open('data_test.json', 'w') as outfile:
        json.dump(data, outfile)

    end_time = dt.datetime.now()
    elapsed_time = end_time - start_time
    print('Elapsed time (min, sec): {}'.format(
        divmod(elapsed_time.days * 86400 + elapsed_time.seconds, 60)))


#generate_data(MIN_PERSONS_PER_DAY, ADDITIONAL_PERSONS_PER_DAY)
