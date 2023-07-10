# Joshua Soto
# 1553869

from datetime import date


def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


print("Birthday Calculator")
print('Current Day')
c_month = int(input('Month: '))
c_day = int(input('Day: '))
c_year = int(input('Year: '))
print("Birthday")
b_month = int(input('Month: '))
b_day = int(input('Day: '))
b_year = int(input('Year: '))
print("you are ", calculateAge(date(c_year, c_month, c_day), date(b_year, b_month, b_day)), "years old.")
if (c_month == b_month) and (c_day == b_day) and (c_year == b_year):
    print('Happy Birthday!')
