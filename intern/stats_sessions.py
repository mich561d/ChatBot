import matplotlib.pyplot as plt
import numpy as np
import traceback
import data_sessions as data


def chat_interval(year=0, month=0, week=0, day=0):
    years = []
    months = []
    weeks = []
    days = []
    try:
        # Gets specific year or all years
        if year == 0:
            for temp_year in data.SESSIONS.keys():
                years.append(temp_year)
        else:
            years.append(year)
        # Gets specific month or all month
        if month == 0:
            for temp_year in data.SESSIONS.keys():
                for temp_month in data.SESSIONS[temp_year].keys():
                    months.append(temp_month)
        else:
            months.append(month)
        # Gets specific week or all week
        if week == 0:
            for temp_year in data.SESSIONS.keys():
                for temp_month in data.SESSIONS[temp_year].keys():
                    for temp_week in data.SESSIONS[temp_year][temp_month].keys():
                        weeks.append(temp_week)
        else:
            weeks.append(week)
        # Gets specific day or all day
        if day == 0:
            for temp_year in data.SESSIONS.keys():
                for temp_month in data.SESSIONS[temp_year].keys():
                    for temp_week in data.SESSIONS[temp_year][temp_month].keys():
                        for temp_day in data.SESSIONS[temp_year][temp_month][temp_week].keys():
                            days.append(temp_day)
        else:
            days.append(day)
        # Create plot data
        plot_data = {}
        for temp_year in years:
            for temp_month in months:
                for temp_week in weeks:
                    for temp_day in days:
                        try:
                            for temp_hour in data.SESSIONS[temp_year][temp_month][temp_week][temp_day].keys():
                                temp_list = data.SESSIONS[temp_year][
                                    temp_month][temp_week][temp_day][temp_hour]
                                temp_sum = sum(temp_list)
                                temp_len = len(temp_list)
                                temp_avg = temp_sum / temp_len
                                temp_max = max(temp_list)
                                temp_min = min(temp_list)
                                plot_data.setdefault(
                                    temp_hour, [temp_avg, temp_max, temp_min])
                        except KeyError:
                            pass

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

        title = 'Average of chat data in minutes per hour of the day'
        subtitle = 'Years: {} | Month: {} | Weeks: {} | Days: {}'.format(
            years, months, weeks, days)
        x_label = 'Hours of the day'
        y_label = 'Session length in minutes'
        x_max = 24
        y_max = max(max_sessions) + (3 - (max(max_sessions) % 3))
        create_graph(
            title,
            subtitle,
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
        print(years)
        print(months)
        print(weeks)
        print(days)


def create_graph(title, subtitle, x_label, y_label, x_max, y_max, x_list, y_list_avg, y_list_max, y_list_min):
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
    plt.yticks(np.arange(y_max+1, step=3))
    # Creates bars
    plt.bar(x_list, y_list_max, width=0.25, align='edge', color='#ff8c8c', label='Maximum length')
    plt.bar(x_list, y_list_avg, width=0.25, align='center', color='#8cff8c', label='Average length')
    plt.bar(x_list, y_list_min, width=-0.25, align='edge', color='#6bcffa', label='Minimum length')
    # Shows plot
    plt.legend()
    plt.show()


# TODO: Remove
chat_interval()
chat_interval(2019, 10, 44, 31)
