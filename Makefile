install:
	python setup.py build_ext --inplace
	python setup.py install
test:
	$(MAKE) install
	pytest .