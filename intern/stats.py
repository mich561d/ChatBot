from stats_activity import chat_session_count as activity
from stats_countries import chatBot_countries as countries
from stats_knowledge import chatBot_learing_rate as knowledge
from stats_learning import chatBot_learning_time as learning
from stats_ratings import chatBot_ratings as ratings
from stats_sessions import chat_interval as sessions
from stats_tags import chatBot_common_tags as tags
from stats_users import chatBot_ip as users


def generate_plots(year=2019, month=12):
    print('---------- Starting creating plots ----------')
    activity(year=year, month=month)
    print('1. Activity Done')
    countries(year=year, month=month)
    print('2. Countries Done')
    knowledge(year=year, month=month)
    print('3. Knowledge Done')
    learning(year=year, month=month)
    print('4. Learning Done')
    ratings(year=year, month=month)
    print('5. Ratings Done')
    sessions(year=year, month=month)
    print('6. Sessions Done')
    tags(year=year, month=month)
    print('7. Tags Done')
    users(year=year, month=month)
    print('8. Users Done')
    print('-------------------- End --------------------')

generate_plots()