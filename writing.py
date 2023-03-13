
from interface import *
info=[]

def writing_txt(info):
           
    with open('phone_book.txt', 'a', encoding='utf-8') as data:
        data.write(f'{info[num-3]}\n{info[num-2]}\n{info[num-1]}\n\n')
        print(num)


num=0
def get_info():
    global num
    
    last_name=input('Введите фамилию: ')
    info.append(last_name)
    num+=1
    first_name=input('Введите имя ')
    info.append(first_name)
    num+=1
    phone_number=''
    valid = False

    while not valid:
        try:
            phone_number=input('Введите номер телефона ')
            if len(phone_number)!=7:
                print('В номере должно быть 7 цифр')
            else:
                phone_number=int(phone_number)
                valid=True
        except(ValueError):
            print('Введите только цифры')

    info.append(phone_number)
    num+=1
    print(f'info {info}')
    
    return info








    