import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange

with open('./data_learning.json') as json_file:
    data = json.load(json_file)


def chatBot_learning_time(year=0, month=0):
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
        date_format = '%Y/%m/%d-%H:%M:%S'
        for i in range(1, days_in_month+1):
            try:
                temp_list = data[str(year)][str(month)][str(i)]
                start = dt.datetime.strptime(
                    temp_list['start_time'], date_format)
                end = dt.datetime.strptime(temp_list['end_time'], date_format)
                between = end - start
                minutes = between.total_seconds() / 60
                plot_data.setdefault(i, minutes)
            except KeyError:
                plot_data.setdefault(i, 0)

        days_in_month_list = list(plot_data.keys())
        time_spend = list(plot_data.values())

        title = 'Learning time of the chatbot'
        x_label = 'Days'
        y_label = 'Minutes'
        x_max = days_in_month
        y_max = max(time_spend) + 2
        create_graph(
            title,
            x_label,
            y_label,
            x_max,
            y_max,
            days_in_month_list,
            time_spend
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
    plt.yticks(np.arange(y_max+1, step=1))
    # Creates bars
    plt.bar(x_list, y_list, width=0.5, align='center',
            color='#8cff8c', label='Time')
    # Shows plot
    plt.legend()
    # plt.show()
    plt.savefig('GUI/Figure_Learning.png')
