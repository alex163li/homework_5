# 2-Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def candy_picker(player, candy_pick):
    i = int(input(f"{player}, введите количество конфет, которое возьмете от 1 до {candy_pick}: "))
    while i < 1 or i > candy_pick:
        i = int(input(f"Конфет должно быть от 1 до {candy_pick}: "))
    return i

def step_printer(player_name, candy, candy_counter, candy_value):
    print(f"{player_name} взял {candy}шт, у него всего {candy_counter}шт конфет. На столе осталось {candy_value} конфет")

def player_pick(n_num):
    player = input('Кто будет играть?\nВведите имя Игрока или "Бот"\n')
    if player != 'Бот':
        return player
    else: return f'Бот{n_num}'

def last_candy_check(max_c,max_c_pick):
    if ((max_c%max_c_pick)-1) == 0:
        return 1
    else: return ((max_c%max_c_pick)-1)

player1 = player_pick(1)
player2 = player_pick(2)
player1_bank = 0 
player2_bank = 0
max_candy = int(input("Всего количество конфет на столе: "))
max_candy_pick = int(input("Сколько конфет можно взять за раз: "))
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while max_candy > max_candy_pick:
    if flag:
        if (player1 != 'Бот1'):                             
            stash = candy_picker(player1, max_candy_pick)
        else: 
            if (max_candy < max_candy_pick*2):              
                stash = last_candy_check(max_candy,max_candy_pick)
            else: stash = randint(1,max_candy_pick+1)  
        player1_bank += stash
        max_candy -= stash
        flag = False
        step_printer(player1, stash, player1_bank, max_candy)
    else:
        if (player2 != 'Бот2'):
            stash = candy_picker(player2, max_candy_pick)
        else: 
            if (max_candy < max_candy_pick*2):
                stash = last_candy_check(max_candy,max_candy_pick)
            else: stash = randint(1,max_candy_pick+1)   
        player2_bank += stash
        max_candy -= stash
        flag = True
        step_printer(player2, stash, player2_bank, max_candy)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")