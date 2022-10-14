from random import randint as rInt  

# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


dict_list={}
result_line=" "

listStr=''.join(list(map(str,[rInt(0,9) for i in range(25)])))
print(f"Случайная выборка чисел: {listStr}")

for c in listStr:
    if dict_list.get(c):
        dict_list[c]=dict_list.get(c)+1
       
    else:
        dict_list[c]=1
print(dict_list)  

for k,v in dict_list. items():
    if v==1:
        result_line += str(k)+"  "

print(f"Уникальные цифры {result_line}") if result_line else print("Уникальных позиций нет")
     