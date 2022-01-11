""" Format use in strftime()
Directive	| Meaning	                                                                                                              | Example
%a	        | Abbreviated weekday name.	                                                                                              | Sun, Mon, ...
%A	        | Full weekday name.	Sunday,                                                                                           | Monday, ...
%w	        | Weekday as a decimal number.	                                                                                          | 0, 1, ..., 6
%d	        | Day of the month as a zero-padded decimal.	                                                                          | 01, 02, ..., 31
%-d	        | Day of the month as a decimal number.	                                                                                  | 1, 2, ..., 30
%b	        | Abbreviated month name.	                                                                                              | Jan, Feb, ..., Dec
%B	        | Full month name.	                                                                                                      | January, February, ...
%m	        | Month as a zero-padded decimal number.	                                                                              | 01, 02, ..., 12
%-m	        | Month as a decimal number.	                                                                                          | 1, 2, ..., 12
%y	        | Year without century as a zero-padded decimal number.	                                                                  | 00, 01, ..., 99
%-y	        | Year without century as a decimal number.	                                                                              | 0, 1, ..., 99
%Y	        | Year with century as a decimal number.	                                                                              | 2013, 2019 etc.
%H	        | Hour (24-hour clock) as a zero-padded decimal number.	                                                                  | 00, 01, ..., 23
%-H	        | Hour (24-hour clock) as a decimal number.	                                                                              | 0, 1, ..., 23
%I	        | Hour (12-hour clock) as a zero-padded decimal number.	                                                                  | 01, 02, ..., 12
%-I	        | Hour (12-hour clock) as a decimal number.	                                                                              | 1, 2, ... 12
%p	        | Locale’s AM or PM.	                                                                                                  | AM, PM
%M	        | Minute as a zero-padded decimal number.	                                                                              | 00, 01, ..., 59
%-M	        | Minute as a decimal number.	                                                                                          | 0, 1, ..., 59
%S	        | Second as a zero-padded decimal number.	                                                                              | 00, 01, ..., 59
%-S	        | Second as a decimal number.	                                                                                          | 0, 1, ..., 59
%f	        | Microsecond as a decimal number, zero-padded on the left.	                                                              | 000000 - 999999
%z	        | UTC offset in the form +HHMM or -HHMM.	                                                                              |
%Z	        | Time zone name.	                                                                                                      |
%j	        | Day of the year as a zero-padded decimal number.	                                                                      | 001, 002, ..., 366
%-j	        | Day of the year as a decimal number.	                                                                                  | 1, 2, ..., 366
%U	        | Week number of the year (Sunday as the first day of the week). All days in Sunday are considered to be in week 0.       | 00, 01, ..., 53
%W	        | Week number of the year (Monday as the first day of the week). All days in Monday are considered to be in week 0.       | 00, 01, ..., 53
%c	        | Locale’s appropriate date and time representation.	                                                                  | Mon Sep 30 07:06:05 2013
%x	        | Locale’s appropriate date representation.	                                                                              | 09/30/13
%X	        | Locale’s appropriate time representation.	                                                                              | 07:06:05
%%	        | A literal '%' character.	                                                                                              | % """

from datetime import datetime
import pytz

# get current day
date = datetime.today().strftime('%A')
print(date)                                                                     # Tuesday

# UTC
UTC = pytz.utc
print("UTC in Default Format :", datetime.now(UTC).strftime("%X"))              # UTC in Default Format : 13:14:11

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