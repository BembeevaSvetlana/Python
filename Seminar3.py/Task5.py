# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

n = int(input('Введите длину ряда Фибоначчи: '))

def fibo(n):
    if n>=0:
       idx = range(n+1)
       x = [0,1]
       for k in idx[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[n]
    else:
       n=-(n-1)
       idx = range(n+1)
       x = [1,0]
       for k in idx[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]

for i in range(-(n),n+1):
   print(fibo(i), end=" ")
   
fibo(n)


# n = int(input('Введите длину ряда Фибоначчи: '))
# n2 = int(input('Введите длину ряда Фибоначчи отрицательную: '))

# f1 = 0 
# f2 = 1
# print(f1, f2, end=' ')
# i = 2
# while i < n:
# 	f1, f2 = f2, f1 + f2 
# 	print(f2, end=' ') 
# 	i += 1
# print()

# h1 = 1
# h2=(-1)
# print(h1, h2, end=' ')
# i=-2
# while -i > n2:
# 	h1, h2 = h2, h2 - h1
# 	print(h2, end=' ') 
# 	i -= 1
# print()
