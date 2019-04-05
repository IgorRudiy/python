# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Задача из урока 3. №7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными)

import random
n = input("Введите размер массива: ")
if n.isdigit():
  n=int(n)
else:    
  print("Ошибка ввода")
  exit()
l=input("Введите максмальную разрядность чисел (не более 9): ")
if l.isdigit(): 
  l=int(l)
  if l > 9:
    print("Ошибка ввода разрядности")
    exit()
else:  
  print("Ошибка ввода цифры")
  exit()
m=[]
for i in range(0,n):
  m.append(random.randint(0,10**l-1))

# print(m)

# Вариант 2
def var1():
  if m[1] < m[0]:
    min1 = m[1]
    i_min1 = 1
    min2 = m[0]
    i_min2 = 0
  else:
    min1 = m[0]
    i_min1 = 0
    min2 = m[1]
    i_min2 = 1
  for i in range(2,len(m)):
    if m[i] < min2 :
      if m[i] < min1:
        min2 = min1
        i_min2 = i_min1
        min1 = m[i]
        i_min1 = i
      else:
        min2 = m[i]
        i_min2 = i
  return i_min1, i_min2 

# Вариант 2
def var2():
  min1 = min2 = max(m)
  i_min1 = i_min2 = m.index(min1)
  for i, n in enumerate(m):
    if n < min2 :
      if n < min1:
        min2 = min1
        i_min2 = i_min1
        min1 = n
        i_min1 = i
      else:
        min2 = n
        i_min2 = i
  return i_min1, i_min2 

# Вариант 3
def var3():
  i_min1 = m.index(min(m))
  return i_min1, m.index(min(m[:i_min1]+m[i_min1+1:]))

print("Проверка функций")
print(var1())
print(var2())
print(var3())

import timeit
print(timeit.timeit("var1()", setup="from __main__ import var1", number=10))
print(timeit.timeit("var2()", setup="from __main__ import var2", number=10))
print(timeit.timeit("var3()", setup="from __main__ import var3", number=10))

def main():
  v1_1 , v1_2  = var1()
  v2_1 , v2_2  = var2()
  v3_1 , v3_2  = var3()

import cProfile
cProfile.run('main()')
