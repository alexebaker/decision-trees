# Decision Trees

UNM CS 429/529 Machine Learning Project 1: Decision Trees


## Details

Details about this project can be found on [Kaggle](https://inclass.kaggle.com/c/cs529-project1)


## Getting Started

**NOTE**: This repo requires [virtualenv](https://virtualenv.pypa.io/en/stable/) to be installed. See the link for installation instructions.
This is installed on both `moons.cs.unm.edu` and `trucks.cs.unm.edu`. All code and scripts have been tested and will work on either of these systems.

This project uses a virtualenv for managing packages. First, you need to initialize the virtualenv:

```bash
virtualenv .venv
```

Next, activate the virtualenv in your current shell:

```bash
source .venv/bin/activate
```

You can deactivate the virtualenv with the following command:

```bash
deactivate
```


## Usage

The main entry point for this project is `dtree.py`. Use the `-h` flag from any command to see help:

```bash
>>> python dtree.py -h
usage: dtree.py [-h] [--data-file DATA_FILE]

Creates decision trees based on a given data file.

optional arguments:
  -h, --help            show this help message and exit
  --data-file DATA_FILE
                        Path to the data file to use.
```

Create a decision tree for a given data file:

```bash
python dtree.py --data-file $path_to_data_file
```


## Documentation

This module uses documentation complied by [sphinx](http://www.sphinx-doc.org/en/stable/) located in the `docs/` directory. First, the documentation must be built:

```bash
make docs
```

Once the documentation is built, it can be viewed in your brower by running the `open-docs.py` script:

```bash
python open-docs.py
```


## TODO

- [ ] - Implement ID3
- [ ] - Implement Gini Index
- [ ] - Implement Information Gain
- [ ] - Implement Chi-Square testing in ID3
- [ ] - Write up final report


## Authors

* [Alexander Baker](mailto:alexebaker@unm.edu)

* [Caleb](mailto:waterscaleb@unm.edu)

* [Mark Mitchell](mailto:mamitchell@unm.edu)
