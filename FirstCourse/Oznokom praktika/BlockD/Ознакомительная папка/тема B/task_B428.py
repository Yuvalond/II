"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;+
- непустые строки добавить в список;+
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы); +
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель; +
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;+
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

import string 
import re

def wiki_function(file_path):
    # Открываем файл и читая построчно добавляем непустые строки в список
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Удаляем из каждой строки все символы, кроме латинских букв и пробелов
    translator = str.maketrans('', '', string.digits + string.punctuation)
    lines = [line.translate(translator) for line in lines]

    # Объединяем все строки из списка в одну строку с пробелом в качестве разделителя
    text = ' '.join(lines)

    # Создаем словарь для подсчета количества каждого слова
    word_counts = {}
    for word in text.split(): #это что бы он слова учитывал а не буквы
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    # Сортируем слова по количеству появлений в порядке убывания 
    sorted_words = sorted(word_counts.items(),key = lambda x: x[1], reverse=True)

    # Заменяем наиболее популярные слова на "PYTHON"
    popular_words = [word[0] for word in sorted_words[:10]]
    for word in popular_words:
        pattern = r"\b" + re.escape(word) + r"\b" #обозначаем целое слово 
        text = re.sub(pattern, 'PYTHON', text)

    # popular_words = [word[0] for word in sorted_words[:10]]
    # for word in popular_words:
    #     text = text.replace(word, 'PYTHON')

    # Записываем текст в новый файл
    with open('wiki2_0.txt','w') as f:
        line_length = 0
        for word in text.split():
            word_length = len(word)
            if line_length + word_length + 1 > 100: #Обработка переноса 
                f.write('\n')
                line_length = 0
            if line_length == 0:
                f.write(word)
                line_length += word_length
            else:
                f.write(' ' + word)
                line_length += word_length + 1

    # Выводим наиболее популярные слова в форматированном виде
    print('топ 10 популярных слов:')
    for i, word_count in enumerate(sorted_words[:10], 1):
        word, count = word_count
        print(f'{i} место --- {word} --- {count} раз(а)')

    return text


# Вызов функции
wiki_function("wiki.txt")