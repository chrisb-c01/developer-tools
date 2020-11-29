This repository contains some skeleton code to configurare and run essential development tools for Python project via pre-commit hooks. It includes hooks for:
* isort
* Flake8
* Bugbear
* Black
* Mypy
* Pytest
* Coverage.py
* Bandit
* Safety

Steps for using pre-commit hooks: 
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Install pre-commit hooks `pre-commit install`
4. Change some code and commit to your own repository (the pre-commit hooks will run) 

Note:
* By default the development tools are not installed locally via pip (but fetched during execution of the pre-commit hooks). If you want you can (also) install all tools locally by `pip install -r requirements-dev.txt`.