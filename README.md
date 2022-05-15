# pyqt-foldable-item-list-widget
PyQt QListWidget which itemWidget is foldable

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-foldable-item-list-widget`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

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

Result

![python 2022-02-14 오전 11_16_52](https://user-images.githubusercontent.com/55078043/153788861-fea13fd4-475f-4112-bd0c-411a0936b479.png)

## See Also
* <a href="https://github.com/yjg30737/pyqt-foldable-window.git">pyqt-foldable-window</a>
