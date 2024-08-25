import functions_framework
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
import time

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
    load_bq(name, bucket)


dataset = 'get_Data'
table = "Table1"


def load_bq(filename, bucket):
    client = bigquery.Client()
    filename = filename
    table_ref = client.dataset(dataset).table(table)
    job_config = LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Skip the header row in the CSV file
        autodetect=True,
        max_bad_records=20,  # Allow up to 10 bad records
        allow_quoted_newlines=True  # Allow newlines within quoted fields
    )

    uri = f'gs://{bucket}/{filename}'
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()  
    time.sleep(10)
    num_rows = load_job.output_rows
    print(f"{num_rows} rows loaded into {table}.")
