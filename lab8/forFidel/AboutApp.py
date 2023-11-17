#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "about.ui"


class AboutApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("top_frame", master)
        builder.connect_callbacks(self)

    def get_top_frame(self):
        return self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    app = AboutApp(root)
    app.run()
