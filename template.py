import os
from pathlib import Path
import logging

format_string = 'level=%(levelname)s datetime=%(asctime)s %(message)s'
logging.basicConfig(encoding='utf-8', level=logging.DEBUG,
                    format=format_string)
#logging.basicConfig(Level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name ="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml"
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("created directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsizeize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")