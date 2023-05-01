from tkinter import *
import tkinter.ttk as ttk

class Window:
    def __init__(self):
        self.window = Tk() # при создании объекта класса Tk запускается итерпритарор базоваого окна приложения
        self.window.title("Конвертер Валют")
        self.width = "600"
        self.length = "250"
        self.window.resizable(False, False)
        self.tab_control = ttk.Notebook(self.window) #Управление вкладками
        self.tab_control.bind("<<NotebookTabChanged>>", self.change_resolution)

    def change_resolution(self, event):
        current_tab = self.tab_control.index("current")
        if current_tab == 0:
            self.window.geometry("600x125")
        elif current_tab == 1:
            self.window.geometry(f"{self.width}x{self.length}")

