"""This module contains classes that hold the data of the project
   and tools used to serialize and deserialize it."""

import json
import os

class CHRBytes():
    """CHRBytes is a class that holds the CHR data of the project."""
    def __init__(self) -> None:
        self.data = bytearray(0x1000)

    def load_str(self, chr_str):
        """Load the CHR data from a str."""
        self.data = bytearray.fromhex(chr_str)
        assert len(self.data) % 0xF == 0

    def load_file(self, chr_path):
        """Load the CHR data directly from a file."""
        with open(chr_path, "rb") as file:
            self.data = bytearray(file.read())
        assert len(self.data) % 0xF == 0

    def save_str(self):
        """Save the CHR data to a str."""
        return self.data.hex(sep=' ')

    def save_file(self, file_path):
        """Save the CHR data to a file."""
        # overwrites!
        with open(file_path, "wb") as file:
            file.write(self.data)

