"""

Создать класс Menu. Поля: название ресторана, адрес, список экземпляров класса Drink, список экземпляров класса Food. Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о меню (с использованием переопределения в классах Drink и Food).
    Переопределить методы получения количества пунктов меню функцией len, получения напитка/блюда по индексу,
    изменения по индексу, удаления по индексу (пусть вначале идут индексы напитков, затем горячих блюд).
    Переопределить операции + и - для добавления или удаления пункта меню. Добавить функцию создания txt-файла
    и записи всей информации в него (в том числе списков ингредиентов напитков и блюд).

"""

from Drink import Drink
from Food import Food
import pickle


class Menu(Drink,Food):
    #конструктор класса
    def __init__(self, restaurant_name: str, address: str, drinks: list, foods: list):
        self.restaurant_name = restaurant_name
        self.address = address
        self.drinks = drinks
        self.foods = foods
        self.log_event("CRE", f"Создан объект |{restaurant_name}|")

    #вывод информации о ресторане
    def __str__(self):
        self.log_event("INF",f"Печать основной информации о меню |{self.restaurant_name}|")
        menu_str = f"\nРесторан: {self.restaurant_name}\nАдрес: {self.address}\n\nНапитки:\n"
        for i in self.drinks:
            menu_str += f"{self.drinks.index(i)+1} {Drink.__str__(i)} \n"
        menu_str += "\nБлюда:\n"
        for i in self.foods:
            menu_str += f"{self.foods.index(i)+1+len(self.drinks)} {Food.__str__(i)} \n"
        return menu_str

    #Вывод количества позициЙ меню
    def __len__(self):
        self.log_event("INF",f"Печать количества позиций меню |{self.restaurant_name}|")
        return len(self.drinks) + len(self.foods)

    #получение объекта по индексу
    def __getitem__(self, index: int):
        index -= 1
        if  0 <= index < len(self.drinks):
            self.log_event("INF",f"Получен индекс позиции Food |{self.drinks[index]}| В меню |{self.restaurant_name}|")
            return print(f"{index+1} {Drink.__str__(self.drinks[index])}")
        elif 0 <= index < len(self.drinks) + len(self.foods): 
            self.log_event("INF",f"Получен индекс позиции Drink |{self.foods[index - len(self.drinks)]}| В меню |{self.restaurant_name}|")
            return print(f"{index+1} {Food.__str__(self.foods[index - len(self.drinks)])}")
        else:
            raise IndexError("Неверный индекс")
        
    #Не помню функционал 
    def __setitem__(self, index, item):
        if index < len(self.drinks):
            self.drinks[index] = item
        else:
            self.foods[index - len(self.drinks)] = item
        
    #Удалить по индексу
    def __delitem__(self, index):
        index -= 1
        if  0 <= index < len(self.drinks): # Если напиток
            del self.drinks[index]
            self.log_event("INF",f"Удален объект класса Drink из меню |{self.restaurant_name}|")
        elif 0 <= index < len(self.drinks) + len(self.foods): #если еда
            del self.foods[index - len(self.drinks)]
            self.log_event("INF",f"Удален объект класса Food из меню |{self.restaurant_name}|")
        else:
            self.log_event("INF",f"Попытка удалить объект по не существующему индексу |{index}|")
            return None


    def __add__(self, item): # +=
        if isinstance(item, Drink):
            self.log_event("INF",f"Добавлен объект |{item}| класса Drink в меню |{self.restaurant_name}|")
            self.drinks.append(item)
        elif isinstance(item, Food):
            self.log_event("INF",f"Добавлен объект |{item}| класса Food в меню |{self.restaurant_name}|")
            self.foods.append(item)
        else:
            self.log_event("ERR",f"Попытка пополнить меню не тем классом объекта {item}")
            raise TypeError("Меню можно пополнить только напитками или блюдами")
        return self

    def __sub__(self, item): # -= 
        if isinstance(item, Drink):
            self.drinks.remove(item)
        elif isinstance(item, Food):
            self.log_event("INF",f"Удален объект |{item}| класса Food из меню |{self.restaurant_name}|")
            self.foods.remove(item)
        else:
            self.log_event("ERR",f"Попытка удалить из меню не тот класс объекта |{item}|")
            raise TypeError("Из меню можно удалить только напитки или блюда")
        return self

    def save_to_file(self, file_name):
        self.log_event("INF",f"Выполнено сохранение меню |{self.restaurant_name}| в файл |{file_name}|")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(self.__str__())

