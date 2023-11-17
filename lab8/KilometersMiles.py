# Fidel Kilometers to Miles Calculator
import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH,  "KilometersMiles.ui")


class KilometersMilesApp:
    MILES_TO_KILOMETERS = 0.62137119

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("root_frame", master)
        self.kilometer_entry = builder.get_object("kilometer_entry", master)
        self.miles_variable = builder.get_variable("miles_variable")
        builder.connect_callbacks(self)


    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

    def calculate_kilometers(self):
        try:
            kilometers = float(self.kilometer_entry.get())
            miles = kilometers * self.MILES_TO_KILOMETERS
            self.miles_variable.set("{:.2f} miles".format(miles))

        except ValueError:
            mb.showerror("Error","Please enter valid value")
            return


if __name__ == "__main__":
    root = tk.tk()
    app = KilometersMilesApp(root)
    app.run()

