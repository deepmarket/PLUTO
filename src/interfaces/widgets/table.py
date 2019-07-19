from collections import OrderedDict

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem


class Table(QTableWidget):
    """
    This file provide a table widget.
    """

    current_row     : int = 0
    count_row       : int = 0
    count_column    : int = 0

    def __init__(self, widget, count_row:int, header:OrderedDict, **kwargs):
        """
        :param widget: parent widget
        :param count_row: max row in table
        :param header: dictionary, key is the column label, value is the column width
        """
        super(Table, self).__init__(widget)

        self.count_row = count_row

        # set the number of column in table
        self.count_column = len(header)
        self.setColumnCount(self.count_column)

        # set horizontal header label and width
        self.setHorizontalHeaderLabels(header.keys())
        for i, width in enumerate(header.values()):
            self.setColumnWidth(i, width)
        self.horizontalHeader().setStretchLastSection(True)

        # Lambda func grab input args
        get_param = lambda x : kwargs.get(x)

        row_height = get_param("row_height")
        name = get_param("name")
        if_vertical = get_param("if_vertical")

        name and self.setObjectName(name)

        # set row height
        row_height = row_height if row_height else 40
        self.verticalHeader().setDefaultSectionSize(row_height)

        if_vertical is not True and self.verticalHeader().setVisible(False)

         # selected entire row
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        # single rows selected each time
        self.setSelectionMode(QAbstractItemView.SingleSelection)

        # alternating coloring
        self.setAlternatingRowColors(True)

        # hide grid line
        self.setShowGrid(False)

        # initially fill table with empty line
        self.reset()

    def add(self, dat:list):
        """
        :param dat: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
        """

        if len(dat) > self.count_column:
            dat = dat[:self.count_column]

        # if enough row has been inserted to table
        # insert new row
        if self.current_row >= self.count_row:
            self.insertRow(self.current_row)

        for i in range(self.count_column):
            # insert cell
            self.setItem(self.current_row, i, QTableWidgetItem(dat[i]))

            # disable editing
            self.item(self.current_row, i).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            # set cell align
            self.item(self.current_row, i).setTextAlignment(Qt.AlignCenter)

        self.current_row += 1

    def reset(self):
        self.current_row = 0

        # remove all existing row
        while self.rowCount():
            self.removeRow(0)

        # insert empty row
        for i in range(self.count_row):
            self.insertRow(i)
            # for j in
            for j in range(self.count_column):
                # insert empty cell
                self.setItem(i, j, QTableWidgetItem(""))

                # disable interaction
                self.item(i, j).setFlags(Qt.NoItemFlags)

    def if_select(self):
        model = self.selectionModel()

        if model.hasSelection():
            row = model.selectedRows()[0].row()

            text = self.get_cell(row, self.count_column-1)
            return row if text is not -1 else None
        else:
            return -1

    def get_cell(self, row:int, column:int):
        return self.item(row, column).text()

    # TODO, when implement edit feature, cont work on this function
    def allow_edit(self, row:int):
        pass
