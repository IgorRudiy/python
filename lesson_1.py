﻿#   1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# a = input("Введите число: ")
# if len(a) != 3:
#   print("Ошибка! Надо ввести 3 знака") 
# elif a.isdigit():
#   s=0
#   m=1
#   for i in a:
#     n= int(i)
#     s+=n
#     if n>0:
#       m*=n
#   print("Сумма : ", s)
#   print("Произведение : ", m)
# else:
#     print("Ошибка! Введены не только цифры.")

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
# print("Побитовое И: " , 5 & 6)
# print("Побитовое ИЛИ: " , 5 | 6)
# print("Побитовое исключительное ИЛИ: " , 5 ^ 6)
# print("Сдвиг влево: " , 5<<2)
# print("Сдвиг вправо: " , 5>>2)
# Побитовый сдвиг числа x влево на n знаков равен x*2**n   
# Побитовый сдвиг числа x вправо на n знаков равен x//2**n   

# 3. По введенным пользователем координатам дву х точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# def is_float(str):
#   try:
#     float(str)
#     return float(str)
#   except ValueError:
#     print("Ошибка! Это не число")
#     exit()
# print("Определяем координаты прямой по двум точкам")

# print("Введите координаты точки 1:")
# x1 = is_float(input("x1 = "))
# y1 = is_float(input("y1 = "))

# print("Введите координаты точки 2:")
# x2 = is_float(input("x2 = "))
# y2 = is_float(input("y2 = "))

# print("Искомое уравнение прямой :")
# yx = (y2 - y1) / (x2 - x1)
# y0 = y1 - yx*x1
# print(" y = %.3f + %.3f * x" % (y0, yx))


# 4. Написать программу, которая генерирует в указанных пользователем границах:

# случайное целое число;
# import random
# def is_int(a):
#   if a.isdigit():
#     return int(a)
#   else:
#     print("Ошибка! Это не целое число")
#     exit()

# print("Генерим случайное целое число в диапазоне")

# n1 = is_int(input("Нижняя граница диапазона : "))
# n2 = is_int(input("Верхняя граница диапазона: "))

# if n2>n1:
#     print("Искомое число :", random.randint(n1, n2))
# else:
#     print("Ошибка! Верхняя граница диапазона должна быть болше нижней")

# случайное вещественное число;
# import random
# def is_float(str):
#   try:
#     float(str)
#     return float(str)
#   except ValueError:
#     print("Ошибка! Это не число")
#     exit()

# print("Генерим случайное вещественное число в диапазоне")

# n1 = is_float(input("Нижняя граница диапазона : "))
# n2 = is_float(input("Верхняя граница диапазона: "))

# if n2>n1:
#   print("Искомое число :", random.uniform(n1, n2))
# else:
#   print("Ошибка! Верхняя граница диапазона должна быть болше нижней")

# случайный символ.

# import random
# print("Генерим случайный символ в диапазоне")

# s1 = input("Нижняя граница диапазона : ")
# s2 = input("Верхняя граница диапазона: ")

# if len(s1) == 1 and len(s2) == 1:
#     s1 = ord(s1)
#     s2 = ord(s2)
#     if s2 > s1:
#         print("Искомый символ :", chr(random.randint(s1, s2)))
#     else:
#         print("Искомый символ :", chr(random.randint(s2, s1)))
# else:
#     print("Ошибка! Надо было ввести по одному символу")


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# import string
# st = input("Введите два сивола : ").lower()

# if len(st) == 2:
#   n1 = string.ascii_lowercase.index(st[0])
#   n2 = string.ascii_lowercase.index(st[1])

#   print("Первый символ: %i ; второй: %i ;" % (n1,n2))
#   if (n2 - n1) > 1:
#       print("Между ними %i символов" % (n2-n1-1))
#   elif (n1 - n2) > 2:
#       print("Между ними %i символов" % (n1-n2-1))
#   else:
#       print("Между ними в алфавите нет символов")

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# import string
# st = input("Введите номер буквы в алфавите : ")
# if st.isdigit():
#   if int(st)<53:
#     print("Буква с этим номером:", string.ascii_letters[int(st)-1])
#   else:
#     print("Ошибка! Введите число не более 52")
# else:
#   print("Ошибка! Это не целое число")

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# print("Введите длины трех отрезков")
# a = (float(input("длина 1 = ")), 
#     float(input("длина 2 = ")), 
#     float(input("длина 3 = ")))
# if sum(a) > 2* max(a):
#     if max(a) == min(a):
#         print("Эти отрезки составляют равносторонний трехугольник")
#     elif sum(a) == max(a) + 2 * min(a) or sum(a) == 2 * max(a) + min(a) :
#         print("Эти отрезки составляют равнобкдренный трехугольник")
# else:
#     print("Эти отрезки не являются сторонами трехугольника")

# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# st = input("Введите год: ")
# if st.isdigit():
#   if (a % 4) == 0:
#       print("Это високосный год")
#   else:
#       print("Это не високосный год")
# else:
#   print("Ошибка! Это не целое число")

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# print("Введите три числа")
# a = (float(input("Число 1 = ")), 
#     float(input("Число 2 = ")), 
#     float(input("Число 3 = ")))
# for i in a:
#     if i != max(a) and i != min(a):
#         print("Число %i среднее " % i)
#         break
