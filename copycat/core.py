import shutil
import py7zr

from pathlib import Path
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

from copycat.config import Config

class Core:
    @staticmethod
    def bytes_to_mb(size: int) -> float|int:
        """Converts bytes to megabytes"""
        return size/1024/1024
    
    @staticmethod
    def archive_copy(src: str):
        if not Path(src).exists():
            raise FileNotFoundError(f"Directory {src} does not exist!")
        
        with py7zr.SevenZipFile("Archive.7z", 'w') as archive:
            archive.writeall(src)

    @staticmethod
    def copy(src: str, dst: str, **kwargs):
        """Copies the content of a source directory towards a destination"""

        home = kwargs.get("home", Path.cwd())
        verbose = kwargs.get("verbose", False)
        archive = kwargs.get("archive", False)

        src_path = Path(f"{home}/{src}")
        dst_path = Path(f"{home}/{dst}")

        max_size = Config.get("size_limit")
        exclude = Config.get("exclude")

        print(exclude)

        if not src_path.exists():
            raise FileNotFoundError(f"Source directory {src_path} does not exist!")

        if not dst_path.exists():
            dst_path.mkdir(parents=True)

        with ThreadPoolExecutor(max_workers=4) as executor:
            for src in tqdm(list(src_path.rglob("*"))):
                dst_item = Path(dst_path / src.relative_to(src_path))

                if (src.is_dir() and not 
                    any(part in exclude for part in src.parts)):
                    
                    dst_item.mkdir(exist_ok=True)

                elif (Core.bytes_to_mb(src.stat().st_size) <= max_size
                      and not any(part in exclude for part in src.parts)):
                    
                    executor.submit(shutil.copy2, src, dst_item)

        if archive:
            Core.archive_copy(dst_path)