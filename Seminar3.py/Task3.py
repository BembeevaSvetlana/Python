# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list=[1.1, 1.2, 3.1, 5, 10.01]
print(list)

for i in range(len(list)):
    el=round(list[i]%10)
    print(el)
    
   