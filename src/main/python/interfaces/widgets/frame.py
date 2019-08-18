"""

    This module generate a simple placeholder frame without any contents.

"""

from PyQt5.QtWidgets import QFrame


class Frame(QFrame):
    def __init__(
        self,
        *args,
        height: int = 0,
        width: int = 0,
        name: str = "",
        stylesheet=None,
        **kwargs
    ):
        super(Frame, self).__init__(*args)

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)

        # Set property if given
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)
