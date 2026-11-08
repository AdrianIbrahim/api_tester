from pathlib import Path
import yaml

def load_yaml_file(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data