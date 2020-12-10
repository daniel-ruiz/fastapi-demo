.PHONY: migrate runserver


migrate:
	cd ./src && PYTHONPATH=. alembic upgrade head && cd -

runserver:
	uvicorn src.main:app --reload
