#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list=[2, 8, 5, -11, 3]

sum=0

for i in range(len(list)):
    if i % 2 !=0:
        sum+=list[i]
print("Сумма чисел списка, стоящих на нечетных позициях, равна=", sum)
        
        