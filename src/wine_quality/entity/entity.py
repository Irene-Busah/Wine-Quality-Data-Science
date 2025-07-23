"""
entity.py
============================

The file imaplements the Data Ingestion configuration
"""

# importing the needed libraries
from dataclasses import dataclass
from pathlib import Path

# defining the data ingestion dataclass
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path