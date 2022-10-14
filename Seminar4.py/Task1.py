import math

# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# 

d=float(input("нужно ввести вещественное число  d от 0.1 до 0.0000000001(шаблон): "))

π =math.pi
print(π)

def digit_after_dot_counter(d):
    count = 0
    div = 1
    while True:
        if not(d*div == int(d*div)):
            count += 1
            div *= 10
        else: 
           break   
    print(count)
    return count

    
print(round(math.pi,digit_after_dot_counter(d)))



# counter=0

# for i in range (0,d):
#    while d!=".":
#         if d *=10:
#             counter+=1
#         else:
#             break
# print(counter)