"""

    This module provide a group box widget

"""

from PyQt5.QtWidgets import QGroupBox, QWidget


class GroupBox(QGroupBox):

    def __init__(self, widget:QWidget, *args, **kwargs):
        super(GroupBox, self).__init__(widget, *args)

        # Lambda func grab input args
        get_param = lambda x: kwargs.get(x)

        name = get_param("name")
        align = get_param("align")

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)
