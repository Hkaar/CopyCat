import shutil

from copycat import Core

from pathlib import Path
from console import Console

__include__ = ["CopyCat"]

class CopyCat:
    """Command class for the copycat module"""

    def __init__(self, console: Console) -> None:
        """Initializes the command class"""
        
        self.console = console
        self.console.register("copycat", "A backup utility")
        
        copy = self.console.append("copycat", "copy", self.copy)
        copy.add_argument("src", type=str)
        copy.add_argument("dst", type=str)
        copy.add_argument("--home", default=Path.cwd(), type=str)
        copy.add_argument("--verbose", default=False, action="store_true")
    
    def copy(self, args):
        Core.copy(args.src, args.dst, args.home, args.verbose)
