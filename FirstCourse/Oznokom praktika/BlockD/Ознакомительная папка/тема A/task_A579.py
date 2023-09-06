# Создать список (каталог мобильных приложений), состоящий из словарей (приложение). Словари должны содержать как минимум 5 полей
# (например, номер, название, рейтинг...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# apps = [{"id" : 123456, "title" : "Google Play", "rating" : 4.9,...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех приложениях;
# – вывода информации о приложении по введенному с клавиатуры номеру;
# – вывода количества приложений, с оценкой выше введённого;
# – обновлении всей информации о приложении по введенному номеру;
# – удалении приложения по номеру.
# Провести тестирование функций.

def action1(apps): # – вывода информации о всех приложениях;
    for i in range(len(apps)):
        print (apps[i])

def action2(apps): # – вывода информации о приложении по введенному с клавиатуры номеру;
    num = int(input())
    print(apps[num - 1])

def action3(apps): # – вывода количества приложений, с оценкой выше введённого
    counter = 0
    rate = int(input())
    for i in apps:
        if i["rating"] >= rate:
            counter += 1
    print(counter)

def action4(apps): # – обновлении всей информации о приложении по введенному номеру;
    num = int(input())
    apps[num]["id"] = input("enter id: ")
    apps[num]["title"] = input("enter title: ")
    apps[num]["description"] = input("enter description: ")
    apps[num]["rating"] = input("enter rating: ")
    apps[num]["last Feedback"] = input("enter last feedback: ")
    action1(apps)
    return apps

def action5(apps): # – удалении приложения по номеру.
    num = int(input())
    del apps[num - 1]
    action1(apps)
    return apps

apps = [{"id" : 1 , "title" : "Google Play", "description" : "Applications for downloading other applications" ,"rating" : 4.9 , "last Feedback" : "Good app" },
        {"id" : 2 , "title" : "Microsoft 365 (Office)", "description": "One application for documents, tables, presentations, PDF and other files. ", "rating" : 4.8, "last Feedback" : "Comfortable!"},
        {"id" : 3 , "title" : "Yandex translator", "description" : "Applications for tranlating texts and photos" ,"rating" : 4.5 , "last Feedback" : "I like the app" },
        {"id" : 4 , "title" : "Super Auto Pats", "description" : "Gather the strongest team of animals and fight with your friends" ,"rating" : 4.2 , "last feedback" : "The game freezes" },
        {"id" : 5 , "title" : "Subway Surfers", "description" : "Help Jake escape from Inspector and his dog" ,"rating" : 4.5 , "last Feedback" : "Not for me" },
        {"id" : 6 , "title" : "Twitter", "description" : "Find out what's happening in the world right now" ,"rating" : 3.0 , "last Feedback" : "Poor app" },
        {"id" : 7 , "title" : "Instagram", "description" : "communicate in the language of photos" ,"rating" : 3.0 , "last Feedback" : "After the update, app lags" },
        {"id" : 8 , "title" : "CapCut", "description" : "Edit videos with music and effects" ,"rating" : 4.3 , "last Feedback" : "There are few effects , but this is a amazing application" },
        {"id" : 9 , "title" : "Aviasales", "description" : "Search for cheap tickets in the CIS" ,"rating" : 4.6 , "last Feedback" : "A hotel? Trivago!" },
        {"id" : 10 , "title" : "Discord", "description" : "Connect with people all over the world" ,"rating" : 4.5 , "last Feedback" : "I always use it" },]

# while 1:
#     print('0 - Выйти из цикла','1 – вывода информации о всех приложениях;' ,
# "2 – вывода информации о приложении по введенному с клавиатуры номеру;",
# "3 – вывода количества приложений, чей рейтинг выше чем введенный рейтинг;",
# "4 – обновлении всей информации о приложении по введенному номеру;",
# "5 - удалении приложения по номеру.",sep ="\n")
#     k = input()
#     if k == "0":
#         break 
#     exec('action'+k+"(apps)")

action1(apps)







# getinfo(apps) #вывода информации о всех приложениях;+

# print("enter number") #вывода информации о приложении по введенному с клавиатуры номеру;
# getinfo_about(apps, int(input()))

# print("enter rating") # – вывода количества приложений, с оценкой выше введённого;
# rating(apps, int(input())) 

# print("enter number") # – обновлении всей информации о приложении по введенному номеру;
# num = int(input())-1
# update(apps,num)

# print("enter number") # – удалении приложения по номеру.
# apps = erase(apps, int(input()))

        

