import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chatBot_ratings(year=0, month=0):
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
        highest_rating = 0
        for i in range(1, days_in_month+1):
            try:
                temp_list = data[str(year)][str(month)][str(i)]
                bad = 0
                poor = 0
                decent = 0
                good = 0
                best = 0
                for user in temp_list:
                    rating = user['rating']
                    if rating == 1:
                        bad += 1
                    elif rating == 2:
                        poor += 1
                    elif rating == 3:
                        decent += 1
                    elif rating == 4:
                        good += 1
                    else:
                        best += 1
                ratings = [bad, poor, decent, good, best]
                highest_rating = max(ratings) if max(
                    ratings) > highest_rating else highest_rating
                plot_data.setdefault(i, ratings)
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
        x_label = 'Days'
        y_label = 'Count of ratings'
        x_max = days_in_month
        y_max = highest_rating + 1
        create_graph(
            title,
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


def create_graph(title, x_label, y_label, x_max, y_max, x_list, y_list_bad, y_list_poor, y_list_decent, y_list_good, y_list_best):
    barWidth = 0.15
    # Creates title
    plt.title(title, fontsize=12)
    # Creates grid
    plt.grid(color='g', linestyle='--', linewidth='0.2')
    # Creates axis
    plt.axis([-1, x_max+1, 0, y_max])
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks([r for r in range(len(x_list))], np.arange(1, x_max+1, step=1))
    plt.yticks(np.arange(y_max+1, step=1))
    # Set position of bar on X axis
    r3 = np.arange(len(x_list))
    r2 = [x - barWidth for x in r3]
    r1 = [x - barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]
    # Make the plot
    plt.bar(r5, y_list_best, width=barWidth,
            align='center', color='#9feb34', label='Best')
    plt.bar(r4, y_list_good, width=barWidth,
            align='center', color='#34ebeb', label='Good')
    plt.bar(r3, y_list_decent, width=barWidth,
            align='center', color='#ebe534', label='Decent')
    plt.bar(r2, y_list_poor, width=barWidth,
            align='center', color='#eb9334', label='Poor')
    plt.bar(r1, y_list_bad, width=barWidth,
            align='center', color='#eb4034', label='Bad')
    # Shows plot
    plt.legend()
    # plt.show()
    plt.savefig('GUI/Figure_Ratings.png')
