import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # asctime=time, module=file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # create the dir within the project
        logging.StreamHandler(sys.stdout) # shows in terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")