from Window import Window

from tkinter import *
import tkinter.ttk as ttk

import urllib.request
import xml.dom.minidom

import xml.etree.ElementTree as ET

import re

class Tab1(Window):            
    def __init__(self):
        super().__init__()
        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text = "Калькулятор валют")

        #список валюты верх
        self.spisok_valut1 = ttk.Combobox(self.tab)
        self.spisok_valut1.config(width=45)
        self.spisok_valut1["values"] = self.get_list_with_currency() #список валют
        self.spisok_valut1.current(0)
        self.spisok_valut1.grid(column=0, row=0 , padx=10,pady=10)

        #список валюты низ
        self.spisok_valut2 = ttk.Combobox(self.tab)
        self.spisok_valut2.config(width=45)
        self.spisok_valut2["values"] = self.get_list_with_currency() # сюда надо залить список из валют
        self.spisok_valut2.current(1)
        self.spisok_valut2.grid(column=0, row=1 , padx=10,pady=10)

        #Окно ввода кол-ва валюты
        vcmd = (self.window.register(self.validate_input),'%P')

        self.vvod_valut = Entry(self.tab, validate="key", validatecommand= vcmd)
        self.vvod_valut.grid(column=1, row=0 , padx=10,pady=10)

        #кнопка конвертировать 
        btn_convertation = Button(self.tab, text="Конвертировать", command = self.btn_convertation_func )
        btn_convertation.grid(column = 2, row = 0, padx=10,pady=10)

        #вывод переведенной валюты
        self.label_valut = Label(self.tab , text = "Переведенное")
        self.label_valut.grid(column = 1 , row= 1 , padx=10,pady=10)
    
    #ФУНКЦИЯ ПРОВЕРКИ ВВОДА (ЦИФРЫ и только 1 точка)
    @staticmethod
    def validate_input(inp):
        pattern = r'^[0-9]*[\.]?[0-9]*$'
        if re.match(pattern, inp):
            if inp.count(".") <= 1:
                return True
        elif inp == "":
            return True
        return False

    #ФУНКЦИЯ КНОПКИ КОНВЕРТАЦИИ
    def btn_convertation_func(self):
        value1 = str(self.spisok_valut1.get())
        value2 = str(self.spisok_valut2.get())
        #получить их рублевые значения 
        value1 = self.get_currency_val(value1)
        value2 = self.get_currency_val(value2)
        # #формула нахождения валюты из 1 в другую 
        result = self.formula_currency(value1,value2, self)
        # #вернуть в label_valut
        self.change_label_valut(result,self)
        

    @staticmethod
    def change_label_valut(result,self):
        if isinstance(result, str):
            self.label_valut["text"] = f"{result}"
        elif isinstance(result, int) or isinstance(result, float):
            self.label_valut["text"] = f"{result:.3f}"

    # ФОРМУЛА НАХОЖДЕНИЯ 1 ВАЛЮТЫ ОТ ДРУГОЙ ПО ОТНОШЕНИЮ К РУБЛЮ
    @staticmethod
    def formula_currency(value1, value2, self):
        value3 = self.vvod_valut.get()
        if not value3:
            return "Введите значение"
        else:
            result = value1 * float(value3) / value2 
            return result 
        
    #ПОЛУЧЕНИЕ ЛИСТА С СТРАНАМИ НА СЕГОДНЯШНИЙ ДЕНЬ     
    @staticmethod
    def get_list_with_currency():
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = urllib.request.urlopen(url)
        dom = xml.dom.minidom.parseString(response.read())
        nodeArray = dom.getElementsByTagName("Valute")
        result_list = [node.getElementsByTagName("Name")[0].childNodes[0].nodeValue for node in nodeArray]
        return result_list
        
    #ПО НАЗВАНИЮ ВАЛЮТЫ ВОЗВРАЩАЕМ ЕЕ ЗНАЧЕНИЕ
    
    @staticmethod
    def get_currency_val(currency_name):
        try:
            url = f"https://www.cbr.ru/scripts/XML_daily.asp"
            with urllib.request.urlopen(url) as response:
                xml_data = response.read()
            root = ET.fromstring(xml_data)

            currency_element = None
            for elem in root.findall(".//Valute"):
                name_elem = elem.find("Name")
                if name_elem is not None and currency_name in name_elem.text:
                    currency_element = elem
                    break

            if currency_element is None:
                return None

            value_elem = currency_element.find("Value")
            nominal_elem = currency_element.find("Nominal")

            if value_elem is None or nominal_elem is None:
                return None

            value = float(value_elem.text.replace(",", "."))
            nominal = float(nominal_elem.text)

            return value / nominal
        except Exception as e:
            print(f"An error occurred: {e}")
            return None