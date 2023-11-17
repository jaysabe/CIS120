# by Jay Abegglen -- Miles to Kilometers
import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "milestokilometers.ui")


class MilestokilometersApp:
    RATE = 1.60934

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object(
            "milestokilometers_top_frame", master)

        self.miles_entry_variable = None
        self.kilometers_entry_variable = None
        builder.import_variables(
            self, ['miles_entry_variable', 'kilometers_entry_variable'])

        builder.connect_callbacks(self)

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

    def calculate_miles_to_kilometers(self):

        try:
            miles = float(self.miles_entry_variable.get())
            miles_to_kilometers = miles * self.RATE
            self.kilometers_entry_variable.set("{:.2f}".format(miles_to_kilometers))
        except ValueError:
            mb.showerror("Error in Calculator!", "Miles must be a decimal number!")
            return


if __name__ == "__main__":
    root = tk.Tk()
    app = MilestokilometersApp()
    app.run()

