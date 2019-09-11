from PyQt5.QtCore import QPropertyAnimation, QByteArray, QRect
from PyQt5.QtWidgets import QWidget


class Animation(QPropertyAnimation):
    def __init__(
        self,
        widget: QWidget,
        duration: int = 0,
        prop: QByteArray = None,
        start_x: int = 0,
        start_y: int = 0,
        end_x: int = 0,
        end_y: int = 0,
        start_width: int = 0,
        start_height: int = 0,
        end_width: int = 0,
        end_height: int = 0,
    ):
        """
        :param widget: required. defined the parent widget for this animation
        :param duration: how long the animation runs
        :param prop: animation type, it can be any kind of widget properties. 
                     reference can be found here, https://doc.qt.io/archives/qt-4.8/qwidget.html
        """

        super(Animation, self).__init__(widget)

        # Set animation type
        prop and self.setPropertyName(prop)

        # Set duration
        duration and self.setDuration(duration)

        # Set start value
        start_width = start_width if start_width else widget.width()
        start_height = start_height if start_height else widget.height()

        self.setStartValue(QRect(start_x, start_y, start_width, start_height))

        # set end value
        end_width = end_width if end_width else widget.width()
        end_height = end_height if end_height else widget.height()

        self.setEndValue(QRect(end_x, end_y, end_width, end_height))


class MoveAnimation(Animation):
    def __init__(
        self,
        widget: QWidget,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration: int = 230,
    ):
        """
        :param widget: required. defined the parent widget for this animation
        :param start_x: widget's position at x-axis when start the animation
        :param start_y: widget's position at y-axis when start the animation
        :param end_x: widget's position at x-axis when end the animation
        :param end_y: widget's position at y-axis when end the animation
        :param duration: optional, how long the animation runs
        """
        super(MoveAnimation, self).__init__(
            widget,
            duration=duration,
            prop=b"geometry",
            start_x=start_x,
            start_y=start_y,
            end_x=end_x,
            end_y=end_y,
        )
