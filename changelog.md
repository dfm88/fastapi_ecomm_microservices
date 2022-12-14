# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- simple fixture for login test

## [v1.0.2] - 2022-08-27
### Customer service
- first test setup
- fix Import of pydantic BaseSetting during tests

## [v1.0.1] - 2022-08-26
### Customer service
- authentication, login and jwt secret, refresh and test endpoint
- user update

## [v1.0.0] - 2022-08-26
### Customer service
- docker-compose for Postgres
- Customer and Address models
- base FastaPI config file
- Alembic for migrations
- first costumer and address models and schemas
- costumer create service and endpoint
- password hashing and verifying

### Release notes
- run alembic migrations 
```shell
docker-compose up
alembic revision --autogenerate
alembic upgrade head
```
