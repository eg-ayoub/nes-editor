"""NES-Editor layout class."""

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from PyQt6.QtCore import Qt


# layout looks like this (roughly):
# +-----------------+
# | CHR ROM (Tiles) |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# +-----------------+

class MainLayout(QHBoxLayout):
    """Main layout of the NES-Editor."""
    def __init__(self, chr_rom_canvas):
        super().__init__()

        chr_rom_canvas = TitledLayout("CHR ROM (Tiles)", chr_rom_canvas)

        self.addLayout(chr_rom_canvas)
        chr_rom_canvas.initialize()

class TitledLayout(QVBoxLayout):
    """Titled widget."""
    def __init__(self, title, widget):
        super().__init__()
        self.title = title
        self.widget = widget

    def initialize(self):
        """Initialize the layout after adding it to parent."""
        # TODO alignment for label
        self.addWidget(QLabel(self.title))
        self.addWidget(self.widget)

