from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from pyqt_foldable_item_list_widget.foldableListWidgetItemWidget import FoldableListWidgetItemWidget


class FoldableListWidget(QListWidget):
    def __init__(self):
        super().__init__()

    def setFoldableListWidgetItem(self, folded_item, unfolded_item):
        item = QListWidgetItem(self)
        widget = FoldableListWidgetItemWidget(self.count()-1, folded_item, unfolded_item)
        widget.foldToggled.connect(self.__foldToggled)
        self.setItemWidget(item, widget)

    def __foldToggled(self, idx):
        item = self.item(idx)
        widget_to_resize = self.itemWidget(item)
        widget_to_resize.setFixedHeight(widget_to_resize.height())
        item.setSizeHint(QSize(widget_to_resize.width(), widget_to_resize.height()))
