#  
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно))

# n=int(input("введите число="))
# list=[]

# for i in range(1,n+1):
#     a=((1+1/i)**i)
#     list.append(round(a,2))
# print(list)    

# print((sum(list)))

# Исправленный код

n=int(input("введите число="))
list=list(map(lambda i:(1+1/i)**i,[i for i in range(1,n+1)]))

print(list)  
summa=sum(list)
  
print((round(summa,2)))