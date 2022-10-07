# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from audioop import minmax

list=[62.12, 5.89, 15.07, 6.21, 2.35, 4.08]
print(list)

newlist=[]

for i in range(len(list)):
    el=round(list[i]%1,2)
    if el!=0:
        newlist.append(el)    
print(newlist)

# def minmax(newlist):
#     newlist[0]=n_min
#     newlist[0]=n_max 
#     for i in range(len(newlist)):
#         if  i<n_min:
#             n_min=i
#         else:
#             if i>n_max:
#                 i=n_max
#             else:
#               print(n_max,n_min)
#     return(n_max,n_min)      

# minmax(newlist)
a=min(newlist)
b=max(newlist)

result=b-a
print("=>",round((result),2))