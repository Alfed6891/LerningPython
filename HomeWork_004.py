# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

set_numbers_one = int (input("Введите количество элементов первого множества: "))
set_numbers_two = int (input("Введите количество элементов второго множества: "))
numbers_one = []
numbers_two = []
for i in range(set_numbers_one):
    numbers_one.append(int (input("Введите элемент первого множества: " )))
for i in range(set_numbers_two):
    numbers_two.append (int (input("Введите элемент второго множества: " )))

print(numbers_one)
print(numbers_two)

list_numbers = []

for i in range (len(numbers_one)):
    for j in range (len (numbers_two)):
        if numbers_one [i] == numbers_two [j]:
            list_numbers.append(numbers_one [i])

print("В обоих списках встречаются числа: ") 
print(*list_numbers)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

number_bushes = int (input("Введите количество кустов: "))
berries = []
for i in range(number_bushes):
    berries.append(int (input(f"Введите количество ягод на кусте {i+1}: " )))

print(berries)
max = 0
for i in range (len (berries)):
    if i == 0:
        max = berries[-1] + berries [0] + berries[1]
    elif i > 0 and i < (len (berries) - 1):
        if max < berries [i-1] + berries [i] + berries [i+1]:
            max = berries [i-1] + berries [i] + berries [i+1]
    elif i == (len (berries)- 1):
        if max < berries [i-1] + berries [i] + berries [0]:
            max = berries [i-1] + berries [i] + berries [0]
print(f"Максимальное количество ягод за 1 проход: {max}")