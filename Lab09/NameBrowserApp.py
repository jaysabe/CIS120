#!/usr/bin/python3
import tkinter as tk
import pathlib
import pygubu
from Name import Name
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "name_browser.ui"


class NameBrowserApp:
    def __init__(self, master=None):
        self.build_ui(master)
        self.setup_type_combo()
        self.setup_show_treeview()

    def build_ui(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        self.year_entry = builder.get_object("year_entry", master)
        self.min_votes_entry = builder.get_object("min_votes_entry", master)
        self.show_treeview = builder.get_object("show_treeview", master)
        self.type_combo = builder.get_object("type_combo", master)
        self.gender = None
        builder.import_variables(self, ['gender'])

        builder.connect_callbacks(self)

    def setup_type_combo(self):
        self.type_combo["values"] = ["tvSeries", "tvEpisode", "movie", "videoGame"]
        self.type_combo.current(0)

    def setup_show_treeview(self):
        tree = self.show_treeview

        # config will be list or tuple
        tree.configure(columns=["Title", "Type", "Year", "Rating", "Votes"])

        tree.heading("Title", text="Title", anchor=tk.W)
        tree.heading("Type", text="Type")
        tree.heading("Year", text="Year")
        tree.heading("Rating", text="Rating")
        tree.heading("Votes", text="Votes")

        tree.column("Title", width=400)
        tree.column("Type", anchor=tk.CENTER)
        tree.column("Year", anchor=tk.CENTER)
        tree.column("Rating", anchor=tk.CENTER)
        tree.column("Votes", anchor=tk.CENTER)

    def run(self):
        self.mainwindow.mainloop()

    # @staticmethod
    # def show_to_tuple():
    #     return (show.get_name()...)
    # query - SELETE DISTINCT <name_type>
    # FROM <column name>


    def search(self):
        print("Search dis bish")
        for child in self.show_treeview.get_children():
            self.show_treeview.delete(child)
        year = int(self.year_entry.get())
        min_votes = int(self.min_votes_entry.get())
        type = self.type_combo.get()
        shows = Show.fetch_names(type, year, min_votes)
        for show in shows:
            self.show_treeview.insert("", "end", values=self.show_to_tuple(show))
        print(type, year, min_votes)
        print(self.gender.get())


if __name__ == "__main__":
    app = NameBrowserApp()
    app.run()
