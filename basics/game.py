# import random
# name = input('Ваше имя: ')
# wish = input('Хотите сыграть?: ')
# random_value = random.randint(0,100)
# popytki = 0
# print("Загадано число от 0 до 100. Попробуйте отгадать за 10 попыток")
# for i in range(1,11):
#     choice = int(input("Введите число: "))
#     if choice > random_value:
#         print("Многовато будет")
#     elif choice < random_value:
#         print("Маловато будет")
#     else:
#         print(f"Точно! Количество попыток - {i}")
#         break
#     popytki += 1
#     print(f"Осталось попыток {10-popytki}")
# if popytki >= 10:
#     print(f"Попытки закончились! Было загадано {random_value}")


import random
words = 'книга свет учеба код словарь ноутбук мышь стол стул терпение мучение игра вода нервы'.split()
rand = random.choice(words)
words = '*' (len(words))
guess = input('Введите букву: ')

def randomword(wordslist):
    
    popytki = 7

    while popytki > 0:
        for letter in rand:
            if letter
