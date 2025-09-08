import logging
import os
import sys
import docker

from study_llm_codegeneration.helpers.docker_helper import DockerHelper
from study_llm_codegeneration.helpers.subproccess_helper import run_shell


def main():
    # Ensure the folder exists
    # folder path relative to the script file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUT_DIR = os.path.join(BASE_DIR, "out")
    os.makedirs(OUT_DIR, exist_ok=True)
    SETUP_PATH = os.path.join(BASE_DIR, "setup.sh")
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(OUT_DIR, "log.txt"), mode='w'),
            logging.StreamHandler(sys.stdout)
        ],
        force=True
    )
    logging.info("---9. Alpha Codium---")
    logging.info("---Building Docker Container using Shell Script---")
    result = run_shell(f"{SETUP_PATH}", shell=True)
    logging.debug(result["stdout"])
    logging.debug(result["stderr"])
    if(result["returncode"] != 0):
        logging.debug(result["returncode"])
        sys.exit(result["returncode"])

    logging.info("---Running Docker Container ---")
    IMAGE_TAG = "codegen_study-alpha_codium"
    COMMAND = "sleep infinity"
    HOST_VOLUME_PATH = "/Users/paul/paul_data/projects_cs/study_llm_codegeneration/codegen_09_alpha_codium/out"
    GUEST_VOLUME_PATH = "/data"
    #create helper
    container = DockerHelper()
    container.run_container(IMAGE_TAG, COMMAND, HOST_VOLUME_PATH, GUEST_VOLUME_PATH)
    container.exec(container, "touch ~/data/hallo.txt")


if __name__ == "__main__":
    main()