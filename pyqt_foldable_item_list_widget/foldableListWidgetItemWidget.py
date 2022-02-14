from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStackedWidget, QSizePolicy


class FoldableListWidgetItemWidget(QWidget):
    foldToggled = pyqtSignal(int)

    def __init__(self, idx, folded_item, unfolded_item):
        super().__init__()
        self.__idx = idx
        self.__foldedItem = folded_item
        self.__unfoldedItem = unfolded_item
        self.__initUi()

    def __initUi(self):
        self.__arrowBtn = QPushButton()
        self.__arrowBtn.setIcon(QIcon('ico/down-arrow.svg'))

        self.__arrowBtn.setCheckable(True)
        self.__arrowBtn.toggled.connect(self.__foldToggled)
        self.__arrowBtn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.__leftWidget = QStackedWidget()
        self.__leftWidget.addWidget(self.__foldedItem)
        self.__leftWidget.addWidget(self.__unfoldedItem)

        lay = QHBoxLayout()
        lay.addWidget(self.__leftWidget)
        lay.addWidget(self.__arrowBtn)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        icon_width = self.__arrowBtn.iconSize().width()
        margin_for_icon = icon_width // 4
        self.setStyleSheet(f'QWidget {{ border: 0; }} '
                           f'QPushButton {{ padding-left: {margin_for_icon}; '
                                          f'padding-right: {margin_for_icon}; }}')
        self.setLayout(lay)

        self.setMinimumHeight(self.__arrowBtn.sizeHint().height())

    def __foldToggled(self, f):
        item = ''
        if f:
            self.__arrowBtn.setIcon(QIcon('ico/up-arrow.svg'))
            item = self.__unfoldedItem
        else:
            self.__arrowBtn.setIcon(QIcon('ico/down-arrow.svg'))
            item = self.__foldedItem
        self.__leftWidget.setCurrentWidget(item)
        self.setFixedHeight(item.sizeHint().height())
        self.foldToggled.emit(self.__idx)

