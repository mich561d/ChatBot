import matplotlib.pyplot as plt
import numpy as np
import traceback
import json
import datetime as dt
from calendar import monthrange
import operator
import collections

with open('./data_test.json') as json_file:
    data = json.load(json_file)


def chatBot_common_tags(year=0, month=0):
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
                for temp_user in temp_users:
                    for temp_line in temp_user['lines']:
                        tag = temp_line['tag']
                        value = plot_data.setdefault(tag, 0)
                        plot_data.update({tag: (value + 1)})
            except KeyError:
                pass

        sorted_data_list = sorted(
            plot_data.items(), key=operator.itemgetter(1), reverse=True)
        sorted_plot_data = collections.OrderedDict(sorted_data_list)
        common_tags_used = list(sorted_plot_data.keys())
        times_used_per_tag = list(sorted_plot_data.values())

        title = 'Most common tags used'
        x_label = 'Tags'
        y_label = 'Times used'
        x_max = len(common_tags_used)
        y_max = max(times_used_per_tag) + 5
        create_graph(
            title,
            x_label,
            y_label,
            x_max,
            y_max,
            common_tags_used,
            times_used_per_tag
        )
    except KeyError:
        traceback.print_exc()


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
    plt.xticks(np.arange(x_max+1, step=1))
    plt.yticks(np.arange(y_max+1, step=5))
    # Creates bars
    plt.bar(x_list, y_list, width=0.5, align='center',
            color='#8cff8c', label='Times used')
    # Shows plot
    plt.legend()
    # plt.show()
    plt.savefig('GUI/Figure_Tags.png')
