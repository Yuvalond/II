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

        #list of first currency
        self.spisok_valut1 = ttk.Combobox(self.tab)
        self.spisok_valut1.config(width=45)
        self.spisok_valut1.state(['readonly'])
        self.spisok_valut1["values"] = self.get_list_with_currency() #list of currency 
        self.spisok_valut1.current(0)
        self.spisok_valut1.grid(column=0, row=0 , padx=10,pady=10)

        #list of the second currency 
        self.spisok_valut2 = ttk.Combobox(self.tab)
        self.spisok_valut2.state(['readonly'])
        self.spisok_valut2.config(width=45)
        self.spisok_valut2["values"] = self.get_list_with_currency() # сюда надо залить список из валют
        self.spisok_valut2.current(4)
        self.spisok_valut2.grid(column=0, row=1 , padx=10,pady=10)

        #for inputing values 
        vcmd = (self.window.register(self.validate_input),'%P')

        self.vvod_valut = Entry(self.tab, validate="key", validatecommand= vcmd)
        self.vvod_valut.grid(column=1, row=0 , padx=10,pady=10)

        #button of conversion
        btn_convertation = Button(self.tab, text="Конвертировать", command = self.btn_convertation_func )
        btn_convertation.grid(column = 2, row = 0, padx=10,pady=10)

        #output of the conversion
        self.label_valut = Label(self.tab , text = "Результат")
        self.label_valut.grid(column = 1 , row= 1 , padx=10,pady=10)
    
    @staticmethod
    def validate_input(inp):
        pattern = r'^[0-9]*[\.]?[0-9]*$'
        if re.match(pattern, inp):
            if inp.count(".") <= 1:
                return True
        elif inp == "":
            return True
        return False

    def btn_convertation_func(self):
        value1 = str(self.spisok_valut1.get())
        value2 = str(self.spisok_valut2.get())
        #getting the value of ruble for them 
        value1 = self.get_currency_val(value1)
        value2 = self.get_currency_val(value2)
        #formula for changing from one to another 
        result = self.formula_currency(value1,value2, self)
        #bringing the result of the conversion
        self.change_label_valut(result,self)
        
    def blink(self,label , count):
        if count % 2 == 0:
            label.config(fg="black")
        else:
            label.config(fg="red")
        if count>0:
            label.after(500, self.blink, label , count-1)

    @staticmethod
    def change_label_valut(result,self):
        if isinstance(result, str):
            self.label_valut["text"] = f"{result}"
            self.blink(self.label_valut, 7)
        elif isinstance(result, int) or isinstance(result, float):
            self.label_valut["text"] = f"{result:.3f}"


    @staticmethod
    def formula_currency(value1, value2, self):
        value3 = self.vvod_valut.get()
        if not value3:
            return "Введите значение"
        else:
            result = value1 * float(value3) / value2 
            return result 
        
   
    @staticmethod
    def get_list_with_currency():
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = urllib.request.urlopen(url)
        dom = xml.dom.minidom.parseString(response.read())
        nodeArray = dom.getElementsByTagName("Valute")
        result_list = [node.getElementsByTagName("Name")[0].childNodes[0].nodeValue for node in nodeArray]
        result_list.append("Российский рубль")
        return result_list
        
    
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
                if currency_name == "Российский рубль":
                    return 1.0
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
        