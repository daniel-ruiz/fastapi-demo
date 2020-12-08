.PHONY: runserver

runserver:
	uvicorn src.main:app --reload
