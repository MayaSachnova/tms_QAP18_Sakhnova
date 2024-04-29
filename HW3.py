# 1 Привести к целому типу - 1.6, 2.99

x = int(1.6)
y = int(2.99)

print(x,y)


# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

print("www.my_site.com#about".replace("#","/"))


# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

print("stroka" + "ing")


# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

str1 = "Ivanou Ivan"
str1 = str1.split(" ")
str1 = str1[::-1]
str1 = " ".join(str1)

print(str1)


# 5 Напишите программу которая удаляет пробел в начале, в конце строки

str2 = " Ivan Ivanou "

print(str2.strip())


# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в
# десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

school = {"1a": 20, "1b": 23}

print(school)


# 7 Создайте список и извлеките из него списка второй элемент.

list1 = (25, 41, 56, 87, 99)

print(list1[1])


# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )

a = "employ"
b = "employment"

print(a in b)


# 9 Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt

x = "My name is Agent Smith"

print(x[1])
print(x[3], x[6], x[9], x[12], x[15])

# 10 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число


numbers = [1, 5, 2, 9, 2, 9, 1]

unique = [i for i in numbers if numbers.count(i) == 1]

print(unique)








