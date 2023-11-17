import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from KilometersMiles import KilometersMilesApp
from MilestoKilometers import MilestokilometersApp


class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add first calculator
        kilos_to_miles_app = KilometersMilesApp(self.__mainwindow)
        self.__main_notebook.add(kilos_to_miles_app.get_top_frame(), text="Kilometers to Miles")

        # Add second calculator
        miles_to_kilos_app = MilestokilometersApp(self.__mainwindow)
        self.__main_notebook.add(miles_to_kilos_app.get_top_frame(), text="Miles to Kilometers")

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()
