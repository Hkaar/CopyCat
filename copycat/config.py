import json

from typing import Any

class Config:
    @staticmethod
    def open_config(path: str):
        with open(path, "r") as f:
            try:
                return json.load(f)
                
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON in {path}: {e}")
            
    @staticmethod
    def convert_type(value: Any, new_type: Any):
        try:
            if new_type == bool:
                return value.upper() == "TRUE"
        
            elif new_type == list:
                return type(map(str.strip, json.loads(value)))

            elif new_type != dict:
                return new_type(value)

        except ValueError:
            raise ValueError(f"Cannot convert {value} to {type}!")
            
    @staticmethod
    def get(key: str, path: str = "config.json") -> Any:
        data = Config.open_config(path)

        if key not in data:
            raise KeyError(f"Config key for {key} does not exist!")
        
        return data[key]
    
    @staticmethod
    def set(key: str, value: str, path: str = "config.json") -> bool:
        data = Config.open_config(path)

        if key not in data:
            raise KeyError(f"Config key for {key} does not exist!")
        
        data_type = type(data[key])

        value = Config.convert_type(value, data_type)
        
        data[key] = value

        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        
        return True
        