# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

number_coins = int (input("Введите количество монет: "))
eagle_side = 0
tails_side = 0
for i in range(number_coins):
    coins_side  = int (input("Введите как лежит монета, где 1 - орел и 0 - решка: " ))
    if coins_side == 1:
        eagle_side += 1
    if coins_side == 0:
        tails_side += 1
if eagle_side > tails_side:
    print (f"Монет с решкой меньше, всего {tails_side}, переверните их!")
else:
    print (f"Монет с орлом меньше, всего {eagle_side}, преверните их!")




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int (input ('Введите сумму чисел: '))
multiple = int (input ('Введите произведение чисел: '))
number_x = 0
number_y = 0
for i in range (1000):
    for j in range(1000):
        if i + j == sum and i * j == multiple:
            number_x = i
            number_y = j
print (number_x, number_y)




# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

add_number = int (input ('Введите максимальне число: '))
x_multiple = 1
while x_multiple <= add_number:
    print(x_multiple, end= ' ')
    x_multiple=x_multiple*2

# Второй вариант решения
# add_number = int (input ('Введите максимальне число: '))
# x_= 1
# for i in range (1, add_number):
#     if x < add_number:
#         print(x) 
#         x=2**i
       
        

