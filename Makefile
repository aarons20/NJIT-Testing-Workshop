test: virtualBankLimited.py tests_bank.py Exceptions.py
	coverage run -m pytest -vv tests_bank.py

report: test
	coverage report && coverage html

run: Exceptions.py virtualBankLimited.py
	python virtualBankLimited.py

clean:
	del .coverage && rmdir /s htmlcov

.PHONY: test clean run