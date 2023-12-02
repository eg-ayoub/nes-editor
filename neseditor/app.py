"""NES-Editor entry point."""

import logging
import pkg_resources
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QCommandLineOption, QCommandLineParser

import neseditor.ui.widgets as widgets

def parse(app):
    """Parse command line arguments."""

    parser = QCommandLineParser()
    parser.setApplicationDescription("A character rom and nametable editor for the NES in python")
    parser.addHelpOption()
    parser.addVersionOption()

    chr_rom_option = QCommandLineOption(['c', 'chr-rom'], "Path to CHR ROM file", "chr_rom")
    parser.addOption(chr_rom_option)

    log_level_option = QCommandLineOption(['l', 'log-level'], "Set log level", "log_level", "INFO")
    parser.addOption(log_level_option)

    parser.process(app)

    # setup logging
    logger = logging.getLogger("neseditor")
    log_level = logging.getLevelName(parser.value(log_level_option).upper())
    logger.setLevel(log_level)

    # setup rest of the parameters
    args = {
        "chr_rom": parser.value(chr_rom_option)
    }

    return args

def main():
    """NES-Editor main method."""
    # setup Qt6 application
    app = QApplication(sys.argv)
    app.setOrganizationName("Poire-Cartable")
    app.setApplicationName("NES-Editor")
    app.setApplicationVersion(pkg_resources.get_distribution("neseditor").version)

    args = parse(app)

    logger = logging.getLogger("neseditor")

    # setup main window
    main_window = widgets.MainWindow(args)
    main_window.show()

    logger.info("Starting NES-Editor")
    app.exec()
