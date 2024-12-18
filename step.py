from random import randint
from time import sleep
from heplers import *
from data import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Магазин
4 - Получить валюту
5 - Показать инвентарь
6 - Информация об игроке
7 - Информация о текущем противнике
8 - Бой с тенью (с самим собой)
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 5:
            break
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
        earn()
    elif action == '5':
        display_inventory()
    elif action == '6':
        display_player()
    elif action == '7':
        display_enemy(current_enemy)
    elif action == '8':
        fight_to_me()
print("Спасибо за игру!")


        
            


