#### preinstalled python dependancies
from datetime import datetime

### user created dependancies
from modules import helpers

def check_time_elapsed(time_then, timer_duration):
    hour, minutes, seconds = timer_duration.split(':')
    hour, minutes, seconds = int(hour), int(minutes), int(seconds)
    time_now = datetime.now()
    time_elapsed = time_now - time_then
    hours_elapsed = int(time_elapsed.total_seconds() / 60 / 60)
    minutes_elapsed = int(time_elapsed.total_seconds() / 60)
    seconds_elapsed = int(time_elapsed.total_seconds() - (minutes * 60))

    if hours_elapsed >= hour:
        if minutes_elapsed >= minutes:
            if seconds_elapsed >= seconds:
                return True

    # hours left
    if hours_elapsed > hour:
        hours_left = 0
    else:
        hours_left = int(hour - hours_elapsed)
    # minutes left
    if minutes_elapsed > minutes:
        minutes_left = 0
    else:
        minutes_left = int(minutes - minutes_elapsed)
    # seconds left
    if seconds_elapsed > seconds:
        seconds_left = 0
    else:
        seconds_left = int(seconds - seconds_elapsed)
    return f'{hours_left}:{minutes_left}:{seconds_left}'

def get_time_from_string(string_with_time):
    hour, minutes, seconds = 0, 0, 0
    # get hour, minutes, and seconds from voice input
    if 'hour' in string_with_time:
        hour = helpers.string_before(string_with_time, 'hour')
    if 'minutes' in string_with_time:
        if hour > 0:
            minutes = helpers.string_after(string_with_time, 'hour')
            minutes = helpers.string_before(minutes, 'minutes')
        else:
            minutes = helpers.string_before(minutes, 'minutes')
    if 'seconds' in string_with_time:
        if hour > 0 and minutes == 0:
            seconds = helpers.string_after(string_with_time, 'hour')
            seconds = helpers.string_before(seconds, 'seconds')
        elif minutes > 0:
            seconds = helpers.string_after(string_with_time, 'minutes')
            seconds = helpers.string_before(seconds, 'seconds')
        else:
            seconds = helpers.string_before(string_with_time, 'seconds')
    return f'{hour}:{minutes}:{seconds}'