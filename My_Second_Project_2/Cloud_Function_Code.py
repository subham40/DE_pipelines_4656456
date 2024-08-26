import functions_framework
from google.cloud import bigquery

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    process_incremental_data(bucket, name)

dataset_id = 'New_DataSet_Increamental'
main_table = 'Credit_Table'

def process_incremental_data(bucket_name, file_name):
    # Initialize BigQuery client
    client = bigquery.Client()
    
    # Define dataset and table names
    staging_table_id = f'{dataset_id}.staging_table'
    main_table_id = f'{dataset_id}.{main_table}'

    # Load new data into the staging table
    uri = f"gs://{bucket_name}/{file_name}"
    load_job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True
    )
    load_job = client.load_table_from_uri(uri, staging_table_id, job_config=load_job_config)
    load_job.result()  # Wait for the load job to complete

    # Merge the data from the staging table into the main table
    merge_query = f"""
    MERGE {main_table_id} T
    USING {staging_table_id} S
    ON T.customer_id = S.customer_id AND T.account_number = S.account_number
    WHEN MATCHED THEN
      UPDATE SET
        T.credit_score = S.credit_score,
        T.account_balance = S.account_balance,
        T.last_modified = S.last_modified
    WHEN NOT MATCHED THEN
      INSERT (customer_id, account_number, credit_score, account_balance, last_modified)
      VALUES (S.customer_id, S.account_number, S.credit_score, S.account_balance, S.last_modified);
    """
    client.query(merge_query).result()  # Execute the merge query

    # Drop the staging table
    drop_table_query = f"DROP TABLE {staging_table_id};"
    client.query(drop_table_query).result()  # Execute the drop table query

    print(f"Processed and cleaned up staging table {staging_table_id}")


