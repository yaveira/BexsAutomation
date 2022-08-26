# Framework of APIs Testing
A example of testing framework for APIs using [Python](https://www.python.org/downloads/) 3.10.6 and [Behave](https://behave.readthedocs.io/en/stable/).

## Configuration
Create a virtual environment to installing dependencies of the project
```bash
python -m venv venv
```

Activate the virtual environment
```bash
.\venv\Scripts\activate
```

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```

## Usage
```python
# Behave
behave .\features\

# Use tag "@test" to indicate a completed test.
# Use tag "@wip" to indicate that Feature or Scenario is in development.
behave .\features\ -t "@tag_name"
```