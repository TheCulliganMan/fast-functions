install:
	conda install -c conda-forge cupy cudatoolkit=10.0
	pip install --upgrade jax jaxlib==0.1.62+cuda110 -f https://storage.googleapis.com/jax-releases/jax_releases.html
	python -m pip install -e .
test:
	$(MAKE) install
	pytest .