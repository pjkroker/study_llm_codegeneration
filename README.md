## Installation

(1) clone the repostitory:
```bash
git clone LINK_TO_GITHUB
cd study_llm_codegeneration/
```

(2) setup a virtual environment：
This tool was developed using Python 3.12.
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

(3) make sure the following shell scripts are executable
```bash
chmod +x /codegen_09_alpha_codium/setup.sh
chmod +x /codegen_10_open_code_interpreter/setup.sh
```
## Individual Requirements

### 09. Alpha Codium

(1) Alpha Codium comes preconfigured in a Docker container, which must be run with an x86 architecture for compatibility. On non-x86 systems, this can be achieved using virtualization tools like QEMU with Docker Desktop, wich is activated by default.

(2) Duplicate the file `codegen_09_alpha_codium/secrets_template.toml`, rename it as `codegen_09_alpha_codium/.secrets.toml`, and fill in your OpenAI API key:
```
[openai]
key = "..."
```
### 10. Open Code Generator
(1) Braucht eine lokale Nvidia GPU.


(2) Duplicate the file `env.template`, rename it as `.env`, and fill in your HF API key:
```
HF_TOKEN=hf_xxx...
```
## Run the applications
Make sure the venv is activated and you are in the project root directory (where study_llm_codegeneration/ lives).
You should not cd into subfolders to run the code — instead use Python’s module execution (-m).
```bash
source ./venv/bin/activate
cd ..
python -m study_llm_codegeneration.codegen_09_alpha_codium.main
python -m study_llm_codegeneration.codegen_10_open_code_interpreter.main
```
