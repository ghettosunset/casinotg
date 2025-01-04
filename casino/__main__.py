import os

libs = {'telebot': 'pyTelegramBotAPI', 'requests': 'requests'}


for i in libs:
    try:
        exec(f"import {i}")
    except:
        print(f'Библиотека {i} не установлена. Установка...')
        os.system(f'pip install {libs[i]}')

print("Все библиотеки установлены. Проверяю конфиг...")

with open('config.py', 'r+') as f:
    if f.read() == '':
        print('Конфиг пуст...')
        f.write(f'TOKEN=\"{input("Введите токен бота: ")}\"\nMAIN=\"{input("Введите ID основного канала: ")}\"\nAPI=\"{input("Введите CryptoBot API: ")}\"')
    else:
        print("Конфиг заполнен. Запускаю скрипт.")
os.system('python casino.py')
        
