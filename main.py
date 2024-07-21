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
day = input("Введите день вашего рождения: ")
month = input("Введите месяц вашего рождения: ")
year = input("Введите год вашего рождения: ")

formatted_day = day.replace("0", "*")
formatted_month = month.replace("0", "*")
formatted_year = year.replace("0", "*")

print("Вы родились", formatted_day, formatted_month, formatted_year)
