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
            # Getting year
            this_year = dt.datetime.now().year
            months_in_year = 12
            # Create plot data
            for month in range(1, months_in_year+1):
                asked = 0
                answered = 0
                for day in range(1, monthrange(this_year, month)[1]+1):
                    try:
                        temp_list = data.LINES[this_year][month][day]
                        asked += temp_list['asked']
                        answered += temp_list['answered']
                    except KeyError:
                        pass
                percentage = 100 * float(answered) / \
                    float(asked) if asked > 0 else 0
                plot_data.setdefault(month, percentage)
        else:
            # Getting date
            now = dt.datetime.now()
            this_year = now.year
            last_month = now.month - 1
            days_in_month = monthrange(this_year, last_month)[1]
            # Create plot data
            for i in range(1, days_in_month+1):
                try:
                    temp_list = data.LINES[this_year][last_month][i]
                    asked = temp_list['asked']
                    answered = temp_list['answered']
                    percentage = 100 * float(answered)/float(asked)
                    plot_data.setdefault(i, percentage)
                except KeyError:
                    plot_data.setdefault(i, 0)

        days_in_month_list = list(plot_data.keys())
        percentage_answered = list(plot_data.values())

        title = 'Learning rate of the chatbot'
        subtitle = 'This Year' if isYear else 'Past Month'
        x_label = 'Months' if isYear else 'Days'
        y_label = 'Correct answers in procentage'
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
    plt.bar(x_list, y_list, width=0.5, align='center', color='#8cff8c', label='Answered questions in %')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chatBot_learing_rate(False)
chatBot_learing_rate()
