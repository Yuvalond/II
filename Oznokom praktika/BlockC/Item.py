from datetime import datetime

class Item:
    #конструктор 
    def __init__(self, name, price): 
        self.name = name #свойство название 
        self.price = price #свойство цена
        self.log_event("CRE",f"Создан объект |{__name__}| класса Item")
    
    def log_event(self, key, comment): #делаем лог действия
        with open("log.txt", "a",encoding="utf-8") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{key} --- {date_time} --- {comment}\n")
            
    # def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
    #     state = {}
    #     state["name"] = self.name
    #     state["price"] = self.price
    #     return state
    
    # def __setstate__(self, state: dict):  # Как мы будем восстанавливать класс из байтов
    #     self.name = state["name"]
    #     self.price = state["price"]