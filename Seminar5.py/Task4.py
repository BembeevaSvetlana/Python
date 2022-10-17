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
    









    

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')

# line="a a aaaaabbbbbbcccccccccd"
# letters=line.split(" ")
# print(type(letters))

# 


    
    