import logging
import os
import sys


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
    logging.info("---starting set up script---")

if __name__ == "__main__":
    main()