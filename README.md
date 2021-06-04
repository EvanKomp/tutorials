# Tutorials ![build badge](https://github.com/valleau-lab/tutorials/actions/workflows/main.yml/badge.svg?branch=main)
This repository contains python tutorials for machine learning, visualization, computational chemistry etc. 
These tutorials were created by students in the [Valleau lab](https://www.valleau-lab.com/students). 

<img src="/docs/long_logo_2.png" alt="logo" width="400"/>

## Where to find the tutorials

Individual turorials are located in the `/tutorials/` folder. See the repository structure below.

Currently contained tutorials:
- `machine_learning_with_keras`
- `github`

## Repo structure
```
tutorials/
|-setup.py                                    # File that defines the python package and allows it to be installed
|-.gitignore                                  # Defines path structure for git to ignore by default, eg. eggs
|-README.md                                   # What you are looking at!
|-LICENSE
|-tutorials/                                  # Folder containing the tutorials
| |-machine_learning_with_keras/              # Tutorial on using keras to produce neural networks
| |-github/                                   # Tutorial on continuous integration and the importance of the structure here
|-docs/
|-package/                                    # An example python package installed by setup.py
| |-amodule.py                                # An importable module
| |-asubpackage/                              # An importable subpackage
| | |-anothermodule.py                        # Importable module within asubpackage
| |-test/                                     # Test folder defining tests for the package, mirrors package structure
| | |-test_amodule.py                         # tests package/amodule.py
| | |-test_asubpackage/                       # contains tests for package/asubpackage/
| | | |-test_anothermodule.py                 # tests package/asubpackage/anothermodule.py. empty! poor coverage
|-.github/
| |-wofklows/
| | |-main.yml                                # Contains the continuous integration actions to be ran.
```

## Installation and dependecies

Install the demonstration package by running the following:
> pip install .

For testing packages as well
> pip install -e .[tests]

This will install:
- flake8-docstrings
- coverage
- pytest

Which are ran on pull requests.

## License
[Apache 2.0](LICENSE)

## About Us
This repo is created and maintained by Valleau Lab, University of Washington

Primary Maintainer:

    - Stephanie Valleau
    
Contributers:

    - Nida Janulaitis
    - Evan Komp
    - Brenden Pelkie
