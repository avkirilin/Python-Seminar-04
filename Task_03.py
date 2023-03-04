# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random
lenght_array = int(input("Введите кол-во значений в списке: "))
my_list = [random.randint(999, 10000) for _ in range(lenght_array)]
number_to_exclude = input("Введите число: ")
print(type(number_to_exclude))
print(my_list)
my_list2 = []
for value in my_list:
    element = str(value)
    if number_to_exclude in element:
        element = element.replace(number_to_exclude, '')
    my_list2.append(element)
print(my_list2)
my_list3 = []
for value in my_list2:
    sum_num = sum([int(element) for element in value])
    while sum_num > 9:
        sum_num = sum([int(element) for element in str(sum_num)])
    my_list3.append(sum_num)
print(my_list3)
print(set(my_list3))
