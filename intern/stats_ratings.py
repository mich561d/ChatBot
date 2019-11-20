import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange


def chatBot_ratings():
    try:
        plot_data = {}
        # Getting date
        now = dt.datetime.now()
        this_year = now.year
        this_month = now.month
        days_in_month = monthrange(this_year, this_month)[1]
        # Create plot data
        highest_rating = 0
        for i in range(1, days_in_month+1):
            try:
                temp_list = data.RATINGS[this_year][this_month][i]
                bad = temp_list[1]
                poor = temp_list[2]
                decent = temp_list[3]
                good = temp_list[4]
                best = temp_list[5]
                highest_rating = bad if bad > highest_rating else highest_rating
                highest_rating = poor if poor > highest_rating else highest_rating
                highest_rating = decent if decent > highest_rating else highest_rating
                highest_rating = good if good > highest_rating else highest_rating
                highest_rating = best if best > highest_rating else highest_rating
                plot_data.setdefault(i, [bad, poor, decent, good, best])
            except KeyError:
                plot_data.setdefault(i, [0, 0, 0, 0, 0])

        days_in_month_list = list(plot_data.keys())
        ratings = list(plot_data.values())

        list_of_bad_ratings = list(plot_data.values())
        list_of_poor_ratings = list(plot_data.values())
        list_of_decent_ratings = list(plot_data.values())
        list_of_good_ratings = list(plot_data.values())
        list_of_best_ratings = list(plot_data.values())
        temp_counter = 0
        for temp_ratings in ratings:
            list_of_bad_ratings[temp_counter] = temp_ratings[0]
            list_of_poor_ratings[temp_counter] = temp_ratings[1]
            list_of_decent_ratings[temp_counter] = temp_ratings[2]
            list_of_good_ratings[temp_counter] = temp_ratings[3]
            list_of_best_ratings[temp_counter] = temp_ratings[4]
            temp_counter += 1

        title = 'Ratings of the chatbot'
        subtitle = 'This Month'
        x_label = 'Days'
        y_label = 'Count of ratings'
        x_max = days_in_month
        y_max = highest_rating + 10
        create_graph(
            title,
            subtitle,
            x_label,
            y_label,
            x_max,
            y_max,
            days_in_month_list,
            list_of_bad_ratings,
            list_of_poor_ratings,
            list_of_decent_ratings,
            list_of_good_ratings,
            list_of_best_ratings
        )
    except KeyError:
        traceback.print_exc()


def create_graph(title, subtitle, x_label, y_label, x_max, y_max, x_list, y_list_bad, y_list_poor, y_list_decent, y_list_good, y_list_best):
    barWidth = 0.15
    # Creates title and subtitle
    plt.title(title, fontsize=12)
    plt.suptitle(subtitle, fontsize=10)
    # Creates grid
    plt.grid(color='g', linestyle='--', linewidth='0.2')
    # Creates axis
    plt.axis([-1, x_max+1, 0, y_max])
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks([r for r in range(len(x_list))],np.arange(1, x_max+1, step=1))
    plt.yticks(np.arange(y_max+1, step=5))
    # Set position of bar on X axis
    r3 = np.arange(len(x_list))
    r2 = [x - barWidth for x in r3]
    r1 = [x - barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]
    # Make the plot
    plt.bar(r5, y_list_best, width=barWidth, align='center', color='#9feb34', label='Best')
    plt.bar(r4, y_list_good, width=barWidth, align='center', color='#34ebeb', label='Good')
    plt.bar(r3, y_list_decent, width=barWidth, align='center', color='#ebe534', label='Decent')
    plt.bar(r2, y_list_poor, width=barWidth, align='center', color='#eb9334', label='Poor')
    plt.bar(r1, y_list_bad, width=barWidth, align='center', color='#eb4034', label='Bad')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chatBot_ratings()
