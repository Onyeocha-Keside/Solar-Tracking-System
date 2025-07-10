import time
from config import TIME_SOURCE

def get_current_time_and_date():
    if TIME_SOURCE == "GPS":
        # Code to get time from GPS module
        pass
    elif TIME_SOURCE == "NTP":
        # Code to get time from NTP server
        pass
    return time.time(), time.localtime()