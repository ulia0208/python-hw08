from os.path import exists
from writing import *
from export import export_from



def view():
    print('2-view')
    print(export_from('Phone_book.txt'))

# /////////////////////////////             RECORD

def record_info():
    info=get_info()
    writing_txt(info)


def search():
    info = export_from('Phone_book.txt').split('\n\n')

    x=input('Введите имя, фамилию или первые цифры номера телефона ')
    for i in range(len(info)):
        if x in info[i]:
            print(info[i])

info_small=[]


def change():
    
    # info_change = export_from('Phone_book.txt').split('\n\n')
    info_change=remove_spaces(export_from('Phone_book.txt').split('\n'))  
    print(info_change)
    l=input('Введите имя, фамилию или первые цифры номера телефона ')

    for i in range(len(info_change)):    

        if l in info_change[i]:
            print(f'info_change {info_change[i]}')
            k=input('1 - исправить данные, другая клавиша - главное меню ')
            if k =='1':
                m=input('Введите новые данные ')
                info_change[i]=m

            else:
                choice()


    print(info_change)

    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in range(len(info_change)):
            if (i+1)%3==0:
                data.write(f'{info_change[i]}\n\n')
            else:
                data.write(f'{info_change[i]}\n')
            
 






def remove_spaces(list_sp):
    return [i for i in list_sp if i != '']

info_clear=[]


def delete():
    info = export_from('Phone_book.txt').split('\n')
    info_clear=remove_spaces(info)  
 
    # print(info_clear)  
    x=input('Введите имя, фамилию или первые цифры номера телефона ')
    if x not in info_clear:
        print('Нет таких данных ')
        choice()


    k=info_clear.index(x)
    if (k+1)%3==0:   
        d=input(f'Удаляем {info_clear[k-2]} {info_clear[k-1]} {info_clear[k]}? Да - 1, нет - любая другая ')
        if d == '1':
            del info_clear[(k-2):(k+1)]
        else:
            choice()
    elif (k+1)%3==1:
        d=input(f'Удаляем {info_clear[k]} {info_clear[k+1]} {info_clear[k+2]}? Да - 1, нет - любая другая ')
        if d == '1':
            del info_clear[k:(k+3)]
        else:
            choice()
    elif (k+1)%3==2:
        d=input(f'Удаляем {info_clear[k-1]} {info_clear[k]} {info_clear[k+1]}? Да - 1, нет - любая другая ')
        if d == '1':
            del info_clear[(k-1):(k+4)]
        else:
            choice()
    
    # print(info_clear)

    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in range(len(info_clear)):
            if (i+1)%3==0:
                data.write(f'{info_clear[i]}\n\n')
            else:
                data.write(f'{info_clear[i]}\n')


# /////////////////////////////             CHOICE


def choice():         

    flag=input('Намите \'1\' для продолжения или что-нибудь другое для завершения ')
    if flag=='1':
        

        choice_action=input('Намите \'1\' для введения новых данных, \'2\' для просмора справочника, \'3\' для поиска по одной из характеристик, \'4\' для удаления элемента по одной из характеристик ')
        if choice_action=='1':
       
            record_info()
            
            
        if choice_action=='2':
            view()
            

        if choice_action=='3':
            search()
            
        if choice_action=='4':
            delete()
            

        if choice_action=='5':
            print('5-change')
            change()
            

        else:
            choice()
    else:
        print('Завершение')