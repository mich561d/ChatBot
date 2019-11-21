import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chatBot_learing_rate():
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
                asked = 0
                answered = 0
                for temp_user in temp_users:
                    for temp_line in temp_user['lines']:
                        asked += 1
                        if temp_line['tag'] != 'default':
                            answered += 1
                percentage = 100 * float(answered)/float(asked)
                plot_data.setdefault(i, percentage)
            except KeyError as e:
                plot_data.setdefault(i, 0)

        days_in_month_list = list(plot_data.keys())
        percentage_answered = list(plot_data.values())

        title = 'Learning rate of the chatbot'
        subtitle = 'This Month'
        x_label = 'Days'
        y_label = 'Correct answers in procentage'
        x_max = days_in_month
        y_max = 100
        create_graph(
            title,
            subtitle,
            x_label,
            y_label,
            x_max,
            y_max,
            days_in_month_list,
            percentage_answered
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
    plt.axis([0, x_max+1, 0, y_max])
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks(np.arange(1, x_max+1, step=1))
    plt.yticks(np.arange(y_max+1, step=5))
    # Creates bars
    plt.bar(x_list, y_list, width=0.5, align='center',
            color='#8cff8c', label='Answered questions in %')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chatBot_learing_rate()
