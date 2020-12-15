import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader) # make reader to the next line(the second), return
    # the first line. So header_row is the first line.

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            # the strptime is format the date(the first coefficient) to the format
            # the second coefficent sets
            # %A the weekday name, like Monday
            # %B the month name, like January
            # %m the month number. like 01-12
            # %d the day number, 01-31
            # %Y the year number with 4 digits, like:2014
            # %y the year number with 2 digits, like:14
            # %H the hour with 24 hours format, 00-23
            # %I the hour with 12 hours format, 01-12
            # %p pm or am
            # %M minutes number, 00-59
            # %S seconds, 00-61
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            lows.append((low))
            dates.append(current_date)

    # print(highs)
    fig = plt.figure(dpi=80, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5) # alpha is the degree of transparence, which is between 0 and 1
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # to fill the empty areas between high-curve and low-curve
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title('Daily high and low temperatures \nDeath vally, CA', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    # make the xlabels suit the fontsieze automatically, thus making
    # the dates declined
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


