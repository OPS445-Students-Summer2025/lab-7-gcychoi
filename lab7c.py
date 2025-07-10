#!/usr/bin/env python3
# Name: lab7c.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/07/09

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sec_t1 = time_to_sec(t1) # conver the time to second
    sec_t2 = time_to_sec(t2) # conver the time to second

    sum = sec_t1 + sec_t2 # add the seconds

    t1_sec = sec_to_time(sum) # convert the second to time

    return t1_sec

def change_time(time, seconds):
    sec_t1 = time_to_sec(time) # conver the time to second

    sum = sec_t1 + seconds # add the seconds

    t1_sec = sec_to_time(sum) # convert the second to time

    time.hour = t1_sec.hour # assign new hour to time.hour
    time.minute = t1_sec.minute # assign new minute to time.minute
    time.second = t1_sec.second # assign new second to time.second

    return None
...
...
def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time
...
...

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
