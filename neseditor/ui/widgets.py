"""NES-Editor widget classes."""

import logging

from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QCheckBox, QLabel, QFileDialog
from PyQt6.QtGui import QAction

from neseditor.ui.layouts import MainLayout

logger = logging.getLogger("neseditor")

class MainWindow(QMainWindow):
    """Main window of the NES-Editor."""
    def __init__(self, args):
        super().__init__()
        self.args = args

        logger.info("Initializing main window")
        self.build_menu_bar()
        self.build_status_bar()
        self.build_layout()
        self.build_toolbar()

        self.setWindowTitle("NES-Editor")

    def build_menu_bar(self):
        """Build the menu bar."""
        self.menuBar()
        # menubar looks like this:
        # File           | Edit          | View          | Tools         | Help
        #   New          |   Undo
        #   Open         |   Redo
        #   Save         |
        #   Save As      |
        #   Exit

        # Actions

        # file

        # new
        new_action = QAction("New", self)
        new_action.setStatusTip("Create a new project")
        new_action.triggered.connect(self.new_project)

        # open
        open_action = QAction("Open", self)
        open_action.setStatusTip("Open a project")
        open_action.triggered.connect(self.open_project)

        # save
        save_action = QAction("Save", self)
        save_action.setStatusTip("Save current project")
        save_action.triggered.connect(self.save_project)

        # save as
        save_as_action = QAction("Save As", self)
        save_as_action.setStatusTip("Save current project as")
        save_as_action.triggered.connect(self.save_as_project)

        # exit
        exit_action = QAction("Exit", self)
        exit_action.setStatusTip("Exit NES-Editor")
        exit_action.triggered.connect(QApplication.instance().quit)

        # edit

        # undo
        undo_action = QAction("Undo", self)
        undo_action.setStatusTip("Undo last action")
        undo_action.triggered.connect(self.undo)

        # redo
        redo_action = QAction("Redo", self)
        redo_action.setStatusTip("Redo last action")
        redo_action.triggered.connect(self.redo)

        # build menubar
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(exit_action)

        edit_menu = self.menuBar().addMenu("&Edit")
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

    def build_status_bar(self):
        """Build the status bar."""
        self.statusBar()

    def build_layout(self):
        """Build the layout."""
        local_plt = LocalPalettePicker()
        global_plt = GlobalPalettePicker()
        chr_rom_canvas = CHRROMCanvas()
        nametable_canvas = NameTableCanvas()
        toggles = [
            QCheckBox("PAL/NTSC"),
        ]
        layout = MainLayout(local_plt, global_plt, chr_rom_canvas, nametable_canvas, toggles)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def build_toolbar(self):
        """Build the toolbar."""

    def new_project(self):
        """Create a new project."""
        filename, _ = QFileDialog.getSaveFileName(
            self, "New Project", "", "NES Project (*.nesproj)")
        logger.info("Creating new project: %s", filename)

    def open_project(self):
        """Open a project."""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "", "NES Project (*.nesproj)")
        logger.info("Opening project: %s", filename)

    def save_project(self):
        """Save current project."""

    def save_as_project(self):
        """Save current project as."""

    def undo(self):
        """Undo last action."""

    def redo(self):
        """Redo last action."""



class PalettePicker(QWidget):
    """Palette picker widget."""

class LocalPalettePicker(PalettePicker):
    """Local palette picker widget."""

class GlobalPalettePicker(PalettePicker):
    """Global palette picker widget."""

class CHRROMCanvas(QWidget):
    """CHR ROM canvas widget."""

class NameTableCanvas(QWidget):
    """Name table canvas widget."""
