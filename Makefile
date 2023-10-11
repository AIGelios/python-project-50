test:
	poetry run pytest --cov

lint:
	poetry run flake8 gendiff

check:
	poetry run flake8 brain_games
	petry run pytest --cov

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

update:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall
