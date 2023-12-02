"""This module contains classes that hold the data of the project
   and tools used to serialize and deserialize it."""

import json

from enum import Enum

class ColorFormat(Enum):
    """ColorFormat is an enum that represents the color format of the project."""
    FMT_2C02 = 0
    FMT_2C07 = 1

class CHRData():
    """CHRData is a class that holds the CHR data of the project."""
    def __init__(self) -> None:
        self.data = bytearray(0x2000)

    def load(self, data):
        """Load the CHR data from a str."""
        self.data = bytearray.fromhex(data)

    def save(self):
        """Save the CHR data to a str."""
        return self.data.hex(sep=' ')

class NMTData():
    """NMTData is a class that holds the NMT data of the project."""
    def __init__(self) -> None:
        self.data = bytearray(0x400)

    def load(self, data):
        """Load the NMT data from a str."""
        self.data = bytearray.fromhex(data)

    def save(self):
        """Save the NMT data to a str."""
        return self.data.hex(sep=' ')

class PaletteData():
    """PaletteData is a class that holds the palette data of the project."""
    def __init__(self) -> None:
        self.data = bytearray(0x20)

    def load(self, data):
        """Load the palette data from a str."""
        self.data = bytearray.fromhex(data)

    def save(self):
        """Save the palette data to a str."""
        # TODO: make sure memory locations are mirrored correctly
        return self.data.hex(sep=' ')

class ProjectState():
    """ProjectState is a class that holds the state of the project."""
    def __init__(self) -> None:
        # by default, load empty CHR and NMT data
        self.chr_data = CHRData()
        self.nmt_data = NMTData()
        # and a default palette
        self.palette_data = PaletteData()
        # and a default color format (NTSC)
        self.color_format = ColorFormat.FMT_2C02

    def load(self, filename):
        """Load a project from a file."""
        required_keys = ["chr_data", "nmt_data", "palette_data", "color_format"]
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key in required_keys:
                if key not in data.keys():
                    raise KeyError(f"Missing key {key} in project file {filename}")
            # deserialize the project file
            self.chr_data.load(data["chr_data"])
            self.nmt_data.load(data["nmt_data"])
            self.palette_data.load(data["palette_data"])
            self.color_format = ColorFormat(data["color_format"])

    def save(self, filename):
        """Save a project to a file."""
        data = {
            "chr_data": self.chr_data.save(),
            "nmt_data": self.nmt_data.save(),
            "palette_data": self.palette_data.save(),
            "color_format": self.color_format.value
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
