"""
common.py
===============

Contains common utils used in the entire project
"""


# importing necessary libraries
import os
import yaml
from src.wine_quality import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any


# defining a function to read yaml file

@ensure_annotations
def read_yaml(yaml_filepath: Path) -> ConfigBox:
    """Reads yaml file and returns ConfigBox"""

    try:
        with open(yaml_filepath) as file:
            content = yaml.safe_load(file)

            logger.info(f"Successfully Loaded {yaml_filepath}")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


# function to create directories
@ensure_annotations
def create_directories(directory_names: list, verbose=True):
    """Create list of directories"""

    for path in directory_names:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created Directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves the JSON data"""

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    
    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON file data"""

    with open(path) as file:
        content = json.load(file)

    logger.info(f"JSON file loaded successfully from {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves the binary file"""

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")


@ensure_annotations
def save_bin(path: Path):
    """Saves the binary file"""

    data = joblib.load(path)
    logger.info(f"Binary file load at {path}")

    return data
