"""NES-Editor entry point."""

import logging
import pkg_resources
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QCommandLineOption, QCommandLineParser

import neseditor.ui.widgets as widgets
from neseditor.backend.editor import Editor


def parse(app):
    """Parse command line arguments."""

    parser = QCommandLineParser()
    parser.setApplicationDescription(
        "A character rom and nametable editor for the NES in python")
    parser.addHelpOption()
    parser.addVersionOption()

    chr_rom_option = QCommandLineOption(
        ['c', 'chr-rom'], "Path to CHR ROM file", "chr_rom")
    parser.addOption(chr_rom_option)

    log_level_option = QCommandLineOption(
        ['l', 'log-level'], "Set log level", "log_level", "INFO")
    parser.addOption(log_level_option)

    parser.process(app)

    # setup logging
    logger = logging.getLogger("neseditor")
    log_level = logging.getLevelName(parser.value(log_level_option).upper())
    logger.setLevel(log_level)

    # setup rest of the parameters
    editor_args = {
        "chr_rom_path": parser.value(chr_rom_option)
    }

    return editor_args


def main():
    """NES-Editor main method."""
    # setup Qt6 application
    app = QApplication(sys.argv)
    app.setOrganizationName("Poire-Cartable")
    app.setApplicationName("NES-Editor")
    app.setApplicationVersion(
        pkg_resources.get_distribution("neseditor").version)

    editor_args = parse(app)

    logger = logging.getLogger("neseditor")

    # editor back-end
    editor = Editor(**editor_args)

    # setup main window
    main_window = widgets.EditorWindow()
    main_window.show()

    logger.info("Starting NES-Editor")
    app.exec()
