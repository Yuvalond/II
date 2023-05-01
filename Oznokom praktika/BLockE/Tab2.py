from Tab1 import Window, Tab1

import locale

from tkinter import *
import tkinter.ttk as ttk

import urllib.request
import xml.etree.ElementTree as ET

import datetime 

import matplotlib
import matplotlib.pyplot as plt

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
        self.currency_list.config(width=45)
        self.currency_list.grid(column=0, row=1, padx=10, pady=10)
        self.currency_list.current(0)

        #Кнопка построить график
        build_button = ttk.Button(self.tab2, text="Построить график" , command = self.build_button_command)
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

        self.show_list_week()

        radiobutton_month = ttk.Radiobutton(self.tab2, text="Месяц", variable = period_var, value = 1, command=self.show_list_month)
        radiobutton_month.grid(column=1, row=2, padx=10, pady=10)

        radiobutton_quarter = ttk.Radiobutton(self.tab2, text="Квартал", variable = period_var, value = 2, command=self.show_list_quarter)
        radiobutton_quarter.grid(column=1, row=3, padx=10, pady=10)

        radiobutton_year = ttk.Radiobutton(self.tab2, text="Год", variable = period_var, value = 3, command=self.show_list_year)
        radiobutton_year.grid(column=1, row=4, padx=10, pady=10)

        self.period_var = period_var


        #label Выбор периода
        period_label = ttk.Label(self.tab2, text="Выбор периода")
        period_label.grid(column=2, row=0, padx=10, pady=10)

        ###ЗАПУСК###

        self.tab_control.pack(expand = True, fill = BOTH)

        self.window.mainloop()#запуск
    

    #Работа кнопки построения графика
    def build_button_command(self):
                if self.handle_button_click() == 0:
                    value = (self.list_week.get())
                    list_value = self.get_date_range_for_week(value) # X
                    currency_name = self.currency_list.get()
                    list_value2 = [] #Y
                    for date in list_value:
                        list_value2.append(self.get_currency_for_date_and_name(date,currency_name))
                    self.graph(list_value,list_value2)

                elif self.handle_button_click() == 1:
                    value = (self.list_month.get())
                    list_value = self.get_date_range_for_month(value) #X
                    currency_name = self.currency_list.get()
                    list_value2 = [] #Y
                    for date in list_value:
                        list_value2.append(self.get_currency_for_date_and_name(date,currency_name))
                    self.graph(list_value,list_value2)

                elif self.handle_button_click() == 2:
                    value = (self.list_period.get())
                    list_value = self.get_mondays_of_quarter(value) #X
                    currency_name = self.currency_list.get()
                    list_value2 = [] #Y
                    for date in list_value:
                        list_value2.append(self.get_currency_for_date_and_name(date,currency_name))
                    self.graph(list_value,list_value2)

                elif self.handle_button_click() == 3:
                    value = self.list_year.get()
                    list_value = self.get_first_days_of_months(value) #X
                    currency_name = self.currency_list.get() 
                    list_value2 = [] #Y
                    for date in list_value:
                        list_value2.append(self.get_currency_for_date_and_name(date,currency_name))
                    self.graph(list_value,list_value2)
                else:
                    return NONE
                         
    def handle_button_click(self):
        selected_value = self.period_var.get()
        return selected_value

    @staticmethod
    def get_date_range_for_week(date_range):
        date_range = str(date_range)
        start_date, end_date = map(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'), date_range.split())
        delta = end_date - start_date
        dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
        return [date.strftime('%d/%m/%Y') for date in dates]
    
    @staticmethod
    def get_date_range_for_month(month_year_str):
        # преобразуем строку в объект datetime
        month_year_obj = datetime.datetime.strptime(month_year_str, "%B %Y")
        # определяем год и месяц
        year = month_year_obj.year
        month = month_year_obj.month
        # получаем первый день месяца
        first_day = datetime.date(year, month, 1)
        # получаем последний день месяца
        last_day = datetime.date(year, month, 28) + datetime.timedelta(days=4)
        last_day = last_day - datetime.timedelta(days=last_day.day)
        # создаем список дат
        dates = [(first_day + datetime.timedelta(days=i)).strftime('%d/%m/%Y') for i in range((last_day - first_day).days + 1)]
        return dates
    
    @staticmethod
    def get_currency_for_date_and_name(date,currency_name):
        #date = "06/01/2023" #самая первая рабочая дата 06/01/1993
        # формируем URL для запроса
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
        # отправляем GET-запрос
        response = urllib.request.urlopen(url)
        # парсим XML-документ
        tree = ET.parse(response)
        # получаем корневой элемент дерева
        root = tree.getroot()
        # итерируемся по всем элементам <Valute> и ищем нужную валюту
        for valute in root.iter('Valute'):
            name = valute.find('Name').text
            if name == currency_name:
                value_str = valute.find('Value').text.replace(',', '.')
                nominal_str = valute.find('Nominal').text.replace(',','.')
                #print (f"{value_str} {nominal_str}")
                return float(value_str)/float(nominal_str)
        return None




    def show_list_week(self):
        self.hide_list()
        self.list_week = ttk.Combobox(self.tab2, values = self.get_weekly_dates())
        self.list_week.config(width=20)
        self.list_week.grid(column=2, row=1,  padx=10, pady=10)
        self.list_week.current(0)
    
    @staticmethod
    def get_weekly_dates():
        dates = []
        current_date = datetime.date.today()
        for i in range(12):
            # вычисляем дату начала текущей недели
            start_date = current_date - datetime.timedelta(days=current_date.weekday())
            # вычисляем дату конца текущей недели
            end_date = start_date + datetime.timedelta(days=6)
            # добавляем даты начала и конца недели в список
            dates.append((start_date.strftime("%d/%m/%Y"), end_date.strftime("%d/%m/%Y")))
            # переходим к предыдущей неделе
            current_date -= datetime.timedelta(weeks=1)
        # возвращаем список дат
        return dates

    def show_list_month(self):
        self.hide_list()
        self.list_month = ttk.Combobox(self.tab2, value = self.get_monthly_dates())
        self.list_month.grid(column=2, row=2,  padx=10, pady=10)
        self.list_month.current(0)
    
    @staticmethod
    def get_monthly_dates():
        locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
        today = datetime.date.today()
        dates = []
        for i in range(24):
            date = today - datetime.timedelta(days=30*i)
            dates.append(date.strftime("%B %Y"))
        return dates
    
    def show_list_quarter(self):
        self.hide_list()
        self.list_period = ttk.Combobox(self.tab2, values = self.get_quarter_dates())
        self.list_period.grid(column=2, row=3,  padx=10, pady=10)
        self.list_period.current(0)

    @staticmethod
    def get_mondays_of_quarter(quarter):
        year = int(quarter.split()[-1])
        quarter_num = int(quarter.split()[0])
        if quarter_num == 1:
            start_date = datetime.datetime(year, 1, 1)
        elif quarter_num == 2:
            start_date = datetime.datetime(year, 4, 1)
        elif quarter_num == 3:
            start_date = datetime.datetime(year, 7, 1)
        elif quarter_num == 4:
            start_date = datetime.datetime(year, 10, 1)
        else:
            return []
        end_date = start_date + datetime.timedelta(days=91)
        monday_dates = []
        while start_date <= end_date:
            if start_date.weekday() == 0: # если это понедельник
                monday_dates.append(start_date.strftime('%d/%m/%Y'))
            start_date += datetime.timedelta(days=1)
        return monday_dates

    @staticmethod
    def get_quarter_dates():
        quarters = []
        for i in range(12):
            now = datetime.date.today() - datetime.timedelta(days=i*365/4)
            quarter = (now.month-1)//3 + 1
            quarters.append(str(quarter) + " квартал " + str(now.year))
        return quarters
    
    def show_list_year(self):
        self.hide_list()
        self.list_year = ttk.Combobox(self.tab2, values = self.get_years_list())
        self.list_year.grid(column=2, row=4,padx=10, pady=10)
        self.list_year.current(0)

    @staticmethod
    def get_years_list():
        now = datetime.date.today()
        years = [now.year - i for i in range(12)]
        return years
    
    @staticmethod
    def get_first_days_of_months(year):
        date_list = []
        year = int(year)
        for month in range(1, 13):
            date = datetime.datetime(year, month, 1)
            date_list.append(date.strftime('%d/%m/%Y'))
        return date_list

    def hide_list(self):
        for widget in self.tab2.winfo_children():
            if isinstance(widget, ttk.Combobox):
                if widget != self.currency_list:
                    widget.destroy()

    


    def graph(self,x,y):
        plt.rc('font', size=6)
        matplotlib.use('TkAgg')
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = self.tab2)
        self.plot_widget = canvas.get_tk_widget()
        fig.clear()
        today = datetime.datetime.now().date() # текущая дата
        valid_dates = [] # список дат, которые можно отображать
        for date_str in x:
            date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            if date <= today:
                valid_dates.append(date_str)
        valid_indices = [x.index(date_str) for date_str in valid_dates] # индексы дат, которые можно отображать
        valid_y = [y[i] for i in valid_indices] # значения y для отображаемых дат
        plt.plot(valid_dates, valid_y)
        plt.grid()
        plt.xticks(rotation=45)
        self.width = "1225"
        self.length = "725"
        self.window.geometry(f"{self.width}x{self.length}")
        self.plot_widget.grid(row=10, column=10)