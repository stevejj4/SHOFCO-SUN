import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2.service_account import Credentials

# Set your project details
PROJECT_ID = "report-assistant-450121"  # Change to your project ID
DATASET_ID = "reporting"  # Change to your dataset
TABLE_ID = "processed"  # Change to your table name

# Path to your Google Cloud service account JSON key
SERVICE_ACCOUNT_FILE = "C:/Users/SHOFCO SUN/OneDrive/Desktop/SA/report-assistant-450121-911c9fb8ac87.json"

# Set authentication (ensure the file is stored securely)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

# Load data from the local file (replace with your file path)
file_path = "C:/Users/SHOFCO SUN/OneDrive/Desktop/dashboard/data/cleaned/merged_data.csv"  # Change to your file path
df = pd.read_csv(file_path)  # If it's a CSV file. Use read_excel for Excel, etc.

# Initialize BigQuery client
client = bigquery.Client()

# Define BigQuery table reference
table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# Upload DataFrame to BigQuery
job = client.load_table_from_dataframe(df, table_ref)

# Wait for job to complete
job.result()

print(f"Data successfully uploaded to BigQuery table: {table_ref}")
