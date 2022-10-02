#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xA=int(input("Введите координату х точки A="))
yA=int(input("Введите координату y точки A="))
xB=int(input("Введите координату х точки B="))
yB=int(input("Введите координату y точки B="))

d=float(((xB-xA)**2)+(yB-yA)**2)**0.5

print(round(d,2))


# pointA=input("Введите координаты точки А х и у через пробел=").split(" ")
# pointB=input("Введите координаты токи В х и у через пробел=").split(" ")

# print(pointA)
# print(pointB)

# d=float((int(pointB[0])-int(pointA[0]))**2+(int(pointB[1])-int(pointA[1]))**2)**0.5

# print(round(d,2))


