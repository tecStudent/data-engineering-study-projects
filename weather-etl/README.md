# Weather ETL

A study project that builds a local weather data pipeline using **OpenWeather**, **Apache Airflow**, **Python**, **Docker**, and **PostgreSQL**.

The project is being developed incrementally through sprints, starting with raw ingestion and local orchestration, and later evolving into transformation, modeling, and relational loading.

---

## Index

- [Overview](#overview)
- [Current Architecture](#current-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Current Status](#current-status)
- [How to Run](#how-to-run)
- [Environment Variables](#environment-variables)
- [Airflow Access](#airflow-access)
- [Current DAG](#current-dag)
- [Sprint Tracking](#sprint-tracking)
- [Next Steps](#next-steps)
- [Known Issues](#known-issues)

---

## Overview

`weather-etl` is a hands-on data engineering project created to practice the core parts of a real data pipeline:

- extracting data from an external API
- orchestrating tasks with Airflow
- storing raw data
- preparing the project for future transformation and database loading

At the current stage, the pipeline extracts weather data from the **OpenWeather API** and stores the raw response as a JSON file.

---

## Current Architecture

The current flow of the project is:

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

### Current execution flow

1. Airflow triggers the DAG
2. Python calls the OpenWeather API
3. The API response is received as JSON
4. The raw payload is saved locally in the storage layer

---

## Tech Stack

* **Python**
* **Apache Airflow**
* **Docker**
* **PostgreSQL**
* **OpenWeather API**

---

## Project Structure

```text
weather-etl/
├── airflow/
│   └── dags/
├── src/
│   ├── __init__.py
│   └── extract/
│       ├── __init__.py
│       ├── openweather.py
│       └── test_openweather.py
├── storage/
│   └── raw/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## Current Status

So far, the project already supports:

* local environment startup with Docker
* Apache Airflow running locally
* PostgreSQL container running locally
* extraction from OpenWeather API
* raw JSON payload generation in `storage/raw`
* DAG execution through the Airflow UI

This means the project already has a working **raw ingestion MVP**.

---

## How to Run

### 1. Start the containers

From the root of the `weather-etl` folder:

```bash
docker compose up -d --build
```

If needed, you can recreate everything from scratch:

```bash
docker compose down --volumes --remove-orphans
docker compose up -d --build
```

---

## Environment Variables

The project expects a `.env` file in the root folder.

Example:

```env
AIRFLOW_UID=50000

OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_CITY=Sao Paulo
OPENWEATHER_COUNTRY=BR
OPENWEATHER_UNITS=metric
OPENWEATHER_LANG=pt_br
```

---

## Airflow Access

After the containers are up, access Airflow at:

```text
http://localhost:8081
```

PostgreSQL is exposed locally at:

```text
localhost:5433
```

---

## Current DAG

At the current stage, the main DAG is responsible for:

* calling the OpenWeather API
* collecting the current weather payload
* saving the raw JSON output into the storage layer

Expected output:

```text
storage/raw/
```

A successful execution should create a JSON file in that folder.

---

## Sprint Tracking

The sprint planning and execution tracking for this project are being monitored in Notion:

[Weather ETL Sprint Plan](https://lava-ridge-12d.notion.site/Plano-de-Sprints-Weather-ETL-34caba75252180fd92c7f77844ed47fa)

---

## Next Steps

The next steps planned for the project are:

* transform the raw weather payload
* define a staging layer
* load structured data into PostgreSQL
* model the data for analytics
* improve documentation and local setup reliability
* evaluate dbt usage for transformation/modeling

---

## Known Issues

At the current stage, writing to `storage/raw` may require permission adjustment inside the Airflow container.

If needed, the following command was used successfully during local setup:

```bash
docker compose exec --user root airflow-scheduler bash -c "mkdir -p /opt/airflow/storage/raw && chmod -R 777 /opt/airflow/storage"
```

This indicates that the storage permission handling still needs a more permanent solution.

---
