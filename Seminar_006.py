# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                     Ввод:
# 5                         5
# 1 2 3 4 5                 1 5 1 5 1
# Вывод:                    Вывод:
# 0                         2

'''
n = int(input())
list_first = list()
for i in range(n):
    x = int(input())
    list_first.append(x)
count = 0
for i in range(1, n - 1):
    if list_first[i - 1] < list_first[i] < list_first[i + 1]:
        count += 1
print(count)
'''

'''
numbers = [5, 1, 5, 3, 6, 3, 4]
count= 0
for i in range(1, len(numbers)-1):
    if numbers[i - 1] < numbers[i] > numbers[i+1]:
        count += 1

print(count)
'''

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:               Вывод:
# 1 2 3 2 3           2


'''
import random

my_list = [1,2,3,2,3]
count = 0
i = 0
while i < len(my_list):
    j = i + 1
    while j < len(my_list):
        if my_list[i] == my_list[j]:
            print(my_list[i],my_list[j])
            my_list.pop[j]
            my_list.pop[i]
            count += 1
            i=0
            j=0
        j += 1
    i += 1
'''

# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k > 300.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).


'''
def sum_divisors (number):
    summa = 0
    for i in range (1, number//2 + 1):
        if number % i == 0:
            summa += i
    return summa

number_k = int(input("Введите число к: "))
for i in range (1, number_k):
    for j in range (i+1, number_k):
        if sum_divisors(j) == i and sum_divisors(i) == j and i != j:
            print(i,j)
'''

def div_list(number: int)-> dict:
    div_dict = {}
    for j in range (1, number):
        summa_div = 0
        for i in range (1, j):
            if j % i == 0:
                summa_div += i
        div_dict[j] = summa_div
    return div_dict

number = int (input("Введите предел: "))

div_dict = div_list(number)

for i in range (1, number):
    for j in range (i, number):
        if i == div_dict.get(j) and j == div_dict.get(i) and i != j:
            print (i,j)