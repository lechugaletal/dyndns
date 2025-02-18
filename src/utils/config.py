import yaml
import sys

def load(config_path: str) -> yaml:

    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Config file {config_path} does not exist!")
        sys.exit(1)
