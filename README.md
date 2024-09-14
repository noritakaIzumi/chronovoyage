# ChronoVoyage

[![PyPI - Version](https://img.shields.io/pypi/v/chronovoyage.svg)](https://pypi.org/project/chronovoyage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chronovoyage.svg)](https://pypi.org/project/chronovoyage)

![logo](https://raw.githubusercontent.com/noritakaIzumi/chronovoyage/main/assets/images/logo.jpeg)

-----

## Motivation

I'm trying to write my own database migration framework and discuss database management ideals.

## Table of Contents

- [Installation](#Installation)
- [License](#License)

## Installation

```console
pip install chronovoyage
```

## Required dependencies

To use MariaDB, you need the MariaDB development package.

Install via apt:

```shell
sudo apt install libmariadb-dev
```

## Usage

First, you should name and initialize a directory.

```shell
chronovoyage init my-project
cd my-project
```

Edit `config.json`.

```json
{
  "$schema": "https://raw.githubusercontent.com/noritakaIzumi/chronovoyage/main/schema/config.schema.json",
  "vendor": "mariadb",
  "connection_info": {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "mariadb",
    "password": "password",
    "database": "test"
  }
}
```

Create migration template directory.

```shell
chronovoyage add ddl initial_migration
```

If you create DML,

```shell
chronovoyage add dml second_migration
```

Write up sql to `go.sql`, and rollback sql to `return.sql`.

Then, migrate.

```shell
chronovoyage migrate
```

## License

`chronovoyage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Roadmap

- Support for Python
    - [x] 3.8
    - [x] 3.9 or later
- Database support
    - [ ] MySQL
    - [x] MariaDB
    - [ ] PostgreSQL
- Migration file support
    - [x] SQL (.sql)
    - [ ] Shell script (.sh)
- Commands
    - ~~new~~ init
        - [x] create migration directory and config file
    - ~~generate~~ add
        - [x] create migration files from template
    - migrate
        - [x] to latest
        - [x] to specific version
        - [x] from the beginning
        - [x] from the middle
        - --dry-run
            - [ ] show executing SQL
        - [ ] detect ddl or dml
    - status
        - [ ] show current migration status
    - rollback
        - [ ] to version
    - test
        - [ ] check if every "migrate -> rollback" operation means do nothing for schema
        - [ ] if dml, the operation means do nothing for data (including autoincrement num)
