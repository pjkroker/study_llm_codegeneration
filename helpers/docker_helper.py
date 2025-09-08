import logging
import docker
import os
import sys
import json
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class DockerHelper:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.client = docker.from_env()
        self.logger.info("Docker client initialized")
    

    #TODO test it 
    def build_container(self, context_path=".", dockerfile="dockerfile", tag="my_docker_file", platform="linux/amd64", log_path="docker_build_log.jsonl"):
        """
        Build a Docker image.

        :param dockerfile: Path to Dockerfile
        :param tag: Image tag
        :param platform: Target platform (e.g., "linux/amd64")
        #:param context: Build context (default ".")
        :return: Built image object
        """
        #os.environ.setdefault("DOCKER_BUILDKIT", "1")
        #os.environ["DOCKER_DEFAULT_PLATFORM"] = "linux/amd64"
        api = docker.APIClient(base_url="unix:///var/run/docker.sock")
        
        

        with open(log_path, "w") as f:
            build_output = api.build(
                path=context_path,
                dockerfile=dockerfile,
                tag=tag,
                platform=platform,
                rm=True,
                decode=True,
            )

            for chunk in build_output:
                # write every JSON chunk to file
                f.write(json.dumps(chunk) + "\n")

                # you can still log selectively
                if "stream" in chunk:
                    self.logger.info(chunk["stream"].rstrip())
                if "error" in chunk:
                    self.logger.error(chunk["error"].rstrip())

    def run_container(self, image, command, host_volume_path, guest_volume_path):

        container = self.client.containers.run(
            image=image,
            command=command,  # This is inside the container
            volumes={
                host_volume_path: {  # This is on the host
                    "bind": guest_volume_path,  # This will appear inside the container
                    "mode": "rw"
                }
            },
            tty=True,
            stdin_open=True,
            detach=True,
            stdout=True,  # capture stdout
            stderr=True,
        )
        return container
    
    #TODO test it
    def exec(self, container, cmd, workdir=None, use_bash=True):
        if not container:
            raise RuntimeError("No container running")
        return self.container.exec_run(["bash", "-lc", cmd], stdout=True, stderr=True, demux=True)

    #TODO test it
    def stop_container(self, container, *, remove=True):
        """Cleanup helper."""
        try:
            container.remove(force=True) if remove else container.stop()
        except Exception:
            pass
