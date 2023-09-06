# Написать функцию vowel_2_index, которая заменяет все гласные (a, e, i, o, u)
# в заданной строке на число – порядковый номер буквы в строке
#
# Примеры:
# vowel_2_index("this is my string") ==> "th3s 6s my str15ng"

import traceback


def vowel_2_index(string):
    vowels = ['a', 'e', 'i', 'o', 'u'] #создаем список  из букв которые будем заменять 
    new_string = "" # пустая строка в которую все добавляем 
    index = 1
    for char in string:
        if char.lower() in vowels:
            new_string += str(index) #замена на индекс 
        else:
            new_string += char # игнорируем просто добавляем букву 
        index += 1
    return new_string


# Тесты
try:
    assert vowel_2_index("this is my string") == "th3s 6s my str15ng"
    assert vowel_2_index("Tomorrow is going to be raining") ==  "T2m4rr7w 10s g1415ng t20 b23 r2627n29ng"
    assert vowel_2_index("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
