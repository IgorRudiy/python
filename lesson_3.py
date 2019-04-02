# 1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# Вариант 1
# print ({i: 1000000//i for i in range(2,10)})

# Вариант 2
# for i in range(2,10):
#   print("Числу %i кратны %i чисел" % (i,1000000//i))
 
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# import random
# n = input("Введите размер массива 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)
# m2=[]
# for i in range(len(m)):
#   if (m[i] % 2) == 0:
#     m2.append(i)        
# print("Следующие элементы массива 1 содержат четные числа:")
# print(m2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Меняем местами все минимальные и все максимальные значения массива! 

# import random
# n = input("Введите размер массива 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l))
# print(m)
# max = max(m)
# min = min(m)
# for i in range(len(m)):
#   if m[i] == max:
#     m[i] = min
#   elif m[i] == min:
#     m[i] = max
# print(m)    

# 4. Определить, какое число в массиве встречается чаще всего.

# import random
# n = input("Введите размер массива 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
#  l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)

# m2 = []
# k2 = []
# for i in m:
#     if i not in m2:
#       m2.append(i)
#       k2.append(m.count(i))

# max = max(k2)
# print("В массиве чаще всего, %i раз встречаются следующие числа:" % max)
# for i in range(len(k2)):
#   if k2[i] == max:
#     print(m2[i])

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# import random
# n = input("Введите размер массива: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(-10**l+1,10**l-1))
# print(m)
# n = min(m)

# for i in range(len(m)):
#   if 0 > m[i] > n:
#     n = m[i]
#     i_n = i
# print(i_n, n)

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# import random
# n = input("Введите размер массива: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)

# i_min = m.index(min(m))
# i_max = m.index(max(m))
# if i_max > i_min:
#   print(m[i_min+1 : i_max])
# else:
#   print(m[i_max+1 : i_min])

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными)

# import random
# n = input("Введите размер массива: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)

# i_mim1 = m.index(min(m))
# i_min2 = m.index(mi4(m[:i_min1]+m[i_min1+1:]))

# print(m[i_min1], m[i_min2])


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# X = 5
# Y = 4
# m = []
# for i in range(Y):
#   n = []
#   print("Введите 4 значения строки %i:" %i)
#   for j in range(X-1):
#     n.append(int(input()))
#   m.append(n)

# print (m)    
# for i in range(Y):
#   m[i].append(sum(m[i]))

# for i in m:
#   print(i)


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# import random
# n = input("Введите размер матрицы: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("Ошибка ввода")
#   exit()
# l=input("Введите максмальную разрядность чисел (не более 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("Ошибка ввода разрядности")
#     exit()
# else:  
#   print("Ошибка ввода цифры")
#   exit()
# m=[]
# for i in range(n):
#   m2 = []
#   for j in range(n):
#     m2.append(random.randint(0,10**l-1))
#   m.append(m2)

# for i in m:
#     print(i)
# max_min = 0
# for i in range(n):
#   if min(m[i]) > max_min:
#     max_min = min(m[i])
# print(max_min)