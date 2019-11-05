import matplotlib.pyplot as plt
import numpy as np
import traceback
import datetime as dt
from calendar import monthrange
import data_lines as data


def chatBot_learing_rate(isYear=True):
    # isYear | True = Year | False = Month | TODO: Refactor into better naming
    try:
        plot_data = {}
        if isYear:
            pass
        else:
            # Getting last month
            now = dt.datetime.now()
            this_year = now.year
            last_month = now.month - 1
            days_in_month = monthrange(this_year, last_month)[1]
            # Create plot data
            for i in range(days_in_month):
                try:
                    temp_list = data.LINES[this_year][last_month][i]
                    asked = 0
                    answered = 0
                    for temp_chat in temp_list:
                        asked += temp_chat['asked']
                        answered += temp_chat['answered']
                    percentage = 100 * float(answered)/float(asked)
                    plot_data.setdefault(i+1, percentage)
                except KeyError:
                    plot_data.setdefault(i+1, 0)

        days_in_month_list = list(plot_data.keys())
        percentage_answered = list(plot_data.values())

        title = 'Learning rate of the chatbot'
        subtitle = 'Past Year' if isYear else 'Past Month'
        x_label = 'Months' if isYear else 'Days'
        y_label = 'Correct answers in procetage'
        x_max = 12 if isYear else days_in_month
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
    plt.bar(x_list, y_list, width=0.5, align='center', color='#8cff8c')
    # Shows plot
    plt.show()


# TODO: Remove
chatBot_learing_rate(False)
chatBot_learing_rate()
