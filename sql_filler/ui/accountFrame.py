from tkinter import Label, Entry, Button, Frame, EW
from sql_filler.ui.utils import get_container


class AccountFrame:
    def __init__(self, master=None, ui=None, data_service=None):
        self.frame = get_container(master=master)
        self._connection_tab_position_params = {'row': 1, 'column': 1, 'sticky': 'EW'}

        self._database_username_entry = None
        self._database_dbname_entry = None

        self._unconnected_tab = self.unconnected_tab()
        self._unconnected_tab.grid(self._connection_tab_position_params)
        self._connected_tab = None

        self._ui = ui

    def button_action_connect(self):
        self._ui.connect()

    def connect(self):
        self._connected_tab = self.connected_tab()
        self._unconnected_tab.grid_forget()
        self._connected_tab.grid(self._connection_tab_position_params)

    def button_action_disconnect(self):
        """
        Passes through signal to UI
        :return:
        """
        self._ui.disconnect()

    def disconnect(self):
        """
        Disconnect chores in AccountFrame. UI calls this.
        :return:
        """
        self._connected_tab.destroy()
        self._unconnected_tab.grid(self._connection_tab_position_params)

    def unconnected_tab(self, master=None) -> Frame:
        container = self.get_tab()
        Label(master=container, text="Username").grid(row=1, column=0)
        self._database_username_entry = Entry(master=container)
        self._database_username_entry.grid(row=2, column=0)

        Label(master=container, text="Database name").grid(row=3, column=0)
        self._database_dbname_entry = Entry(master=container)
        self._database_dbname_entry.grid(row=4, column=0)

        Button(master=container, text="Connect", command=self.button_action_connect).grid(row=1, column=1, rowspan=4,
                                                                                          sticky=EW)
        return container

    def connected_tab(self, master=None) -> Frame:
        container = self.get_tab(text='Connected to')
        dbname, username = self._ui.get_connection_credentials()
        Label(master=container, text=f'{username}@{dbname}').grid(row=1, column=0, sticky=EW)

        Button(master=container, text="Disconnect", command=self.button_action_disconnect).grid(row=2, column=0,
                                                                                                sticky=EW)
        return container

    def get_tab(self, **kwargs):
        container = get_container(master=self.frame, width=400, height=300, **kwargs)
        container.grid(self._connection_tab_position_params, sticky=EW)
        return container


    def get_entry_box_values(self):
        if self._database_dbname_entry and self._database_username_entry:
            return self._database_dbname_entry.get(), self._database_username_entry.get()
        return None, None

    def grid(self, row, column, sticky):
        """
        Passthrough method for ui->self.frame
        :param row:
        :param column:
        :param sticky:
        :return:
        """
        self.frame.grid(row=row, column=column, sticky=sticky)

