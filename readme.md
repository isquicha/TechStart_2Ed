# Olist Tech Start 2nd ed

## Description
This project is a programming challenge for an interview at [Olist](https://github.com/olist). Project complete description and specification (in pt-BR) are in [instructions](instructions.md).

It's basically a CRUD with 4 tables (Products, Categories, Sellers, Marketplaces). To do so, I made an API with Python's web framework Flask.

### Files and folder structure
- [settings.py](settings.py) is responsible for the project's settings, with includes configuration variables, extensions and blueprints.
- `migrations` folder is a database migrations folder created and managed by flask-migrate extension
- `requirements` folder contains the project's requirement files
    - [com.txt](com.txt) have the common dependencies and must be installed
    - [dev.txt](dev.txt) have the development dependencies
    - [prod.txt](prod.txt) have the production dependencies
    - [test.txt](test.txt) have the test dependencies
- `server` folder is a set of scripts to help me put the project on a production server
- `src` folder contains the application itself
    - `app` folder contains the flask app creation and initialization
    - `blueprints` folder contains the application's business rules

TODO: Finish topic


## Installation

### Requirements
- Git
- Python 3 (tested with 3.9, probably work with 3.6+)
- Python pip
- Python venv
### Steps
- Open terminal
- `git clone https://github.com/isquicha/TechStart_2Ed`
- `cd techstart_2ed`
- `python -m venv .venv`
- Windows: `.venv\Scripts\activate.bat`  Linux: `source .venv/bin/activate`
- `pip install -r requirements/com.txt` (on windows, backslash instead of forward slash)
- `pip install -r requirements/X.txt` with X = [dev, prod, test] for development, production or testing
- Edit and rename `dotenv example.txt` to `.env`
- `flask db init`
- `flask db migrate`
- `flask db upgrade`
- Run
    - `flask run` in development
    - `gunicorn 'src.app:create_app()'` in production

## Working Environment
### Development setup
#### Hardware
- CPU: Intel Core i5-4440 @ 4x 3.10GHz
- RAM: 12GB DDR3 1600MHz
- Storage: HDD (ST2000DM008)
#### Software
- Operational System: Windows 10
- Python Version: 3.9.1
- Flask version: 1.1.2
- Application Server: Flask embedded server
### Production setup
#### Hardware
- CPU: Intel Xeon Silver 4114 @ 2x 2.195GHz
- RAM: 1GB
- Storage: 40GB SSD
#### Software
- Operational System: Ubuntu 18.04 bionic
- Python Version: 3.9
- Flask version: 1.1.2
- Application Server: Gunicorn 20.0.4
- Web Server: Nginx 1.14.0
