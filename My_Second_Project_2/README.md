# Incremental Data Load and Updates

## Overview

This project demonstrates how to handle incremental data updates and process data using Google Cloud Platform (GCP). It includes a script to generate and manage data, and a Google Cloud Function to process and merge data updates into a BigQuery dataset.

## Table of Contents

1. [Initial and Incremental Data](#initial-and-incremental-data)
2. [Cloud Function for Data Processing](#cloud-function-for-data-processing)
3. [Performance Considerations](#performance-considerations)
4. [Setup and Usage](#setup-and-usage)
5. [License](#license)

## Initial and Incremental Data

### Overview

- **Initial Data**: A set of dummy records is generated and saved to a CSV file. This data includes customer details and account information.
- **Incremental Data**: Additional dummy records are generated to simulate updates or new records. This data may reuse existing customer IDs and account numbers to reflect realistic scenarios.

### Data Structure

- `customer_id`: Unique identifier for the customer.
- `account_number`: Unique identifier for the account.
- `credit_score`: Credit score of the account.
- `account_balance`: Balance of the account.
- `last_modified`: Timestamp of the last update to the account information.

## Cloud Function for Data Processing

### Overview

The Cloud Function is triggered by changes in a Google Cloud Storage bucket. It processes incremental data and merges it into a BigQuery dataset.

### Function Details

- **Trigger**: Activated by file uploads to a specified Cloud Storage bucket.
- **Process Incremental Data**:
  - Loads data into a BigQuery staging table.
  - Merges data from the staging table into the main table, handling updates and new records.
  - Cleans up the staging table after processing.

## Performance Considerations

- **Scalability**: Ensure that the system can handle increasing data volumes efficiently.
- **Error Handling**: Implement robust error handling and logging mechanisms.
- **Testing**: Conduct thorough testing with different data sizes and scenarios to ensure reliability.

## Setup and Usage

### Initial Data

1. Generate the initial and incremental data files as needed.
2. Ensure these files are placed in the Google Cloud Storage bucket that triggers the Cloud Function.

### Cloud Function

1. Deploy the Cloud Function to GCP.
2. Configure the Google Cloud Storage bucket to trigger the function on file uploads.

### BigQuery

1. Ensure that your BigQuery dataset and table names align with those specified in the Cloud Function script.

## License

This project is licensed under the MIT License.
