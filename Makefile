TEST_PATH=./test
SRC_PATH=./src

install:
	pipenv install --dev
	echo 'make precommit' > .git/hooks/precommit
	chmod u+x .git/hooks/precommit

clean: clean-pyc
	pipenv --rm

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

lint:
	pipenv run pycodestyle --show-source --show-pep8 ./

test: clean-pyc
	PYTHONPATH=${SRC_PATH}:${PYTHONPATH} pipenv run pytest --spec --color=yes $(TEST_PATH)

precommit: lint test

run:
	pipenv run src/app.py