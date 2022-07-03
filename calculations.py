from random import randrange
import datetime


# Functions required
def format_date(date):
    return date.strftime("%d-%m-%y %H:%M:%S")


def random_date(start):
    curr = start + datetime.timedelta(days=randrange(8), minutes=randrange(600))  # at the end set right
    yield curr


# Variables and logic
def click_start():
    start_date = datetime.datetime.now()
    # print(start_date)
    return start_date


def end_date():
    final_date = [x for x in random_date(click_start())][0]
    return final_date


# calculating time difference and costs
def calc_costs(start, end):
    time_diff = end - start
    # print("time diff: ", str(time_diff))
    days = time_diff.days
    days_to_min = days * 24 * 60
    seconds = time_diff.seconds
    hours = seconds // 3600
    hours_to_min = hours * 60
    minutes = (seconds // 60) % 60
    total_min = days_to_min + hours_to_min + minutes
    total_costs = total_min * 0.50
    # print("days: ", days)
    # print("hours: ", hours)
    # print("minutes: ", minutes)
    # print("total minutes: ", total_min)
    # print("total costs: ", total_costs)

    return [total_min, total_costs]


def click_stop():
    ride_time = calc_costs(click_start(), end_date())[0]
    ride_costs = calc_costs(click_start(), end_date())[1]
    start_time = format_date(click_start())  # start_date convert into string
    end_time = format_date(end_date())
