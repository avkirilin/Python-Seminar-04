# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

my_string = input('Введите текст: ')
my_dict = {}
for item in my_string:
  my_dict[item] = my_dict.get(item, 0) + 1
  print(item if my_dict[item] == 1 else f"{item}_{my_dict[item] - 1}", end= ', ')  