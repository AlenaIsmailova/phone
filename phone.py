phone_book = []
path = 'file.txt'


def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)

def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<15}{contact[1]:<15}{contact[2]:<15}')

def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))

def search_contact(phone_book):
    search = input('Введите ключевой элемент: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)

def delete_file(path):
    name = input('Введите контакт: ')
    for contact in phone_book:
        if contact['name'] == name:
            print("Вы хотите удалить контакт %s (yes/no)?: " % name)
            name_del = input('> ')
            if name_del == 'yes':
               phone_book.remove(contact)
               print('Контакт удален')

def load_file(path:str)-> list:
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    return data
def save_file(path: str, data: str):
    file = open(path, 'a', encoding='UTF-8')
    file.write(data)

my_list = load_file(path)
for contact in my_list:
    new_data = contact.split(';')
    temp = {'name': new_data[0], 'phone': new_data[1], 'comment': new_data[2]}
    phone_book.append(temp)

phone_book[1]['name'] = 'Жан Клод'

file_to_save = []
for contact in phone_book:
    str_list = []
    for value in contact.values():
        str_list.append(value)
    file_to_save.append(';'.join(str_list))

save_file(path, ''.join(file_to_save))
data = load_file(path)
print(data)


while True:
    number = int(input('Выберите пункт:'))

    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            save_file(path: str, data: str)
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            load_file(path: str)
        case 6:
            search_contact(phone_book)
        case 7:
            delete_file(path)
        case 8:
            break


