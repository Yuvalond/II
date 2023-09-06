# Написать функцию anagram_difference, на вход которой дан список слов и которая
# определяет сколько всего букв нужно удалить из всех слов, чтобы они все являлись
# анаграммами (каждое слово получалось перестановкой букв другого)
#
# Пример:
#assert anagram_difference(["abc", "ab", "a"]) == 3
# anagram_difference["hello", "hola", "allo"] ==> 7 (["lo", "ol", "lo"]

import traceback

def anagram_difference(words):
    total_diff = 0
    for char in set(''.join(words)): # проходимся по каждому уникальному символу всех слов(set)
        char_count = [word.count(char) for word in words] # количество вхождений символа в каждом слове 
        total_diff += sum([abs(count - sum(char_count) // len(words)) for count in char_count]) #количество удалений, 
                                                                                                #необходимых для того, чтобы превратить 
                                                                                                #все слова в анаграммы.
    return total_diff                            
# Тесты
try:
    assert anagram_difference(["abc", "ab", "a"]) == 3
    assert anagram_difference(["hello", "hola", "allo"]) == 7
    assert anagram_difference(["cat", "dog", "mouse"]) == 11
    assert anagram_difference(["mouse", "house", "hose", "host"]) == 10
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
