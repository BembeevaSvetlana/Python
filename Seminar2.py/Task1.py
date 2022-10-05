#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number=float(input("Введите число N=")) 

num=int(number)
print(type(num))


def summa(num):
    while num>0:
        sum=0
        a=num%10
        sum+=a
        print(sum)
        num=num//10
    return sum

summa(num)
    
    
    
    
    
#     num=int([number])
# print(type(num))
# print("The floating number is : " + str(number))

# # Convert Float to digit list
# # using list comprehension + isdigit()
# res = [int(ele) for ele in str(number) if ele.isdigit()]
	
# # printing result
# print("List of floating numbers is : " + str(res))