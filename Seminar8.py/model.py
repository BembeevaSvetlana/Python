from ast import Delete
import controller

phone_book = []
path = 'Seminar8.py\data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path 
    path += file

def open_file():
    global path 
    global phone_book
    with open (path, 'r', encoding ='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))
    

def record_contact():
    with open(path,'w',encoding='UTF-8') as data: 
        new_phone_book = []
        for contact in  phone_book:
            new_phone_book.append(';'.join(contact))
            #print(new_phone_book)
        new_phone_book.sort()
        data.write('\n'.join(new_phone_book))
      
     
def change_contact(id, choise, value):
    global phone_book
    phone_book [int(id)][int(choise)] = value
    return value

def delete_contact(id):
    global phone_book
    del phone_book[id]
    return phone_book



    

    
    

    
        
 


    


    


