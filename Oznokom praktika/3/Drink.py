"""
Создать производный от Item класс Drink. Новые поля: объем напитка, раздел меню, состав напитка
    (словарь вида название ингредиента: количество). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления и удаления ингредиента, форматированной печати состава напитка. Переопределить
    метод преобразования в строку для печати основной информации (название, раздел меню, объем, цена).
    
"""
from Item import Item

class Drink(Item): #производный класс от item
    def __init__(self, name : str, price: float, menu_category: str, volume: int, ingredients = {}):
        super().__init__(name, price) #вызов родительского конструктора с price и name
        self.volume = volume #объем напитка
        self.menu_category = menu_category #раздел меню
        self.ingredients = ingredients #состав напитка

    def add_ingredient(self, name: str, quantity: float = None): #добавить ингредиент
        if name in self.ingredients: #увеличивает количство ингредиента если он есть
            self.ingredients[name] += quantity
        else: # если нет , то создает ингредиент 
            self.ingredients[name] = quantity

    def remove_ingredient(self, name: str, quantity: float): #удалить ингредиент 
        if name in self.ingredients: #если этот ингридент существует
            if self.ingredients[name] <= quantity: # если кол-во ингр. <= кол-ву удалений
                del self.ingredients[name] # удаляем ингридиент
            else:
                self.ingredients[name] -= quantity #удаляем кол-во ингредиентов

    def print_ingredients(self): #напечатать состав напитка 
        print(f"Ингредиенты: {self.name}")
        for name, quantity in self.ingredients.items():
            print(f"{name}: {quantity} мл")
    
    def __str__(self): #метод преобразования в строку для печати основной информации
        return f"{self.name} - {self.menu_category} - {self.volume} мл - {self.price:.2f} Р"
    
    def change_all(self,name: str, price: int, volume: int, menu_category: str, ingredients: dict ):
        self.name = name
        self.price = price
        self.volume = volume #объем напитка
        self.menu_category = menu_category #раздел меню
        self.ingredients = ingredients #состав напитка
