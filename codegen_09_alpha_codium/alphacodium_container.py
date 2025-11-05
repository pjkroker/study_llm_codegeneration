import logging
import docker
import os
import sys
import json
import tarfile
import io
from pathlib import Path

from study_llm_codegeneration.helpers.docker_helper import DockerHelper
from study_llm_codegeneration.helpers.subproccess_helper import run_shell



logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class AlphaCodiumContainer:
    def __init__(self, setup_path, model):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.SETUP_PATH = setup_path
        self.MODEL = model
        self._build_alpha_container()
        self.cntr_alpha_codium = self._run_alpha_container()
        self.logger.info("AlphaCodium Initialized, Ready to run actual commands")
    
    def _build_alpha_container(self):
        logging.info("---Building Docker Container using Shell Script---")
        result = run_shell(f"{self.SETUP_PATH}", shell=True)
        logging.debug(result["stdout"])
        logging.debug(result["stderr"])
        if(result["returncode"] != 0):
            logging.warning("---Building Docker Container using Shell Script Failed---")
            logging.debug(result["returncode"])
            sys.exit(result["returncode"])
    
    def _run_alpha_container(self):
        logging.info("---Running Docker Container ---")
        IMAGE_TAG = "codegen_study-alpha_codium"
        COMMAND = "sleep infinity"
        HOST_VOLUME_PATH = "/Users/paul/paul_data/projects_cs/study_llm_codegeneration/codegen_09_alpha_codium/out"
        GUEST_VOLUME_PATH = "/data"
        cntr_alpha_codium = DockerHelper()
        cntr_alpha_codium.run_container(IMAGE_TAG, COMMAND, HOST_VOLUME_PATH, GUEST_VOLUME_PATH)
        logging.debug("--- Testing the container ---")
        cntr_alpha_codium.exec("pwd")
        return cntr_alpha_codium
    
    def exec(self, cmd):
        self.cntr_alpha_codium.exec(cmd)
    
    def stop_container(self):
        self.cntr_alpha_codium.stop_container()

    