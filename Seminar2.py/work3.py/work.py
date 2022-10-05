# list=["fkur7049f","f99p,d","ds'we0","skdls4792","495-2"]

# for el in list:
#    for a in el:
#     if a=="f":
#         print("Буква f есть в списке")
#     else:
#         print("Такой буквы нет")


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

from re import A


list1=["qwe", "asd", "zxc", "qwe", "ertqwe"]# ищем:  ответ: 3
list2=["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]#, ищем: "йцу", ответ: 5
list3=["йцу", "фыв", "ячс", "цук", "йцукен"]#, ищем: "йцу", ответ: -1
list4= ["123", "234", 123, "567"]#, ищем: "123", ответ: -1
list5=[]#, ищем: "123", ответ: -1

a="qwe"

def function(list):
    for el in list:
        for i in range (len(list)):
            if el==a:
                print(i)
            else:
                print("No","-1")
return(el)
        
function()