
venv/bin/activate: requirements.txt
	python3 -m venv venv
	@echo "Installing dependencies"
	@venv/bin/pip install -r requirements.txt
	@touch venv/bin/activate

run: venv/bin/activate
	@echo "Removing previous barcodes"
	@rm -rf barcodes
	@echo "Running the application"
	@python3 main.py

zip:
	@echo "Zipping the application"
	@zip -r barcodes_uni-recycle.zip barcodes
	@mv barcodes_uni-recycle.zip /mnt/c/Users/emile/Desktop

clean:
	@echo "Cleaning up"
	@find . -type d -name __pycache__ -exec rm -rf {} +

fclean: clean
	@echo "Removing virtual environment"
	@rm -rf venv

re: fclean venv install run

.PHONY: venv activate install run clean fclean re
