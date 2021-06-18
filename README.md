# youtube_search python project

A baseline starting point to start any python project

## Usage

### Running the app

- `docker-compose up`

### Running tests

- `docker-compose run youtube_search_web pytest`

## Structure
- db: contains schema/migrations
- youtube_search: The actual project
    - api: controller layer
    - domain: domain model, services etc go here
    - exapi: Calls to external systems from this project
    - libraries: General purpose stuff
    - store: DB store
    - `__init__.py`: `create_app` which bootstraps the flask application
    - utils: General utility functions
        - `config.py`: Configurations setup
        - `flask.py`: Some modifications to flask
        - `log.py`: struct-log setup
        - `schema.py`: function wrapper to use voluptuous
- tests: All the tests
    - `conftest.py`: Basic fixtures
- `.drone.yml`: CD setup
- `pytest-fix.sh`: Fix if you switch between multiple environments multiple environments (host machine, docker, vm, etc.)
- `Pipfile`, `Pipfile.lock`: Requirements


## Frameworks/Libraries

### Web framework
- [Flask](http://flask.pocoo.org/)

### Metrics collection / tracing
- [datadog/statsd](https://github.com/DataDog/datadogpy)

### Database: [Postgres](https://www.postgresql.org/)
- [psycopg2](http://initd.org/psycopg/docs/)
- [sqlalchemy](https://www.sqlalchemy.org/)
- [sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
- [flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
- [alembic](http://alembic.zzzcomputing.com/en/latest/)
- [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Schema verification
- [voluptuous](https://github.com/alecthomas/voluptuous)

## Testing
- pytest
- pytest-flask
- responses
- pytest-runner
- pytest-cov
- pytest-pep8

## Other
- stringcase - conversion of string cases
- colorama - pretty console output {NOTE: Only required for development}
  `pipenv install --dev` to install it.
