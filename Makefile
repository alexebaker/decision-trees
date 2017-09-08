all: docs

.PHONY: clean
clean:
	find . -name "*.pyc" -delete

.PHONY: docs
docs:
	sphinx-apidoc -f -o docs/source/ decision_tree/ && pushd docs && make html && popd


