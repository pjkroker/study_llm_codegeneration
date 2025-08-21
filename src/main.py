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


from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
client.view_api()

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		user_message="Give me a program that computes the first 100 prime numbers",
		api_name="/partial"
)
print(result)