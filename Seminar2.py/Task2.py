
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

num=int(input("введите число="))
p=1
list=[]
for i in range(1,num+1):
    p *=i
    list.append(p)
print(list)
      
        