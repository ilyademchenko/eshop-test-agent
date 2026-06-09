.PHONY: install install-browsers test test-auth test-catalog record lint

install:
	pip install -r requirements.txt

install-browsers:
	playwright install chromium

# Запуск всех тестов
test:
	pytest tests/ -v

# Запуск тестов по модулю
test-auth:
	pytest tests/e2e/test_auth.py -v

test-catalog:
	pytest tests/e2e/test_catalog.py -v

# Запись скрипта: make record PAGE=auth NAME=login URL=/login
record:
	python utils/recorder.py --page $(PAGE) --name $(NAME) --url $(URL)

# Конвертация: make convert SCRIPT=recorded_scripts/auth/login.py METHOD=login
convert:
	python utils/script_converter.py $(SCRIPT) --method $(METHOD)

lint:
	ruff check .
	black --check .
