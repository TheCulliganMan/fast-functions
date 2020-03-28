install:
	python setup.py build_ext
	pip install .
test:
	$(MAKE) install
	pytest .