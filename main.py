#Напишите программу, которая запрашивает у пользователя последовательно день
#его рождения, месяц и год;

function getBirthday() {
  var day = document.getElementsByName("day")[0].value;
  var month = document.getElementsByName("month")[0].value;
  var year = document.getElementsByName("year")[0].value;
  
  var birthday = day + "." + month + "." + year;
  
  alert("Ваша дата рождения: " + birthday);
}

#Реализуйте вывод в консоль даты рождения пользователя в формате дд мм гггг,
#где цифры прорисованы звёздочками (*), как на электронном табло.

import datetime
import calendar
from art import *

def get_birthday():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return day, month, year

def day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def is_leap_year(year):
    return calendar.isleap(year)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def display_date_as_stars(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    date_str = f"{day_str} {month_str} {year_str}"
    print(text2art(date_str))

def main():
    day, month, year = get_birthday()
    print(f"Вы родились в {day_of_week(day, month, year)}.")
    print(f"Ваш год рождения {year} {'високосный' if is_leap_year(year) else 'не високосный'}.")
    print(f"Вам сейчас {calculate_age(day, month, year)} лет.")
    print("Ваша дата рождения в формате дд мм гггг:")
    display_date_as_stars(day, month, year)

if __name__ == "__main__":
    main()
