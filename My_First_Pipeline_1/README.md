**Data Pipeline with GCP**

**Overview**
This project demonstrates a basic data pipeline using Google Cloud Platform (GCP). It allows users to upload CSV files to Google Cloud Storage (GCS), which then triggers a Cloud Function to process and store the data in BigQuery. This setup serves as a foundation for more advanced data engineering projects.

**Components**
1. Flask API
A simple API built using Flask that handles CRUD operations and facilitates the upload of CSV files to GCS.

Functionality:
Upload CSV files to GCS
Basic CRUD operations

2. Google Cloud Storage (GCS)
Storage service where CSV files are uploaded by users.

Bucket Name: your-bucket-name (Replace with your actual bucket name)

3. Cloud Functions
Triggered by new file uploads in GCS. This function processes the CSV data and stores it in BigQuery.

Trigger: On new file upload to GCS
Processing: Converts and loads CSV data into BigQuery

4. BigQuery
Data warehouse where the processed data is stored.

Dataset: your-dataset-name (Replace with your actual dataset name)
Table: Created dynamically based on the CSV file schema


**Setup Prerequisites : **
Google Cloud Platform account
Python 3.x
Flask
Google Cloud SDK

**Challenges**
Handling Bad Records: Addressed errors from malformed or incomplete CSV data.

Schema Detection: Auto-detection in BigQuery is slow for large datasets.

Data Consistency: Standardized diverse CSV formats and data types.

Error Logging: Set up robust logging and monitoring for Cloud Functions.

**Future Improvements**
Implement predefined schemas for improved BigQuery performance.

Enhance error handling for better management of bad records.

Add more detailed logging and monitoring.

**Contributing**
Feel free to open issues or submit pull requests. Share your ideas and improvements to make this project even better!
