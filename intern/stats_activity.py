import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chat_session_count(year=0, month=0):
    # Get year and month
    now = dt.datetime.now()
    year = str(year) if year != 0 else str(now.year)
    month = str(month) if month != 0 else str(now.month)
    # Create plot data
    date_format = '%d/%m/%Y %H:%M:%S'
    plot_data = {}
    for temp_day in data[year][month].keys():
        try:
            for temp_user in data[year][month][temp_day]:
                start_time = dt.datetime.strptime(
                    temp_user['start'], date_format)
                temp_hour = start_time.hour
                value = plot_data.setdefault(temp_hour, 0)
                plot_data.update({temp_hour: (value + 1)})
        except KeyError:
            pass

    hours_of_the_day = list(plot_data.keys())
    chat_sessions = list(plot_data.values())

    title = 'Amount of chats per hour of the day'
    x_label = 'Hours of the day'
    y_label = 'Session amount'
    x_max = 24
    y_max = max(chat_sessions) + 2
    create_graph(
        title,
        x_label,
        y_label,
        x_max,
        y_max,
        hours_of_the_day,
        chat_sessions,
    )


def create_graph(title, x_label, y_label, x_max, y_max, x_list, y_list):
    # Creates title
    plt.title(title, fontsize=12)
    # Creates grid
    plt.grid(color='g', linestyle='--', linewidth='0.2')
    # Creates axis
    plt.axis([-1, x_max, 0, y_max])
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks(np.arange(x_max, step=1))
    plt.yticks(np.arange(y_max+1, step=1))
    # Creates bar
    plt.bar(x_list, y_list, width=0.25, align='center',
            color='#8cff8c', label='Amount of chats')
    # Shows plot
    plt.legend()
    # plt.show()
    plt.savefig('Figure_Activity.png')
    plt.close()
