"""Editor Backend Classes."""

from neseditor.backend.models import CHR
from neseditor.meta import SingletonMeta

class Editor(metaclass=SingletonMeta):

    """Main class of the backend"""
    def __init__(self, chr_rom_path: str = None):
        self.chr = CHR()
        if chr_rom_path:
            self.chr.chr_bytes.load_file(chr_rom_path)
