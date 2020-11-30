This repository contains some skeleton code to configure and run essential development tools for Python project via pre-commit hooks. It is an accompanying resource for my blog post '[Essential developer tools for improving your Python code]()' on Medium.  

It includes hooks for:
* [isort](https://github.com/PyCQA/isort)
* [Flake8](https://github.com/PyCQA/flake8)
* [Bugbear](https://github.com/PyCQA/flake8-bugbear)
* [Black](https://github.com/psf/black)
* [Mypy](https://github.com/python/mypy)
* [Pytest](https://github.com/pytest-dev/pytest)
* [coverage.py](https://github.com/nedbat/coveragepy/tree/coverage-5.3)
* [Bandit](https://github.com/PyCQA/bandit)
* [Safety](https://github.com/pyupio/safety)

Steps for running the pre-commit hooks: 
1. Clone this repository: `git clone https://github.com/ChrisCalculus/developer-tools.git`
2. Install requirements: `pip install -r requirements.txt`
3. Install pre-commit hooks `pre-commit install` and `pre-commit install --hook-type pre-push`
4. Change some code and commit to *your own* repository (triggering the pre-commit hooks) 

Notes:
* By default the development tools are not installed locally via pip, but fetched & cached when running the pre-commit hooks for the first time. 
* Alternatively, you can install the development tools locally and run the pre-commit hooks using local packages by:
  * Installing local packages: `pip install -r requirements-dev.txt`.
  * Rename `.pre-commit-config.local.yaml` to `.pre-commit-config.yaml`
  * Install pre-commit hooks `pre-commit install`