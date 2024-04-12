from tkinter import Frame, Menu, ttk, Button, NSEW, Label, Text
from sql_filler.ui.utils import get_container


def get_main_frame(master):
    container = get_container(text="SQL connection", master=master, width=800, height=600)

    menu_bar(container).grid(row=0, column=0)
    return container


def menu_bar(master=None):
    tab_switcher = ttk.Notebook(master=master)

    tab_switcher.add(table_info_tab(master=master), text='table info')
    tab_switcher.add(insert_tab(master=master), text='insert data')
    tab_switcher.add(db_info_tab(master=master), text='db info')
    # tab_switcher.add(tab, text='text')
    tab_switcher.add(settings_tab(master=master), text='settings')

    # lisätään yks ehkä hidden tab varaamaan tila? leikitään ton propagaten kanssa?

    # tab_switcher.add(get_container(text='size', master=master, width=800, height=550))
    return tab_switcher


def settings_tab(master=None):
    container = get_container(text="Settings", master=master, width=800, height=550)
    Button(master=container, text='settings button').grid(row=1, column=0)
    return container


def insert_tab(master=None):
    # luonnostelma, mitään ei ole vielä toteutettu
    container = get_container(text="Insert into DB", master=master, width=800, height=550)
    # columns = self._ui.get_columns()
    columns = []
    for col in columns:

        pass
    return container


def table_info_tab(master=None):
    container = get_container(text="Table info", master=master, width=800, height=550)
    tb = Text(master=container, width=80, height=20)
    tb.grid(row=2, column=0)
    return container


def db_info_tab(master=None):
    container = get_container(text="DB Info", master=master, width=800, height=550)
    return container


def selected_table_label(master=None):
    return Label(master=master, text=f'Selected table {master}')
