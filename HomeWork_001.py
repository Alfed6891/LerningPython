# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


firstThreeNumber = int (input('Ведиете трехзначное число: '))
oneNumber = firstThreeNumber // 100
twoNumber = (firstThreeNumber //10) % 10
threeNumber = firstThreeNumber % 10
resultSum =  print ('Сумма цифр этого числа: ', oneNumber + twoNumber + threeNumber)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

Total= int (input('Ведиете сколько всего корабликов сделали друзья: '))

x = Total / 6

petya = int (x)
sereja = int (x)
katya = (sereja + petya)*2

print(f'Петя сделал {petya} к. катя сделала {katya} к. Серёжа сдедлал {sereja} к.')



# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket = int (input('Ведиете номер вашего билета: '))
firstThreeNumber = ticket // 1000
lastThreeNumber = ticket % 1000
oneNumber = firstThreeNumber // 100
twoNumber = (firstThreeNumber //10) % 10
threeNumber = firstThreeNumber % 10
fourNumber = lastThreeNumber // 100
fiveNumber = (lastThreeNumber // 10) % 10
sixNumber = lastThreeNumber % 10

resultSumFirstNumber = oneNumber + twoNumber + threeNumber
resultSumLastNumber = fourNumber + fiveNumber + sixNumber

if resultSumFirstNumber == resultSumLastNumber:
    print ("Этот билет счастливый")
else:
    print ("Этот билет несчастливый")



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int (input('Введите ширину шоколадки: '))
m = int (input('Введите длинну шоколадки: '))
k = int (input('Введите какую часть хотите отломить: '))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print ('Такую часть можно отломить от шоколадки')
else:
    print ('Не получится!')