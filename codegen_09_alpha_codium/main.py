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
    cntr_alpha_codium = DockerHelper()
    cntr_alpha_codium.run_container(IMAGE_TAG, COMMAND, HOST_VOLUME_PATH, GUEST_VOLUME_PATH)
    cntr_alpha_codium.exec("pwd")
    logging.debug("---Testing Ollama Connection---")
    cntr_alpha_codium.exec("curl http://host.docker.internal:11434/v1/models")
    cntr_alpha_codium.exec('curl -X POST http://host.docker.internal:11434/api/generate  -d \'{"model":"llama2:latest","prompt":"Say hi!"}\'')

    logging.info("---Running Acutal Alpha Codium Commands ---")
    #expo = 'export HUGGINGFACE_API_KEY="hf_"
    expo2= "export LITELLM_LOG=DEBUG;"
    cmd = "source ./venv/bin/activate && python -m alpha_codium.solve_problem --dataset_name /app/valid_and_test_processed --split_name test --problem_number 0"
    cmd3 ="source ./venv/bin/activate && python -m alpha_codium.gen.generators"
    cmd_entire_dataset = "source ./venv/bin/activate &&  python -m alpha_codium.solve_dataset \
            --dataset_name /app/valid_and_test_processed \
            --split_name test \
            --database_solution_path /data/dataset_output.json"
    cmd_evaluate = "source ./venv/bin/activate &&  python -m alpha_codium.evaluate_dataset \
            --dataset_name /app/valid_and_test_processed \
            --split_name test \
            --database_solution_path /data/dataset_output.json"
    cntr_alpha_codium.exec(expo2)
    cntr_alpha_codium.exec("printenv")
    logging.info("test")
    
    cntr_alpha_codium.exec(cmd)
    cntr_alpha_codium.copy_file_from_container("/app/example.log", os.path.join(OUT_DIR, "log_alpha_codium.txt"))
    cntr_alpha_codium.stop_container()
    


if __name__ == "__main__":
    main()