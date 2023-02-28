dict_1 = {"first":1, "second": 2,"third": 3} # создание словаря

'''
for i,j in dict_1.items ():
    print(i,j)
'''
# first 1
# second 2
# third 3

'''
print(dict_1.items()) 
'''
# dict_items([('first', 1), ('second', 2), ('third', 3)])

'''
for i in dict_1.items ():
    print(i)
'''
# ('first', 1)
# ('second', 2)
# ('third', 3)

'''
for keys, value in dict_1.items():
    print(keys, value)
'''
# first 1
# second 2
# third 3

'''
dict_1["four"] = 4
'''
# Добавление к списку новой пары ключ-значение

'''
dict_1.update({"four":4, "five":5})
'''
# Добавление к списку одной или неспкольких пар ключ-значение

'''
print(dict_1["second"])
'''
# 2

'''
print(dict_1.get("four",0))
'''
# 0
# Позволяет выводить значение по умоланию если 
# заданого ключа нет в словаре, при этом 
# программа подолжает свою работу вместо того чтобы выдать ошибку

'''
dict_1.pop ("second")
'''
# .pop позволяет удалять пары ключ-значение

'''
print(dict_1.keys())
'''
# вывод всех ключей словаря
'''

print(dict_1.values())
'''
# вывод всех значений словаря, 
# можно исользовать в цикле для перебора значений



# ВЛОЖЕНЫЕ СПИСКИ

dict_2 = {"tom":{"english": 5, "math": 5}, "Ted": {"english": 4, "math": 4}}

'''
print(dict_2["tom"])
'''
# {'english': 5, 'math': 5}

'''
for i in dict_2["tom"].items():
    print(i)
'''
# ('english', 5)
# ('math', 5)

'''
for i in dict_2["tom"].items():
    print(*i)
'''
# english 5
# math 5

'''
print(dict_2["Ted"]["math"])
'''
# 4

'''
dict_2.update({"klark":{"english":4 , "math": 5}})
print (dict_2)
'''
# {'tom': {'english': 5, 'math': 5}, 'Ted': {'english': 4, 'math': 4}, 'klark': {'english': 4, 'math': 5}}

'''
dict_2["tom"].update({"trud": 6})
print(dict_2)
'''
# {'tom': {'english': 5, 'math': 5, 'trud': 6}, 'Ted': {'english': 4, 'math': 4}}

'''
dict_2["tom"]["math"] = 4
print(dict_2)
'''
# {'tom': {'english': 5, 'math': 4}, 'Ted': {'english': 4, 'math': 4}}



# 31. Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

# Задание необходимо решать через рекурсию

'''
def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)

print(f(int(input("Введите индекс последовательности Фибоначи: "))))
'''


# 33. Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

'''
n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
print(list1)
# list1 = [int(input()) for i in range(int(input()))]

max_n = max(list1)
min_n = min(list1)

for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n

print(list1)
'''


# Задача №35.
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

'''
def prime(n):
    i = 2
    flag = True
    while i < n // 2 + 1 and flag:
        if n % i == 0:
            flag = False
        i += 1
        if flag:
            return "Да, число простое"
        return "Нет, число сложное"

print(prime(int(input("Введите число: "))))
'''


# Задача №37. Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n-1) + f' {k}'

print(f(int(input())))