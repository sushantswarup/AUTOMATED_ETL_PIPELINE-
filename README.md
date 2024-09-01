# Automated ETL Pipeline for Financial Data Processing and Transformation

## Project Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline using Google Cloud and Python to process and transform financial data for mid, large, and small-cap companies. The pipeline is designed to handle the following tasks:

1. **Data Generation:** Python scripts generate financial data for mid, large, and small-cap companies.
2. **Data Upload:** The generated data is automatically uploaded to Google Cloud Storage.
3. **Data Loading:** The uploaded data is loaded into BigQuery staging tables using `bq load` commands.
4. **Data Transformation:** Custom BigQuery procedures are executed to transform the loaded data, making it ready for analysis.
5. **Scheduling:** The entire pipeline is scheduled to run at regular intervals using `cron` or other scheduling mechanisms.

## Key Features

- **Automated Data Processing:** The pipeline automates the entire process of data generation, upload, loading into BigQuery, and transformation.
- **Custom Procedures:** Written custom SQL procedures in BigQuery to handle data transformations efficiently.
- **Scalable and Flexible:** The pipeline is designed to handle data for multiple market segments (mid, large, and small caps) and can be easily extended to include additional data sources or transformations.
- **Scheduling:** The ETL process is fully automated and runs on a predefined schedule, ensuring timely updates of financial data.

## Setup and Usage

### Prerequisites

- Google Cloud Project
- Google Cloud SDK installed and authenticated
- Python 3.x installed
- Access to BigQuery and Google Cloud Storage
