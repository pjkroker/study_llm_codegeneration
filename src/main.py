import logging
import os

#from docker_helper import DockerHelper
#from subproccess_helper import run, run_shell

# Ensure the folder exists
os.makedirs('./log', exist_ok=True)

# Set up basic configuration for logging
logging.basicConfig(
    filename='./log/log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)
logging.debug("---Starting Setup---")
logging.info("---10. OpenCodeInterpreter---")
