# поиска первого вхождения заданной строки P длиной m символов в тексте S, 
# размером n символов, используя алгоритм ПРЯМОГО ПОИСКА СТРОКИ
# сложность O(длина текста * длина подстроки)

#посимвольное сравнение O(len_text*len_substring)
# сдвиги O(len_text)

def find_substring(text: str, substring: str):

    len_text, len_substring = len(text), len(substring) #размер строки и подстроки  
    cmp_count, shift_count = 0, 0                       #посимвольное сравнение и сдвиг подстроки

    print (f"Количество символов в тексте(с пробелами):{len(text)}")

    for i in range(len_text): # цикл по всем символам текста 

        j = 0                                   # начальное значение индекса символа подстроки
        # пока не достигнут конец подстроки и текущий символ text = текущему символу подстроки
        while j < len_substring and text[i+j] == substring[j]:
            j += 1                              # проверяем следующий символ подстроки 
            cmp_count += 1                      # счетчик сравнений +1 
        if j == len_substring:                  # нашли то что искали поиск окончен

            print(f"Количество операций посимвольного сравнения: {cmp_count}")
            print(f"Количество сдвигов подстроки: {shift_count}")
            print(f"Всего: {shift_count+cmp_count}")
            print(f'Всего теоретически : {(len_text*len_substring)+len_text}')
            return i #возвращаем индекс символа с которого начинается подстрока
        
        shift_count += 1 # количество сдвигов +1
        
    #если ничего не нашел
    print(f"Количество операций посимвольного сравнения: {cmp_count}")
    print(f"Количество сдвигов подстроки: {shift_count}")
    print(f"Всего: {shift_count+cmp_count}")
    return -1

# 100,500,1000,2000,5000
# слова для проверки по 6 символов
# сестры, рукава, слышно , именно, свежий

choice = int(input("Введите номер файла(1,2,3,4 или 5) :"))

with open(f'II\\Sortings\\6\\file{choice}.txt', "r", encoding="utf-8") as f:
    text = f.read()
    print(text[:500])
    pattern = str(input("Введите текст: "))
    index = find_substring(text, pattern)
    if index != -1:
        print(f"Подстрока найдена в позиции {index}")
    else:
        print("Подстрока не найдена")