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
        """
        Wrapper object for QFrame.
        :param: widget: required. the parent widget for the frame.
        :param: height: optional. given fixed height to the frame.
        :param: width: optional. given fixed width to the frame.
        :param: name: optional. object name for the frame.
        :param: stylesheet: apply a stylesheet for the frame.
        """
        super(Frame, self).__init__(*args)

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)

        # Set property if given
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)
