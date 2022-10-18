#  Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'
# Оба задания обязательны

from random import randint

# pl1 = input("Введите имя первого игрока: ")
# pl2 = input("Введите имя второго игрока: ")
# total = int(input("Введите количество конфет на столе: "))

# flag = randint(0,1) 
# if flag == 1:
#     winner = pl1
# else:
#     winner = pl2
# print(f'Начинает {winner}')
    
    
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def step_print(name, k, counter, total):
#      print(f"{name} взял {k} конфет, у него сейчас - {counter} конфет. На столе - {total} штук.")

# counter1 = 0 
# counter2 = 0

# while total>28:
#     if flag:
#         k = input_dat(pl1)
#         counter1 += k
#         total -= k
#         flag=False
#         step_print(pl1, k, counter1, total)
#     else:
        
#         k = input_dat(pl2)
#         counter2 += k
#         total -= k
#         flag= True
#         step_print(pl2, k, counter2, total)

# if flag:
#     print(f"Выиграл {pl1}:у него {counter1 + total} конфет, {pl2} передает все свои {counter2} конфет Победителю" )
# else:
#     print(f"Выиграл {pl2}:у него {counter2 + total} конфет, {pl1} передает все свои {counter1} конфет Победителю ")

# Чертов БОТ!

pl1 = input("Введите имя первого игрока: ")
pl2 = "компьютер Вася-второй игрок"
print(pl2)
total = int(input("Введите количество конфет на столе: "))
flag = randint(0,1) 
if flag == 1:
    winner = pl1
else:
    winner = pl2
print(f'Начинает {winner}')
    
    
def input_dat(name):
   x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
   while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
   return x

def input_comp(total):
      k = randint(1,29)
       
      return k
      
      
def step_print(name, k, counter, total):
     print(f"{name} взял {k} конфет, у него сейчас - {counter} конфет. На столе - {total} штук.")

counter1 = 0 
counter2 = 0

while total>28:
    if flag:
        k = input_dat(pl1)
        counter1 += k
        total -= k
        flag=False
        step_print(pl1, k, counter1, total)
    else:
        k = input_comp(total)
        counter2 += k
        total -= k
        flag= True
        step_print(pl2, k, counter2, total)

if flag:
    print(f"Выиграл {pl1}:у него {counter1 + total} конфет, {pl2} передает все свои {counter2} конфет Победителю" )
else:
    print(f"Выиграл {pl2}:у него {counter2 + total} конфет, {pl1} передает все свои {counter1} конфет Победителю ")
