#                                               Задача 1
# my_list = [12, None, -77, 'True', True, 9.5]
#
#
# def my_type():
#     for el in range(len(my_list)):
#         print(type(my_list[el]))
#     return
#
#
# my_type()

#                                               Задача 2
# el_count = int(input("Введите количество элементов списка "))
# my_list = []
# i = 0
# el = 0
# while i < el_count:
#     my_list.append(input("Введите следующее значение списка "))
#     i += 1
#
# for elem in range(int(len(my_list) / 2)):
#     my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
#     el += 2
# print(my_list)

#                                              Задача 3
# seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
# easons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
# month = int(input("Введите месяц по номеру "))
# if month == 1 or month == 12 or month == 2:
#     print(seasons_dict.get(1))
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#     print("Такого месяца не существует")

#                                               Задача 4
# my_str = input("введите строку ")
# my_word = []
# num = 1
# for el in range(my_str.count(' ') + 1):
#     my_word = my_str.split()
#     if len(str(my_word)) <= 10:
#         print(f" {num} {my_word [el]}")
#         num += 1
#     else:
#         print(f" {num} {my_word [el] [0:10]}")
#         num += 1

#                                               Задача 5
# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число (111 - выход) "))
# while digit != 111:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit > my_list[el + 1]:
#             my_list.insert(el + 1, digit)
# print(f"текущий список - {my_list}")
# digit = int(input("Введите число "))

#                                           Задача 6
goods = []
features = {'Название': '', 'Стоимость': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Стоимость': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода напишите 'Q', чтобы продолжить нажмите 'Enter', для анализа данных напишите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущий анализ \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите характеристики "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
