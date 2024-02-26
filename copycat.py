import shutil

from pathlib import Path
from console import Console

class Core:
    @staticmethod
    def bytes_to_mb(size: int) -> float|int:
        return size/1024/1024
    
    @staticmethod
    def copy(src: str, dst: str, home: str = Path.cwd(), verbose: bool = False):
        home = home

        src_path = Path(f"{home}/{src}")
        dst_path = Path(f"{home}/{dst}")

        if not src_path.exists():
            raise FileNotFoundError(f"Source directory {src_path} does not exist!")
        
        if not dst_path.exists():
            dst_path.mkdir()

            Console.log(f"Created destination directory {dst_path}!", verbose)
        
        Console.log(f"Starting copy process from {src_path} to {dst_path}!")

        for src in src_path.rglob("*"):
            dst_folder = dst_path / src.relative_to(src_path)

            Console.log(f"Copying {dst_folder}...", verbose)

            if src.is_dir():
                dst_folder.mkdir(exist_ok=True)
                
            elif Core.bytes_to_mb(src.stat().st_size) <= 500:
                shutil.copy2(src, dst_folder)

        Console.log(f"Successfully copied {src_path} to {dst_path}!")