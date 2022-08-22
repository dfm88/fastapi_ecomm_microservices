# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Customer service
- docker-compose for postgres
- Customer and Address models
- base FastaPI config file
- Alembic for migrations

### Release notes
- run alembic migrations 
```shell
docker-compose up
alembic revision --autogenerate
alembic upgrade head
```