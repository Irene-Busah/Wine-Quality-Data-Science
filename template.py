# importing the necessary libraries
import os
from pathlib import Path
import logging

# setting the logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# setting the project name
project_name = 'wine_quality'


# defining the list of files for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity.py",
    f"src/{project_name}/config/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/notebook.ipynb",
    "templates/index.html",
    "app.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory {file_dir} for the file {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)):
        with open(file_path, 'w') as file:
            pass
            logging.info(f"Creating Empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")
