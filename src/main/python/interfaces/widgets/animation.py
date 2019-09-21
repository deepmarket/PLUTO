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
        Wrapper object for QPropertyAnimation.
        :param widget: required. defined the target widget for this animation
        :param duration: optional. how long the animation runs
        :param prop: optional. animation type, it can be any kind of widget properties. reference can be found here, https://doc.qt.io/archives/qt-4.8/qwidget.html
        :param start_x: optional. target's x-axis value when animation starts
        :param start_y: optional. target's y-axis value when animation starts
        :param end_x: optional. target's x-axis value when animation starts
        :param end_y: optional. target's y-axis value when animation starts
        :param start_width: optional. target's width when animation starts
        :param start_height: optional. target's height when animation starts
        :param end_width: optional. target's width when animation ends
        :param end_height: optional. target's height when animation ends
        """

        super(Animation, self).__init__(widget)

        # set target widget to apply this animation, which is the widget who own it
        self.setTargetObject(widget)

        # Set animation type
        prop and self.setPropertyName(prop)

        # Set duration
        self.setDuration(duration)

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
        :param start_x: optional. target's x-axis value when animation starts
        :param start_y: optional. target's y-axis value when animation starts
        :param end_x: optional. target's x-axis value when animation starts
        :param end_y: optional. target's y-axis value when animation starts
        :param duration: optional. how long the animation runs
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
