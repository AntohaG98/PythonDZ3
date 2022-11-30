#                             Задача 3
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Для красоты будем чистить консоль при каждом запуске
import os
os.system('clear')

num_list = [1.1, 1.2, 3.1, 5.1, 10.01, 6, 5]
print("Исходный массив: ", num_list)
maximum = 0
minimum = 1
for i in num_list:
    if type(i) == float:
        if i % 1 < minimum:
            minimum = round(i % 1, 2)
        if i % 1 > maximum:
            maximum = round(i % 1, 2)
print("Ответ: ", maximum - minimum)