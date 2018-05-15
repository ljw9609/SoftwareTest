# get year from input
# the year should be after 1900. if not, exit
def getYear():
    print("This program prints the calendar of a given year.")
    year = input("Please enter a year (after 1900): ")

    try:
        year = int(year)
    except:
        print("error")
        exit(1)

    if year < 1900:
        print("error")
        exit(1)

    return year


# check if a year is a leap year
# if yes, return True; if not, return False
def leapyear(year):
    if year % 4 != 0:
        leap = False
    else:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
        else:
            leap = False

    return leap


# count how many years between 0000 and year
def allLeapyears(year):
    return (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400


# get the day of the year's first date
def firstDay(year):
    leapyears = allLeapyears(year - 1) - allLeapyears(1900 - 1)
    return ((year - 1900) * (365 % 7) + leapyears + 1) % 7


# get how many dates of the month in the year
def datesOfMonth(year, month):
    if month == 1:
        date = 31
    elif month == 2:
        if leapyear(year):
            date = 29
        else:
            date = 28
    elif month == 3:
        date = 31
    elif month == 4:
        date = 30
    elif month == 5:
        date = 31
    elif month == 6:
        date = 30
    elif month == 7:
        date = 31
    elif month == 8:
        date = 31
    elif month == 9:
        date = 30
    elif month == 10:
        date = 31
    elif month == 11:
        date = 30
    elif month == 12:
        date = 31
    else:
        print("error")
        exit(1)

    return date


# get the day of the month's first date in the year
def firstDayOfMonth(year, month):
    allDates = 0
    if month == 1:
        return firstDay(year)
    else:
        for i in range(1, month):
            if i == 1:
                allDates = allDates + 31
            elif i == 2:
                if leapyear(year):
                    allDates = allDates + 29
                else:
                    allDates = allDates + 28
            elif i == 3:
                allDates = allDates + 31
            elif i == 4:
                allDates = allDates + 30
            elif i == 5:
                allDates = allDates + 31
            elif i == 6:
                allDates = allDates + 30
            elif i == 7:
                allDates = allDates + 31
            elif i == 8:
                allDates = allDates + 31
            elif i == 9:
                allDates = allDates + 30
            elif i == 10:
                allDates = allDates + 31
            elif i == 11:
                allDates = allDates + 30
            elif i == 12:
                allDates = allDates + 31
            else:
                print("error")
                exit(1)
        return (allDates + firstDay(year)) % 7


# generate the month output, store it in a list
def layout(year, month):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    if month == 1:
        monthword = "Jan"
    elif month == 2:
        monthword = "Feb"
    elif month == 3:
        monthword = "Mar"
    elif month == 4:
        monthword = "Apr"
    elif month == 5:
        monthword = "May"
    elif month == 6:
        monthword = "Jun"
    elif month == 7:
        monthword = "Jul"
    elif month == 8:
        monthword = "Aug"
    elif month == 9:
        monthword = "Sep"
    elif month == 10:
        monthword = "Oct"
    elif month == 11:
        monthword = "Nov"
    elif month == 12:
        monthword = "Dec"
    else:
        print("error")
        exit(1)

    frame = [["   "] * 3 + [monthword] + ["   "] * 3, days]

    for i in range(6):
        frame.append([""] * 7)
    for i in range(1, datesOfMonth(year, month) + 1):
        j = i + firstDayOfMonth(year, month) - 1
        frame[j // 7 + 2][j % 7] = i

    return frame


# print the final result with three months in one line
def printCalendar(year):
    print()
    li = [""] * 12
    for i in range(12):
        li[i] = layout(year, i + 1)
    for i in range(4):
        for m in range(8):
            for j in range(3):
                for n in range(7):
                    print("%3s " % (str(li[i * 3 + j][m][n])), end="")
                print("   ", end="")
            print()
        print()


def main():
    year = getYear()
    print()
    print("===========================================%d============================================" % (year))
    printCalendar(year)


if __name__ == "__main__":
    main()
