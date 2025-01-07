# This lays out version requirements and dev setup

Use Python version 3.11

Make sure you are in top level directory of repository.

```bash
ls # Check that you are in top level lmao, you should see the output here:
# README.md       backend         build.sh        deploy-vm.sh    frontend
python3.11 -m venv .venv # Use the system wide installation of python3.11
. .venv/bin/activate # Activate the venv we just made
python --version # Check that this gives back python3.11
pip --version # Check that this gives back pip3.11
pip install -r backend/requirements.txt # Install the requirements using python3.11's pip
```
Feel free to upgrade pip here if prompted to

At this point, select the python3.11 interpreter in VSCode/your editor

Also create a .env file that contains the OpenAPI API Key, please message Haashim to get it!
