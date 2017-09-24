# Decision Trees

UNM CS 429/529 Machine Learning Project 1: Decision Trees


## Details

Details about this project can be found on [Kaggle](https://inclass.kaggle.com/c/cs529-project1)


## Usage

**NOTE**: This code will work with either python 2 or python 3.

The main entry point for this project is `dtree.py`. Use the `-h` flag from any command to see help:

```bash
>>> python dtree.py -h
usage: dtree.py [-h] [--training-data TRAINING_DATA]
                [--testing-data TESTING_DATA]
                [--classification-file CLASSIFICATION_FILE] [--gini-index]
                [--alpha ALPHA]

Creates decision trees based on a given data file.

optional arguments:
  -h, --help            show this help message and exit
  --training-data TRAINING_DATA
                        Path to the training data file.
  --testing-data TESTING_DATA
                        Path to the test data file.
  --classification-file CLASSIFICATION_FILE
                        Path to the classification file to write the results
                        of the testing data.
  --gini-index          Whether or not to use gini-index instead of
                        information gain.
  --alpha ALPHA         Alpha to use in chi-squared calculations.
```

Create a decision tree for a given data file:

```bash
python dtree.py --training-data data/training.csv --testing-data data/testing.csv
```

By default, information gain is used with an alpha vaue of 0.05. You can change these from the command line to use gini-index or a different alpha value:

To use gini-index, simply add the `--gini-index` flag to any command:

```bash
python dtree.py --training-data data/training.csv --testing-data data/testing.csv --gini-index
```

If you want to use an alpha value other than 0.05, you can specify that with the `--alpha` parameters as well:

```bash
python dtree.py --training-data data/training.csv --testing-data data/testing.csv --alpha 0.01
```

You can use both the `--gini-index` and `--alpha` flag together as well"

```bash
python dtree.py --training-data data/training.csv --testing-data data/testing.csv --alpha 0.1 --gini-index
```


## Documentation

This module uses documentation complied by [sphinx](http://www.sphinx-doc.org/en/stable/) located in the `docs/` directory. First, Shpinx needs to be installed into a virtual env:

First, you need to initialize the virtualenv:

```bash
virtualenv .venv
```

Next, activate the virtualenv in your current shell:

```bash
source .venv/bin/activate
```

Now, install the python requirements:

```bash
pip install -r requirements.txt
```

You can deactivate the virtualenv with the following command, however, make sure the virtualenv is active when you build the documentation:

```bash
deactivate
```

Now you can build the documentation. To build the documentation, run the Makefile:

```bash
source .venv/bin/activate
make docs
```

Once the documentation is built, it can be viewed in your brower by running the `open-docs.py` script:

```bash
python open-docs.py
```


## TODO

- [x] - Implement ID3
- [x] - Implement Gini Index
- [x] - Implement Information Gain
- [x] - Implement Chi-Square testing in ID3
- [ ] - Write up final report


## Authors

* [Alexander Baker](mailto:alexebaker@unm.edu)

* [Caleb Waters](mailto:waterscaleb@unm.edu)

* [Mark Mitchell](mailto:mamitchell@unm.edu)
