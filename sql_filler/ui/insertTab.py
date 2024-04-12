from tkinter import Frame, Label, Entry, Button
from sql_filler.ui.utils import get_container


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = get_container(text="Insert into DB", master=master, width=800, height=550)
        self._ui = ui
        self._values = None

    def infoBox(self, column_id, column_name, column_data):
        # jokainen on pieni laatikko josta saa klikkaamalla isomman laatikon jossa on lisäinfoa,
        # pienessä laatikossa nimi ja entry field lukumäärälle
        # label ja entry
        small_box = Frame(master=None, width=750, height=100)
        Label(master=small_box, text=column_name).grid(row=0, column=0)
        val = Entry(master=small_box)
        return val

    def columnListBox(self):
        Button(master=self.frame, text="Insert to DB", command=self.insert_values)
        values = []
        column_list = self._ui.get_insert_tab()
        for column_id, column_name, column_data in column_list:

            boxi = self.infoBox(column_id, column_name, column_data)

            values.append((column_id, boxi))

        self._values = values

    def insert_values(self):
        if self._values:
            self._ui.insert_values(self._values)
