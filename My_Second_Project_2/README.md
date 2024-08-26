# Incremental Data Load and Updates

## Overview

This project demonstrates how to generate dummy data, handle incremental updates, and process data using Google Cloud Platform (GCP). It includes a script to generate initial and incremental data and a Google Cloud Function to process these data updates.

## Table of Contents

1. [Initial and Incremental Data Generation](#initial-and-incremental-data-generation)
2. [Cloud Function for Data Processing](#cloud-function-for-data-processing)
3. [Additional Tips](#additional-tips)
4. [Performance Considerations](#performance-considerations)
5. [Setup and Usage](#setup-and-usage)
6. [License](#license)

## Initial and Incremental Data Generation

### Overview

The script generates two types of data:

- **Initial Data**: Generates a set number of initial dummy records and saves them to a CSV file.
- **Incremental Data**: Generates additional dummy records, with a chance to reuse existing records, and saves them to a separate CSV file.

### Script Details

#### Generate Initial Data:

- Generates `num_records` of initial dummy data.
- Each record includes `customer_id`, `account_number`, `credit_score`, `account_balance`, and `last_modified`.
- Saves the data to `dummy_data.csv`.

#### Track Existing Data:

- Uses a dictionary (`customer_data`) to keep track of existing `customer_id` and `account_number` pairs.

#### Generate Incremental Data:

- Generates `num_incremental_records` of additional dummy data.
- Reuses existing `customer_id` with a 50% chance to simulate updates or additional accounts.
- Saves the incremental data to `incremental_dummy_data.csv`.

### Additional Tips

- **Ensure Unique Account Numbers**: Modify the `generate_dummy_data` function to ensure unique `account_number` values.
- **Variable Chance for Reuse**: Adjust the probability for reusing `customer_id` as needed.
- **Handling Overlaps**: Ensure that incremental data does not overwrite existing records unintentionally.
- **Extend Functionality**: Add functionality for different types of updates or deletions.

## Cloud Function for Data Processing

### Overview

The provided Cloud Function is triggered by changes in a Google Cloud Storage bucket. It processes the incremental data and merges it into a BigQuery dataset.

### Function Details

- **Trigger**:
  - The function is triggered by changes in a Cloud Storage bucket.
  - Logs event details including bucket name, file name, and timestamps.

- **Process Incremental Data**:
  - Loads new data into a BigQuery staging table.
  - Merges the data from the staging table into the main table, updating or inserting records as necessary.
  - Drops the staging table after processing.

## Performance Considerations

- **Scalability**: Ensure the system scales effectively with increasing data volume.
- **Error Handling**: Implement error handling and logging for robustness.
- **Testing**: Perform thorough testing with various data volumes and scenarios.

## Setup and Usage

### Initial Data Generation

1. Update `num_records` and `num_incremental_records` as needed.
2. Run the script to generate `dummy_data.csv` and `incremental_dummy_data.csv`.

### Cloud Function

1. Deploy the Cloud Function to GCP.
2. Configure a Google Cloud Storage bucket to trigger the function.

### BigQuery

1. Ensure the dataset and table names match those specified in the script.

## License

This project is licensed under the [MIT License](LICENSE).
