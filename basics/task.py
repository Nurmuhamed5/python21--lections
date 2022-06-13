# name = input('введите имя: ')
# surname = input('введите фамилию: ')
# age = int(input('возраст: '))
# # name[::а]
# print(surname.join('*'))


# data = input('Введите имя, фамилию и возраст через пробел:\n').split()
# name = data[0]
# last_name = data[1]
# age = data[-1]
# name = name.lower().replace('a', '')
# last_name = '*'.join(list(last_name))
# print((name + last_name) * int(age)) 
"""

#1
string = input('Введите строку: ').lower()
a = string.count('a')
o = string.count('o')
i = string.count('i')
e = string.count('e')
u = string.count('u')
y = string.count('y')
print(f'Вашей строке насчитано {a+o+i+e+u+y}')


#2
x = str(input('Введите строку:'))
y = list(x)
a = y.count('a')
i = y.count('i')
o = y.count('o')
u = y.count('u')
e = y.count('e')
r = y.count('A')
t = y.count('I')
b = y.count('O')
c = y.count('U')
k = y.count('E')
sum = a + i + o + u + e + r + t + b + c + k
strr = 'В вашей строке насчитано {} гласных букв'
print(strr.format(sum))

#3
user = str(input('Введите юзернейм:'))
swap = user.swapcase()
q = len(swap)
qq = (q // 2)
hh = swap[:qq]
rr = swap[qq:]
liist = swap.split(hh)
liist2 = swap.split(rr)
ll = ''.join(liist)
ll2 = ''.join(liist2)
print(ll2, '&', ll, '$', sep='')

#3

username = input('Введите юзернейм: ')
center = int(len(user)/2)
new_username = username[:center] + '&' + username[center:]
password = new_username.swapcase()
print(f'Вам сгенерирован пароль: {password}')


a = int(input())
b = int(input())
if a%b == 0:
    print("%d делится на %d" % (a,b))
else:
    print("%d не делится на %d" % (a,b))
    print("Остаток: %d" % (a%b))
print("Частное: %d" % (a//b))
"""

string1 = 'Makers'
string2 = 'Bootcamp'



т