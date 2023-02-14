# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
"""
list_input = [1, 1, 2, 0, -1, 3, 4, 4]
print (len(set(list_input))) #  set преобразует список в множество, а len выводит его длинну
"""

# 2 решение
'''
list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
result_list = list()
for i in list_1:
    if i not in result_list:
        result_list.append(i)
print(result_list)
print(len(result_list))
'''


# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
'''
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
list_result = list()

for i in range(k):
list_result.append(list_1[len(list_1) - k + i])

for i in range(len(list_1) - k):
list_result.append(list_1[i])
print(list_result)
'''

'''
# 2 вариант решения
lst = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    lst.insert(0, lst.pop(-1)) # функция pop удаляет последенее значение на данной итерации и возвращает в insert, 
                                # которая записывает это значение в нулевую позицию.
print(lst)
'''



# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

print("Original List: ",L)

u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)
'''

'''
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
list_2 = list()
for i in list_1:
    for j in i:
         list_2.append(i[j])

list_result = list()
for i in list_2:
    if i not in list_result:
        list_result.append(i)
print(list_result)
'''

# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

'''
n = [0, -1, 5, 2, 3]
cnt = 0
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        cnt += 1
print(cnt)
'''


n = [0, -1, 5, 2, 3]
cnt = 0
for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        cnt += 1
print(cnt)
