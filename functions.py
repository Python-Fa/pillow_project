import settings
from effects import color_effect
from PIL import Image
from colorama import Fore
from tkinter import filedialog

def folder_without_file_name(address, split_by):
    address = address.split(split_by)[:-1]
    add_slash = ''
    for i in range(len(address)):
        add_slash += address[i] + '//'
    return add_slash[:-2]

def main_menu():
    return settings.MAIN_MENU

def insert_menu(py_file_path):
    print(Fore.WHITE, settings.INSERT)

    image_address = search()

    if len(image_address) != 2 and image_address == 'main_menu':
        status = 'main_menu'
        return status
    else:
        pos = image_address[0]
        image_address = image_address[1]
    #if status != 'main_menu':
    try:
        image = Image.open(image_address)
    except:
        print(Fore.RED, settings.ERROR[1])
        insert_menu(py_file_path)

    #print(folder_without_file_name(image_address))
    image_address = folder_without_file_name(image_address, '//')
    if pos == '':
        if image_address == py_file_path:
            pos = '-r'
        else:
            pos = '-nr'
    #print(image_address)
    #print(pos)
    try:
        return [image, image_address, pos]
    except:
        return 'back'

def export_menu(image, pos, image_address):
    print(settings.EXPORT)
    file_name = input()
    if file_name == 'back':
        status = 'main_menu'
        return status
    print(image_address)
    if pos == '-nr':
        image_address += file_name + '.jpg'
    else:
        image_address = file_name + '.jpg'
    print(image_address)
    image.save(image_address)
    print(Fore.GREEN, settings.SUCCESS)

def edit_menu(image):
    print(Fore.WHITE, settings.EDIT)
    n = input()
    if n == 'back':
        status = 'main_menu'
        return status
    #if status != 'main_menu':
    try:
        n = int(n)
    except:
        print(Fore.RED, settings.ERROR[0])
    if n == 1:
        image = color_effect.gray_scale(image)
    elif n == 2:
        image = color_effect.b_and_w(image)
    else:
        image = color_effect.negative(image)
    return [image, n]

def state_error():
    print(Fore.RED, settings.ERROR)

def search():
    print(Fore.WHITE, settings.SEARCH)
    n = input()
    pos = ''
    if n == 'back':
        status = 'main_menu'
        return status
    if n != '1' and n != '2':
        print(Fore.RED, settings.ERROR[0])
        search()
    try:
        n = int(n)
    except:
        search()

    if n == 1:
        address = filedialog.askopenfilename(
            filetypes=[
                ('PNG', '*.png'),
                ('JPEG', '*.jpeg'),
                ('JPG', '*.jpg'),
                ('All Files', '*'),
            ]
        )
        address = address.replace('/', '//')
        #pos = settings.FILE_MODE[int(input('1. -nr\n2.-r\n')) - 1]
    elif n == 2:
        #address = input().split()
        print(settings.INSERT)
        address = input()
        if address == 'back':
            status = 'main_menu'
            return status
        address = address.split()
        print(address)
        pos = address[0]
        address = address[-1]
    return [pos, address]

def show_changes(changes):
    print(len(changes), 'Change:')
    t = 1
    for change in changes:
        print(str(t) + ': ' + change)
        t += 1