import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# instead of creating folders & files manually
# template.py will automatically create the whole project organization
project_name = "textSummarizer" # name of the project, the src folder will be named using this project_name

list_of_files = [
    ".github/workflows/.gitkeep", # continous update & deploy in github, .gitkeep to be needed initially for creating an empty folder
    f"src/{project_name}/__init__.py", # to be install as a local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # train & prediction pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", # keep all model parameters
    "app.py",
    "main.py",
    "Dockerfile", # image source code for deployment
    "requirements.txt",
    "setup.py",
    "notebooks/1.0_trials.ipynb", # notebooks for experimentation

] # it can be added manually later on


for filepath in list_of_files: # loop into the list above
    filepath = Path(filepath) # Path function to handle path issue
    filedir, filename = os.path.split(filepath) # split file dir & name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # check either the file is empty or contain something
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")