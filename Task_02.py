# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте

my_string = input("Введите текст: ")
list_string = my_string.lower().split()
print(my_string)
print(list_string)
my_dict = {}
count = 0
for item in list_string:                           # решение циклом через формирование списка
  my_dict[item] = my_dict.get(item, 0) + 1
  count += 1  
print(count)

key = my_dict.keys()                               # решение через нахождение ключей и их
print(len(key) + 1)                                # подсчет

print(len(list_string))                            # решение через определине длины множества