import random
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# list=[ 2, 8, 5, -11, 3]

# sum=0

# for i in range(len(list)):
#     if i % 2 !=0:
#         sum+=list[i]
# print("Сумма чисел списка, стоящих на нечетных позициях, равна=", sum)

#Измененный код

list=[random. randint(-10,10) for x in range(5)]
print(list)
sum=0

for i,element in enumerate(list):
     if i % 2 != 0:
      sum += element

print("Сумма чисел списка, стоящих на нечетных позициях, равна=",sum)
