def show_menu():
   print('\nМ Е Н Ю:')
   print("0. Показать все контакты")
   print("1. Открыть файл с контактами")
   print("2. Записать файл с контактами")
   print("3. Добавить контакт")
   print("4. Изменить контакт")
   print("5. Удалить контакт")
   print("6. Поиск по контактам")
   print("8. В Ы Х О Д\n ")
   
   choise=int(input("Выберите пункт меню: "))
   return choise

def show_phone_book(phone_book):
    if len(phone_book)<1:
        print("Телефонная книга пуста")
    else:
        for id,item in enumerate(phone_book):
            print(id,*item)
            
def input_path():
    path=input("введите имя файла: ")
    return path

def input_contact():
    name_contact=input("Введите ФИО контакта: ")
    phone_contact=input("Введите номер телефона контакта: ")
    comment_contact=input("Введите комментарий: ")
    contact=(name_contact, phone_contact, comment_contact)
    return (contact)

def input_change():
    id = int(input("введите номер контакта: "))
    print( " Что изменить? ")
    choise = input ("0 - ФИО, 1 - номер телефона, 2 - комментарии, 3 - Отмена -  ")
    value = input("Введите изменения: ")
    return(id, choise,value)

def input_delete():
    id = int(input("введите номер контакта, чтобы удалить: "))
    return(id)
    

def search_contact(phone_book):
    search=input('Введите какой-нибудь символ для поиска: ')
    found=False
    for contact in phone_book:
        for item in contact:
            if search.lower() in item.lower():
                print(*contact)
                found=True
    if not found:print("Ничего не найдено!")  
 

