# 1. � ��������� ����������� ����� �� 2 �� 1000000 ����������, ������� �� ��� ������ ������� �� ����� � ��������� �� 2 �� 9.

# ������� 1
# print ({i: 1000000//i for i in range(2,10)})

# ������� 2
# for i in range(2,10):
#   print("����� %i ������ %i �����" % (i,1000000//i))
 
# 2. �� ������ ������� ��������� ������� ������ ��������� ������� �������. ��������, ���� ��� ������ �� ���������� 8, 3, 15, 6, 4, 2, �� �� ������ ������ ���� ��������� ���������� 1, 4, 5, 6 (��� 0, 3, 4, 5 - ���� ���������� ���������� � ����), �.�. ������ � ���� �������� ������� ������� ����� ������ �����.

# import random
# n = input("������� ������ ������� 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)
# m2=[]
# for i in range(len(m)):
#   if (m[i] % 2) == 0:
#     m2.append(i)        
# print("��������� �������� ������� 1 �������� ������ �����:")
# print(m2)

# 3. � ������� ��������� ����� ����� �������� ������� ����������� � ������������ ��������.

# ������ ������� ��� ����������� � ��� ������������ �������� �������! 

# import random
# n = input("������� ������ ������� 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
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

# 4. ����������, ����� ����� � ������� ����������� ���� �����.

# import random
# n = input("������� ������ ������� 1: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
#  l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
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
# print("� ������� ���� �����, %i ��� ����������� ��������� �����:" % max)
# for i in range(len(k2)):
#   if k2[i] == max:
#     print(m2[i])

# 5. � ������� ����� ������������ ������������� �������. ������� �� ����� ��� �������� � ������� � �������.

# import random
# n = input("������� ������ �������: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
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

# 6. � ���������� ������� ����� ����� ���������, ����������� ����� ����������� � ������������ ����������. ���� ����������� � ������������ �������� � ����� �� ��������.

# import random
# n = input("������� ������ �������: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
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

# 7. � ���������� ������� ����� ����� ���������� ��� ���������� ��������. ��� ����� ���� ��� ����� ����� ����� (��� �������� ������������)

# import random
# n = input("������� ������ �������: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
#   exit()
# m=[]
# for i in range(0,n):
#   m.append(random.randint(0,10**l-1))
# print(m)

# i_mim1 = m.index(min(m))
# i_min2 = m.index(mi4(m[:i_min1]+m[i_min1+1:]))

# print(m[i_min1], m[i_min2])


# 8. ������� 5x4 ����������� ������ � ���������� ����� ��������� ��������� �����. ��������� ������ ��������� ����� ��������� ��������� ������ ������ � ���������� �� � ��������� ������ ������. � ����� ������� ������� ���������� �������.

# X = 5
# Y = 4
# m = []
# for i in range(Y):
#   n = []
#   print("������� 4 �������� ������ %i:" %i)
#   for j in range(X-1):
#     n.append(int(input()))
#   m.append(n)

# print (m)    
# for i in range(Y):
#   m[i].append(sum(m[i]))

# for i in m:
#   print(i)


# 9. ����� ������������ ������� ����� ����������� ��������� �������� �������.
# import random
# n = input("������� ������ �������: ")
# if n.isdigit():
#   n=int(n)
# else:    
#   print("������ �����")
#   exit()
# l=input("������� ����������� ����������� ����� (�� ����� 9): ")
# if l.isdigit(): 
#   l=int(l)
#   if l > 9:
#     print("������ ����� �����������")
#     exit()
# else:  
#   print("������ ����� �����")
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