import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chatBot_learing_rate(year=0, month=0):
    try:
        plot_data = {}
        # Getting date
        now = dt.datetime.now()
        if(year == 0):
            year = now.year
        if(month == 0):
            month = now.month
        days_in_month = monthrange(year, month)[1]
        # Create plot data
        for i in range(1, days_in_month+1):
            try:
                temp_users = data[str(year)][str(month)][str(i)]
                asked = 0
                answered = 0
                for temp_user in temp_users:
                    for temp_line in temp_user['lines']:
                        asked += 1
                        if temp_line['tag'] != 'default':
                            answered += 1
                percentage = 100 * float(answered)/float(asked)
                plot_data.setdefault(i, percentage)
            except KeyError:
                plot_data.setdefault(i, 0)

        days_in_month_list = list(plot_data.keys())
        percentage_answered = list(plot_data.values())

        title = 'Learning rate of the chatbot'
        x_label = 'Days'
        y_label = 'Correct answers in procentage'
        x_max = days_in_month
        y_max = 100
        create_graph(
            title,
            x_label,
            y_label,
            x_max,
            y_max,
            days_in_month_list,
            percentage_answered
        )
    except KeyError:
        traceback.print_exc()


def create_graph(title, x_label, y_label, x_max, y_max, x_list, y_list):
    # Creates title
    plt.title(title, fontsize=12)
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
    # plt.show()
    plt.savefig('Figure_Knowledge.png')
    plt.close()
