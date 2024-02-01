"""Useful data models for middle ground between front and back end."""

from neseditor.backend.serialization import CHRBytes

class CHR():
    """A PPU Pattern table with serializer"""
    def __init__(self):
        self.chr_bytes = CHRBytes()
        self.tiles = None



class CHRTile():
    """A PPU Pattern table tile."""
