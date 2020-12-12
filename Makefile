.PHONY: install-dependencies migrate runserver env-start


install-dependencies:
	pip install -r requirements.txt

migrate:
	PYTHONPATH=src alembic upgrade head

runserver:
	uvicorn src.fastapi_demo.main:app --reload

env-start: install-dependencies migrate runserver
