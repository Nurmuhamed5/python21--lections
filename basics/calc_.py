# a = float(input('Введите первое число: '))
# b = float(input('Введите первое число: '))
# c = input('Выберите операцию из следующих:' '+' '-' '*' '/' '%' '**' '//')

# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     print(a / b)
# elif c == '%':
#     print(a % b)
# elif c == '**':
#     print(a ** b)
# elif c == '//':
#     print(a // b)
import random
name = input('Ваше имя: ')
wish = input('Хотите сыграть?: ')
random_value = random.randint(0,100)
popytki = 0
print("Загадано число от 0 до 100. Попробуйте отгадать за 10 попыток")
for i in range(1,11):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print("Многовато будет")
    elif choice < random_value:
        print("Маловато будет")
    else:
        print(f"Точно! Количество попыток - {i}")
        break
    popytki += 1
    print(f"Осталось попыток {10-popytki}")
if popytki >= 10:
    print(f"Попытки закончились! Было загадано {random_value}")

#  20.06.2022 task 1
# a = input('Введите значение: ')
# b = input('Введите значение: ')
# try:
#   a = int(a)
#   b = int(b)
# except: 
#   a = str(a)
#   b = str(b)
# print(a+b)
