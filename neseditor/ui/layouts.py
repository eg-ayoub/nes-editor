"""NES-Editor layout class."""

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QLabel


# layout looks like this (roughly):
# +------+-----------------+-----------------+
# |Local | CHR ROM (Tiles) |NameTable(Opt)   |
# |Plt   |                 |                 |
# |      |                 |                 |
# |      |                 |                 |
# +------+                 |                 |
# |Global|                 |                 |
# |Plt   |                 |                 |
# |      |                 |-----------------|
# |      |                 |Toggles          |
# +------+-----------------+-----------------+

class MainLayout(QHBoxLayout):
    """Main layout of the NES-Editor."""
    def __init__(self, local_plt, global_plt, chr_rom_canvas, nametable_canvas, toggles):
        super().__init__()

        local_plt = TitledLayout("Local Palette", local_plt)
        global_plt = TitledLayout("Global Palette", global_plt)
        chr_rom_canvas = TitledLayout("CHR ROM (Tiles)", chr_rom_canvas)
        nametable_canvas = TitledLayout("NameTable (Optional)", nametable_canvas)

        palettes_layout = PalettesLayout(local_plt, global_plt)
        self.addLayout(palettes_layout)
        palettes_layout.initialize()

        self.addLayout(chr_rom_canvas)
        chr_rom_canvas.initialize()

        right_most_layout = RightMostLayout(nametable_canvas, toggles)
        self.addLayout(right_most_layout)
        right_most_layout.initialize()

class TitledLayout(QVBoxLayout):
    """Titled widget."""
    def __init__(self, title, widget):
        super().__init__()
        self.title = title
        self.widget = widget

    def initialize(self):
        """Initialize the layout after adding it to parent."""
        self.addWidget(QLabel(self.title))
        self.addWidget(self.widget)

class PalettesLayout(QVBoxLayout):
    """Palettes layout of the NES-Editor."""
    def __init__(self, local_plt, global_plt):
        super().__init__()
        self.local_plt = local_plt
        self.global_plt = global_plt

    def initialize(self):
        """Initialize the layout after adding it to parent."""
        self.addLayout(self.local_plt)
        self.local_plt.initialize()

        self.addLayout(self.global_plt)
        self.global_plt.initialize()

class RightMostLayout(QVBoxLayout):
    """Right most layout of the NES-Editor."""
    def __init__(self, nametable_canvas, toggles):
        super().__init__()
        self.nametable_canvas = nametable_canvas
        self.toggles = toggles

    def initialize(self):
        """Initialize the layout after adding it to parent."""
        self.addLayout(self.nametable_canvas)
        self.nametable_canvas.initialize()

        toggles_layout = TogglesLayout(self.toggles)
        self.addLayout(toggles_layout)
        toggles_layout.initialize()

class TogglesLayout(QGridLayout):
    """Toggles layout of the NES-Editor."""
    def __init__(self, toggles):
        super().__init__()
        self.toggles = toggles

    def initialize(self):
        """Initialize the layout after adding it to parent."""
        # fill in the layout from arbitrary list of toggles
        col_count = len(self.toggles) // 3 + 1
        for i, toggle in enumerate(self.toggles):
            self.addWidget(toggle, i // col_count, i % col_count)
