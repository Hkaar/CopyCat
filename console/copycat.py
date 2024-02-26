import shutil

from copycat import Core

from pathlib import Path
from console import Console

__include__ = ["CopyCat"]

class CopyCat:
    def __init__(self, console: Console) -> None:
        self.console = console

        self.console.register("copycat", "A backup utility")
        
        copy = self.console.append("copycat", "copy", self.copy)
        copy.add_argument("src", type=str)
        copy.add_argument("dst", type=str)
        copy.add_argument("--home", default=Path.cwd(), type=str)
        copy.add_argument("--verbose", default=False, action="store_true")

        config = self.console.append("copycat", "config", self.config)
        config.add_argument("key", type=str)
        config.add_argument("value", type=str)

    @staticmethod
    def bytes_to_mb(size):
        return size/1024/1024
    
    def copy(self, args):
        verbose = args.verbose
        Core.copy(args.src, args.dst, args.home)
        
    def config(self, key: str, value: str):
        pass
