import requests
import sys


def getDateTime(url, field):
    response = requests.get(url)
    if response.ok:
        dateTime = response.json()[field]
        # Extracting date, and creating a list with the format [yyyy, mm, dd]
        date = list(map(int,
                        dateTime.split('T')[0]
                                .split('-')))
        # Extracting time and creating a list with the format [hours, minutes]
        time = list(map(int,
                        dateTime.split('T')[1][:-1]
                                .split(':')))
        return date, time
    else:
        sys.exit(1)

def convertToSpTimezone(dateUTC, timeUTC):
    year = 0
    month = 1
    day = 2
    # holding the numbers of days of each month
    # February have one more day in leap years
    daysInMonth = [
        31,                                     # Jan
        29 if dateUTC[year] % 4 == 0 else 28,   # Feb
        31,                                     # Mar
        30,                                     # Apr
        31,                                     # May
        30,                                     # Jun
        31,                                     # Jul
        31,                                     # Aug
        30,                                     # Sep
        31,                                     # Oct
        30,                                     # Nov
        31                                      # Dec
    ]
    # Convert to UTC-3, i.e. subtract the hours by 3
    # and fix the hour, month and year to make sense
    # e.g. -1h is not reasonable, neither month 0
    utcSpDiff = -3
    dateSP = dateUTC[:]
    timeSP = timeUTC[:]
    timeSP[0] += utcSpDiff
    if timeSP[0] < 0:
        timeSP[0] += 24
        dateSP[day] -= 1
        if dateSP[day] <= 0:
            dateSP[month] -= 1
            dateSP[day] += daysInMonth[dateSP[month] - 1]
            if dateSP[month] <= 0:
                dateSP[year] -= 1
                dateSP[month] += 12
    return dateSP, timeSP

def dateTimeToString(date, time, timezone='TEST'):
    # Make the original format of date and time from the API
    # e.g.: 2000-01-01T00:00Z
    date = list(map(lambda x: f"{x:02d}", date))
    time = list(map(lambda x: f"{x:02d}", time))
    return f"{timezone}: {'-'.join(date)}T{':'.join(time)}Z"


if __name__ == '__main__':
    dateUTC, timeUTC = getDateTime('http://worldclockapi.com/api/json/utc/now', 'currentDateTime')
    dateSP, timeSP = convertToSpTimezone(dateUTC, timeUTC)
    print(dateTimeToString(dateUTC, timeUTC, timezone='UTC'))
    print(dateTimeToString(dateSP, timeSP, timezone='UTC-3'))
