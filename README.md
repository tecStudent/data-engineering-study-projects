# data-engineering-study-projects

A collection of hands-on data engineering study projects focused on data ingestion, transformation, orchestration, storage, and analytics workflows.

## Index

- [About](#about)
- [Projects](#projects)
  - [Weather ETL](#weather-etl)
- [Weather ETL Architecture](#weather-etl-architecture)
- [Sprint Tracking](#sprint-tracking)

## About

This repository was created to organize practical data engineering study projects.

The goal is to build small and medium-sized projects that simulate real-world data engineering scenarios, covering topics such as:

- data ingestion from APIs and files
- workflow orchestration
- raw and transformed data layers
- relational storage
- data modeling
- local development environments with Docker

Each project is organized in its own folder and may evolve over time as new features and improvements are added.

## Projects

### Weather ETL

Location: `weather-etl/`

`weather-etl` is a study project that simulates a simple weather data pipeline using the OpenWeather API.

At the current stage, the project is focused on:

- extracting weather data from the OpenWeather API
- orchestrating the extraction with Apache Airflow
- storing the raw API response as JSON files
- preparing the foundation for future transformation and loading into PostgreSQL

This project is being developed incrementally through sprints, starting with raw ingestion and local orchestration, and later evolving into transformation, modeling, and database loading.

## Weather ETL Architecture

The current architecture of the project follows a simple local ETL structure:

```text
OpenWeather API
      ↓
Python Extract
      ↓
Airflow DAG
      ↓
Raw JSON Storage
      ↓
(next steps)
Transformation
      ↓
PostgreSQL
````

### Current stack

* **Docker** for local environment setup
* **Apache Airflow** for orchestration
* **Python** for extraction logic
* **OpenWeather API** as data source
* **Local storage (`raw`)** for raw JSON persistence
* **PostgreSQL** prepared for future load steps

### Current status

So far, the project already supports:

* local environment startup with Docker
* Airflow execution through DAGs
* weather data extraction from OpenWeather
* raw JSON file generation in the storage layer

## Sprint Tracking

The execution and sprint progress of the `weather-etl` project is being tracked in Notion:

[Weather ETL Sprint Plan](https://lava-ridge-12d.notion.site/Plano-de-Sprints-Weather-ETL-34caba75252180fd92c7f77844ed47fa)

>>>>>>> e5550c9 (feat: setup local weather ETL environment with Airflow and raw ingestion)
