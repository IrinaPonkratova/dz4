# Напишите функцию принимающую на вход только
# ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def func(**kwargs)->dict[str, str]:
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[value] = key
    return my_dict

print(func(one = 1, two = 2, three = 3, four = 4, five = 5, text = 'Hi'))