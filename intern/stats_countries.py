import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange
import collections
import operator

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chatBot_countries():
    try:
        plot_data = {}
        # Getting date
        now = dt.datetime.now()
        this_year = now.year
        this_month = now.month
        days_in_month = monthrange(this_year, this_month)[1]
        # Create plot data
        for i in range(1, days_in_month+1):
            try:
                temp_users = data[str(this_year)][str(this_month)][str(i)]
                for temp_user in temp_users:
                    country = temp_user['user']['country']
                    value = plot_data.setdefault(country, 0)
                    plot_data.update({country: (value + 1)})
            except KeyError:
                pass


        sorted_data_list = sorted(plot_data.items(), key=operator.itemgetter(1), reverse=True)
        sorted_data = collections.OrderedDict(sorted_data_list)
        filtered_data = {}
        for key in sorted_data.keys():
            if len(filtered_data) < 10 and key != None:
                filtered_data.update({key: sorted_data.get(key)})
        common_countries = list(filtered_data.keys())
        amounts_of_users = list(filtered_data.values())

        title = 'Most common countries using the chatbot'
        subtitle = 'Top 10'
        x_label = 'Countries'
        y_label = 'Amounts of users'
        x_max = len(common_countries)
        y_max = max(amounts_of_users) + 5
        create_graph(
            title,
            subtitle,
            x_label,
            y_label,
            x_max,
            y_max,
            common_countries,
            amounts_of_users
        )
    except KeyError:
        traceback.print_exc()


def create_graph(title, subtitle, x_label, y_label, x_max, y_max, x_list, y_list):
    # Creates title and subtitle
    plt.title(title, fontsize=12)
    plt.suptitle(subtitle, fontsize=10)
    # Creates grid
    plt.grid(color='g', linestyle='--', linewidth='0.2')
    # Creates axis
    plt.axis([-1, x_max, 0, y_max])
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks(np.arange(x_max+1, step=1))
    plt.yticks(np.arange(y_max+1, step=5))
    # Creates bars
    plt.bar(x_list, y_list, width=0.5, align='center',
            color='#8cff8c', label='Amount')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chatBot_countries()
