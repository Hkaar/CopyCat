import argparse, importlib, pkgutil

from typing import Callable
from functools import cache

class Console:
    _root = argparse.ArgumentParser(description="Fluid Console Commands")
    _index = {}

    @classmethod
    @cache
    def exec(cls, cmd: str = None):
        """Execute the console command based on parsed arguments."""

        if not cmd:
            args = cls._root.parse_args()
        else:
            args = cls._root.parse_args(cmd.split(" "))
            
        args.func(args)

    @classmethod
    def register(cls, name: str, desc: str = None) -> argparse._SubParsersAction:
        """Register a subcommand and return its subparser."""

        if name in cls._index:
            raise ValueError(f"Error while adding {name} to index. {name} already exists!")

        subcommand = cls._root.add_subparsers(title=name, description=desc, required=True)
        cls._index[name] = subcommand
        
        return subcommand

    @classmethod
    def append(cls, root: str, name: str, handler: Callable, desc: str = None) -> argparse.ArgumentParser:
        """Append a command to a specified root subcommand."""

        if root not in cls._index:
            raise ValueError(f"Error while appending command {name} to {root}. {root} does not exist!")

        subparser = cls._index[root].add_parser(name, help=desc)
        subparser.set_defaults(func=handler)
        return subparser

    @classmethod
    def auto_import(cls):
        """Automatically import all the included commands."""
        path = __path__

        for (_, module_name, _) in pkgutil.iter_modules(path):
            if not module_name.startswith("__"):
                module = importlib.import_module(f".{module_name}", package="console")

                if hasattr(module, "__include__"):
                    for cmd in module.__include__:
                        getattr(module, cmd)(Console)

    @staticmethod
    def log(msg: str, activate: bool = True):
        if activate:
            print(msg)

# Auto import all the included commands
Console.auto_import()
