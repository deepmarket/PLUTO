"""

    This module generate a table widget.

"""

from collections import OrderedDict

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem



class Table(QTableWidget):

    current_row     : int = 0
    count_row       : int = 0
    count_column    : int = 0

    """
        :param widget: parent widget
        :param count_row: max row in table
        :param header: dictionary, key is the column label, value is the column width
    """
    def __init__(self, widget, count_row:int, header:OrderedDict, **kwargs):
        super(Table, self).__init__(widget)

        self.count_row = count_row

        count_column = 0
        header_label = []
        header_width = []
        for label, width in header.items():
            header_label.append(label)
            header_width.append(width)
            count_column += 1

        # set the number of column in table
        self.count_column = count_column
        self.setColumnCount(self.count_column)

        # set horizontal header label and width
        self.setHorizontalHeaderLabels(header_label)
        for i, width in enumerate(header_width):
            self.setColumnWidth(i, width)
        self.horizontalHeader().setStretchLastSection(True)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        row_height = get_num("row_height")

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
        self.clean()

    """
        :param dat: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
    """
    def add(self, dat:list):

        if len(dat) > self.count_column:
            dat = dat[:self.count_column]

        # if enough row has been inserted to table
        # insert new row
        if self.current_row >= self.count_row:
            self.insertRow(self.current_row)

        for i in range(self.count_column):
            # insert cell
            self.setItem(self.current_row, i, QTableWidgetItem(dat[i]))

            # disable editing ip address
            i == 1 and self.item(self.current_row, i).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.item(self.current_row, i).setTextAlignment(Qt.AlignCenter)

        self.current_row += 1

    def clean(self):
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