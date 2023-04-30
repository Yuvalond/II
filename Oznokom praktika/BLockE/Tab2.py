from Tab1 import Window, Tab1

from tkinter import *
import tkinter.ttk as ttk

import urllib.request
import xml.dom.minidom

import datetime
import re

class Tab2(Tab1, Window):
    def __init__(self):
        super().__init__()
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text = "Динамика курса")

        #label Валюта
        currency_label = ttk.Label(self.tab2, text="Валюта")
        currency_label.grid(column=0, row=0, padx=10, pady=10)

        #Выбор самой валюты список
        self.currency_list = ttk.Combobox(self.tab2, values=self.get_list_with_currency())
        self.currency_list.grid(column=0, row=1, padx=10, pady=10)

        #Кнопка построить график
        build_button = ttk.Button(self.tab2, text="Построить график")
        build_button.grid(column=0, row=4, padx=10, pady=10)

        #label Период
        period_label = ttk.Label(self.tab2, text="Период")
        period_label.grid(column=1, row=0, padx=10, pady=10)

        #Radiobutton Неделя, Месяц, Квартал, Год 
        #значение      (0)    (1)    (2)     (4)
        period_var = IntVar()
        period_var.set(0)


        radiobutton_week = ttk.Radiobutton(self.tab2, text="Неделя" , variable = period_var , value = 0, command = self.show_list_week)
        radiobutton_week.grab_current()
        radiobutton_week.grid(column=1, row=1, padx=10, pady=10)

        radiobutton_month = ttk.Radiobutton(self.tab2, text="Месяц", variable = period_var, value = 1, command=self.show_list_month)
        radiobutton_month.grid(column=1, row=2, padx=10, pady=10)

        radiobutton_quarter = ttk.Radiobutton(self.tab2, text="Квартал", variable = period_var, value = 2, command=self.show_list_period)
        radiobutton_quarter.grid(column=1, row=3, padx=10, pady=10)

        radiobutton_year = ttk.Radiobutton(self.tab2, text="Год", variable = period_var, value = 3, command=self.show_list_year)
        radiobutton_year.grid(column=1, row=4, padx=10, pady=10)


        #label Выбор периода
        period_label = ttk.Label(self.tab2, text="Выбор периода")
        period_label.grid(column=2, row=0, padx=10, pady=10)

        self.tab_control.pack(expand = True, fill = BOTH)

        self.window.mainloop()#запуск
    
    def show_list_week(self):
        self.hide_list()
        list_week = ttk.Combobox(self.tab2)
        list_week.grid(column=2, row=1,  padx=10, pady=10)

    def show_list_month(self):
        self.hide_list()
        list_month = ttk.Combobox(self.tab2)
        list_month.grid(column=2, row=2,  padx=10, pady=10)

    def show_list_period(self):
        self.hide_list()
        list_period = ttk.Combobox(self.tab2)
        list_period.grid(column=2, row=3,  padx=10, pady=10)

    def show_list_year(self):
        self.hide_list()
        list_year = ttk.Combobox(self.tab2)
        list_year.grid(column=2, row=4,padx=10, pady=10)

    def hide_list(self): # пока что не работает надо как то получить имя currency_list что бы его исключить из проверки 
        for widget in self.tab2.winfo_children():
            if isinstance(widget, ttk.Combobox):
                if widget.cget('values') != self.currency_list:
                    widget.destroy()