# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

from itertools import count


path= r"C:\Users\Светлана\Desktop\Python\Seminar5.py\Task4_file.txt"
path2=r'C:\Users\Светлана\Desktop\Python\Seminar5.py\Task4_file2.txt'

with open(path, 'r') as data:
    code=data.readline()
    print('\n'+code)
    

countA=0
countB=0
countC=0
countD=0
countJ=0
    
for i in code:
    for letter in i:
        if letter=="a":
          countA+=1 
        if letter=='b':
            countB+=1
        if letter=='c':
            countC+=1
        if letter=='d':
            countD+=1
        if letter=='j':
            countJ+=1
        real_code = str(countA)+'a'+str(countB)+"b"+str(countC)+"c"+str(countD)+"d"+str(countJ)+'j'    

print(real_code +'\n') 
with open(path, 'a', encoding= 'UTF-8') as data:
    data.writelines('\n'+ real_code)
    

with open(path2, 'r') as data:
    code=data.readline()
    print(code)

str_numb = ''
str_lett = ''
for i in code:
    if i.isalpha():
        str_lett += i
        str_numb += ' '
        #print(str_lett,str_numb)
    else:
        str_numb += i
    list_num = list(map(int, str_numb.split()))
    #print(list_num)
result=(''.join([l*n for l,n in zip(str_lett, list_num)]))
 
print(result+'\n')
 
with open(path2, 'a', encoding= 'UTF-8') as data:
    data.writelines('\n'+result)
    









    







    
    
