import view, model


def start():
    choise = 1
    while True:
        choise = view.show_menu()
        match(choise):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
                
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()
                
            case 2:#record
                try:
                    phone_book = model.record_contact() 
                    print('\nКнига загружена в файл')
                except:
                    print('\nОшибка где-то')
                
            case 3:#add
                contact = view.input_contact()
                model.new_contact(contact)
                
            case 4:#change
                contact = view.input_change()
                phone_book=model.change_contact(*contact)
                            
            case 5:#delete
                id = view.input_delete()
                model.delete_contact(id)
                
            case 6:# search
               contact=view.search_contact(phone_book)
               
            case _:# exit
                return False
          
                
              
                
            

