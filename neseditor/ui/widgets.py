"""NES-Editor widget classes."""

import logging

from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, \
    QCheckBox, QLabel, QFileDialog, QSizePolicy
from PyQt6.QtGui import QAction, QPainter, QBrush, QColor
from PyQt6.QtCore import QRect, Qt, QSize

from neseditor.ui.layouts import MainLayout
from neseditor.backend.editor import Editor

logger = logging.getLogger("neseditor")


class EditorWindow(QMainWindow):
    """Main window of the NES-Editor."""

    def __init__(self):
        super().__init__()

        logger.info("Initializing main window")
        self.build_layout()

        self.setWindowTitle("NES-Editor")

    def build_layout(self):
        """Build the layout."""
        self.chr_rom_canvas = CHRROMCanvasWidget()
        layout = MainLayout(self.chr_rom_canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class CHRROMCanvasWidget(QWidget):
    """CHR ROM canvas widget."""

    def __init__(self):
        super().__init__()
        logger.info("Initializing CHR Canvas")

        self.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding
        )

    def sizeHint(self):
        """Hint to widget size."""
        return QSize(512, 512)

    def rectHint(self):
        """Suggest canvas rect."""
        side = min(self.size().width(), self.size().height())
        x = int((self.size().width() - side) / 2)
        y = int((self.size().height() - side) / 2)
        return QRect(x, y, side, side)

    def paintEvent(self, _event):
        """Paint (part of) the widget or entirely."""
        painter = QPainter(self)
        # simple brush painting
        brush = QBrush()
        brush.setColor(QColor('white'))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = self.rectHint()
        painter.fillRect(rect, brush)

