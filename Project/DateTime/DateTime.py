from datetime import datetime, timedelta
import pytz

""" Datetime module : can access attribute date, weekday, timestamp(), date'attribute and time's attribute"""
# get current day
date = datetime.today().strftime('%A')
print(date)                                                                     # Tuesday

past_day = datetime(2020, 5, 17)
print(past_day)                                                                 # 2020-05-17 00:00:00

t1 = datetime(year = 2018, month = 7, day = 12)
t2 = datetime(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)                                                               # t3 = 201 days, 0:00:00

# timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)                                                               # t3 = 14 days, 13:55:39
print("Total seconds =", t3.total_seconds())                                    # Total seconds = 1259739.0

# UTC
UTC = pytz.utc
print("UTC in Default Format :", datetime.now(UTC))                             # UTC in Default Format : 2022-01-11 14:40:06.914492+00:00

# London
IST = pytz.timezone('Europe/London')
print("London :", datetime.now(IST).strftime("%X"))                             # London : 13:14:11

# Bangkok
BNK = pytz.timezone('Asia/Bangkok')
print("Bangkok :", datetime.now(BNK).strftime("%X"))                            # Bangkok : 20:14:11

# format current date and time
now = datetime.now()

year = now.strftime("%Y")
print("year:", year)                                                            # year: 2022

month = now.strftime("%m")
print("month:", month)                                                          # month: 01

day = now.strftime("%d")
print("day:", day)                                                              # day: 11

time = now.strftime("%H:%M:%S")
print("time:", time)                                                            # time: 20:26:11

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)                                              # date and time: 01/11/2022, 20:26:11

""" Timestamp is the number of seconds between specific date and January 1, 1970 at UTC """
# string from timestamp
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)                                           # Date time object: 2018-06-12 16:55:22

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 1:", d)	                                                        # 06/12/2018, 16:55:22

d = date_time.strftime("%d %b, %Y")
print("Output 2:", d)                                                           # 12 Jun, 2018

d = date_time.strftime("%d %B, %Y")
print("Output 3:", d)                                                           # 12 June, 2018

d = date_time.strftime("%I%p")
print("Output 4:", d)                                                           # 04PM

d = date_time.strftime("%c")
print("Output 5:", d)	                                                        # Tue Jun 12 16:55:22 2018

d = date_time.strftime("%x")
print("Output 6:", d)                                                           # 06/12/18

d = date_time.strftime("%X")
print("Output 7:", d)                                                           # 16:55:22

""" date module : can access attribute year, month, day"""
from datetime import date

# date object of today's date
today = date.today() 

print("Today:", today)                                                          # Today: 2022-01-11
print("Current year:", today.year)                                              # Current year: 2022
print("Current month:", today.month)                                            # Current month: 1
print("Current day:", today.day)                                                # Current day: 11

""" Time module : can access attribute hour, minute, second, microsecond"""
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)                                                                 # a = 00:00:00

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)                                                                 # b = 11:34:56

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)                                                                 # c = 11:34:56

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)                                                                 # d = 11:34:56.234566

""" Find number of days between two given dates """
# To store number of days in all months from January to Dec.
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    # This function counts number of leap years (366 days) before the given date
    @staticmethod
    def countLeapYears(date):
        years = date.y

        # Check if the current year needs to be considered
        # for the count of leap years or not
        if (date.m <= 2): years -= 1

        # An year is a leap year if it is a multiple of 4,
        # multiple of 400 and not a multiple of 100.
        return int(years / 4) - int(years / 100) + int(years / 400)

    # This function returns number of days between two given dates
    @staticmethod
    def getDifference(date1, date2):
        # count total number of days before "date1"
        count1 = date1.y * 365 + date1.d
        for i in range(0, date1.m - 1):
            count1 += monthDays[i]
        count1 += Date.countLeapYears(date1)

        # count total number of days before "date2"
        count2 = date2.y * 365 + date2.d
        for i in range(0, date2.m - 1):
            count2 += monthDays[i]
        count2 += Date.countLeapYears(date2)

        # return difference between two counts
        return count2 - count1

""" Usage """
date1 = Date(26, 8, 2018)
date2 = Date(11, 1, 2021)
print(Date.getDifference(date1, date2), "days")      # 869 days