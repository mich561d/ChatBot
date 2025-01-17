import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chat_interval(year=0, month=0):
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
        date_format = '%d/%m/%Y %H:%M:%S'
        temp_hours_of_the_day = {}
        for i in range(1, days_in_month+1):
            try:
                for temp_user in data[str(year)][str(month)][str(i)]:
                    start_time = dt.datetime.strptime(
                        temp_user['start'], date_format)
                    end_time = dt.datetime.strptime(
                        temp_user['end'], date_format)
                    time_between = (end_time - start_time).seconds

                    temp_hour = start_time.hour
                    if temp_hour not in temp_hours_of_the_day.keys():
                        temp_hours_of_the_day[temp_hour] = {
                            'sum': 0, 'len': 0, 'max': 0, 'min': 10000}

                    temp_hours_of_the_day[temp_hour]['sum'] += time_between
                    temp_hours_of_the_day[temp_hour]['len'] += 1
                    temp_hours_of_the_day[temp_hour]['max'] = time_between if time_between > temp_hours_of_the_day[
                        temp_hour]['max'] else temp_hours_of_the_day[temp_hour]['max']
                    temp_hours_of_the_day[temp_hour]['min'] = time_between if time_between < temp_hours_of_the_day[
                        temp_hour]['min'] else temp_hours_of_the_day[temp_hour]['min']
            except KeyError as e:
                pass
            for hour in temp_hours_of_the_day.keys():
                temp_avg = (temp_hours_of_the_day[hour]['sum'] /
                            temp_hours_of_the_day[hour]['len']) / 60
                temp_max = temp_hours_of_the_day[hour]['max'] / 60
                temp_min = temp_hours_of_the_day[hour]['min'] / 60
                plot_data.setdefault(hour, [temp_avg, temp_max, temp_min])

        hours_of_the_day = list(plot_data.keys())
        chat_sessions_in_minutes = list(plot_data.values())
        avg_sessions = list(plot_data.keys())
        max_sessions = list(plot_data.keys())
        min_sessions = list(plot_data.keys())
        temp_counter = 0
        for temp_session in chat_sessions_in_minutes:
            avg_sessions[temp_counter] = temp_session[0]
            max_sessions[temp_counter] = temp_session[1]
            min_sessions[temp_counter] = temp_session[2]
            temp_counter += 1

        title = 'Average of chat sessions in minutes per hour of the day'
        x_label = 'Hours of the day'
        y_label = 'Session length in minutes'
        x_max = 24
        y_max = max(max_sessions) + 3#(3 - (max(max_sessions) % 3))
        create_graph(
            title,
            x_label,
            y_label,
            x_max,
            y_max,
            hours_of_the_day,
            avg_sessions,
            max_sessions,
            min_sessions
        )
    except KeyError:
        traceback.print_exc()


def create_graph(title, x_label, y_label, x_max, y_max, x_list, y_list_avg, y_list_max, y_list_min):
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
    plt.yticks(np.arange(y_max+1, step=3))
    # Creates bars
    plt.bar(x_list, y_list_max, width=0.25, align='edge',
            color='#ff8c8c', label='Maximum length')
    plt.bar(x_list, y_list_avg, width=0.25, align='center',
            color='#8cff8c', label='Average length')
    plt.bar(x_list, y_list_min, width=-0.25, align='edge',
            color='#6bcffa', label='Minimum length')
    # Shows plot
    plt.legend()
    # plt.show()
    plt.savefig('Figure_Sessions.png')
    plt.close()
