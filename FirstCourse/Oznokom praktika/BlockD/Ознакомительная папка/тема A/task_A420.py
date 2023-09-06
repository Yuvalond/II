# Написать функцию change(first, second), которая возвращает количество
# перестановок между двумя элементами, которые нужно совершить в первом списке,
# чтобы получить второй
#
# Пример:
# ([4, 3, 2, 5, 1], [1, 2, 5, 3, 4]) ==> 3



import traceback


def change(first, second):
    i = 0
    change = 0
    while first != second:
        if first[i] != second[i]:
            index = second.index(first[i])
            first[i],first[index] = first[index], first[i]
            change += 1
        i += 1
    return change


# Тесты
try:
    assert change([1, 2], [2, 1]) == 1
    assert change([4, 3, 2, 1], [2, 1, 4, 3]) == 2
    assert change([3, 6, 1, 5, 4, 2], [1, 5, 4, 2, 3, 6]) == 4
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
