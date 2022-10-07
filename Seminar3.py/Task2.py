import random
# # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # [2, 3, 4, 5, 6] => [12, 15, 16]
# # [2, 3, 5, 6] => [12, 15]

k = int(input('Введите размер списка '))
list = []
newlist = []

for i in range(k):
    list.append(random.randint(0, 10))
print(list)

for i in range(len(list)):
    while i < len(list)/2 and k > len(list)/2:
        k = k - 1
        a = list[i] * list[k]
        newlist.append(a)
        i += 1


print(newlist)





