# pyqt-foldable-item-list-widget
PyQt QListWidget which itemWidget is foldable

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-foldable-item-list-widget.git --upgrade```

## Included Package
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a> // to show the library's icon from main module

## Example
Code Sample
```python
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QTextEdit, QWidget, QApplication
from pyqt_foldable_item_list_widget import FoldableListWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.__add)
        self.__foldableListWidget = FoldableListWidget()
        lay = QVBoxLayout()
        lay.addWidget(addBtn)
        lay.addWidget(self.__foldableListWidget)
        self.setLayout(lay)

    def __add(self):
        foldedItem = QLineEdit()
        foldedItem.setPlaceholderText('Input...')
        unfoldedItem = QTextEdit()
        unfoldedItem.setPlaceholderText('Input...')
        self.__foldableListWidget.setFoldableListWidgetItem(foldedItem, unfoldedItem)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec_()
```
