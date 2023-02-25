'''
list_1 = ["H","e","l","l","o"]
print (' '.join(list_1))
'''
# Функция (''.join(name)) включает тип разделителя в кавычках 
# который вставляется в промежутке между значениями списка

'''
string_1 = "Hello world Moscow Name"
print (string_1.split())
'''
# По умолчанию в скобках функции .split используется пробел
# который можно заменть на любой разделитель, указав его в 
# кавычках

'''
list_1 = []
for i in string_1:
    list_1.append(i)
'''
# Таким образом можно разделить строку на отдельные символы
# хнанящиеся в списке list_1


# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''
text = input().split()
text1 = {}
for i in text:
    if i in text1:
        text1[i] += 1
        print(f'{i}_{text1[i]}', end=" ")
    else:
        print(i, end=' ')
        text1[i] = 0
'''

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

'''
print (len(set(input().upper().split())))
'''
'''
text = input().split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))
'''

