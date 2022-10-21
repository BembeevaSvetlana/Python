import random
# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random
# mylist=[]
# for _ in range(10):
#     mylist.append(random.randint(0,50))
# print(mylist)
# # mylist=[1,2,3,4,5]
# newlist=[]
# newlist=mylist[:]


# for j in range(0,len(newlist)):
#     #print(newlist)
#     ind=random.randint(0,len(newlist)-1)
    
#     temp=newlist[j]
#     newlist[j]=newlist[ind]
#     newlist[ind]=temp
   
# print(newlist)

# Измененный код
mylist=[random.randint(0,50) for k in range(10)]
print(mylist)

def mix_el(mylist):
    newlist=mylist[:]

    for j in range(0,len(newlist)):
        ind=random.randint(0, len(newlist)-1)
    
        temp=newlist[j]
        newlist[j]=newlist[ind]
        newlist[ind]=temp 

    return newlist 
mix_list=mix_el(mylist)
print(mix_list)