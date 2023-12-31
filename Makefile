project-name = ai-village-capture-the-flag-defcon31

default:
	@echo "Project: $(project-name)\n"
	@echo "Commands:"
	@echo "  data: Fetch the dataset from Kaggle"
	@echo "  setup-python: Setup environment and a Jupyter kernel"
	@echo "  teardown-python: Remove the Jupyter kernel and the environment"

data: data/raw/sample_submission.csv
data/raw/sample_submission.csv:
	kaggle competitions download -c $(project-name) -p data/raw
	unzip -d data/raw $$(find data/raw -name '*zip')

submit:
	kaggle competitions submit $(project-name) \
	 -f data/processed/submission.csv \
	 -m "got next flag"

setup-python:
	poetry install --no-root
	poetry run ipython kernel install --user \
	 --name "$(project-name)" \
	 --display-name "Kaggle: CTF" \
	 --env PYTHONPATH $$(pwd)

teardown-python:
	jupyter kernelspec remove "$(project-name)" -y
	poetry env remove --all
