import matplotlib.pyplot as plt
import numpy as np
import traceback
import data_activity as data
import datetime as dt


def chat_session_count(year=0, month=0):
    # Get year and month
    now = dt.datetime.now()
    year = year if year != 0 else now.year
    month = month if month != 0 else now.month
    # Create plot data
    plot_data = {}
    for temp_day in data.SESSIONS[year][month]:
        try:
            for temp_hour in data.SESSIONS[year][month][temp_day].keys():
                temp_list = data.SESSIONS[year][month][temp_day][temp_hour]
                plot_data.setdefault(temp_hour, len(temp_list))
        except KeyError:
            pass

    hours_of_the_day = list(plot_data.keys())
    chat_sessions = list(plot_data.values())

    title = 'Amount of chats per hour of the day'
    subtitle = 'Year: {} | Month: {}'.format(year, month)
    x_label = 'Hours of the day'
    y_label = 'Session amount'
    x_max = 24
    y_max = max(chat_sessions) + 2
    create_graph(
        title,
        subtitle,
        x_label,
        y_label,
        x_max,
        y_max,
        hours_of_the_day,
        chat_sessions,
    )


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
    plt.xticks(np.arange(x_max, step=1))
    plt.yticks(np.arange(y_max+1, step=1))
    # Creates bar
    plt.bar(x_list, y_list, width=0.25, align='center',
            color='#8cff8c', label='Amount of chats')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chat_session_count()
chat_session_count(2019, 11)
