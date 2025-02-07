import os
import pandas as pd

# Define file paths
DATA_DIR = "data"
RAW_DIR = os.path.join(DATA_DIR, "raw")
CLEANED_DIR = os.path.join(DATA_DIR, "cleaned")

# Define paths to the raw data files
members_path = "C:/Users/SHOFCO SUN/OneDrive/Desktop/dashboard/data/raw/Members.csv"
payments_path = "C:/Users/SHOFCO SUN/OneDrive/Desktop/dashboard/data/raw/PaymentsJan.xlsx"

# Create the cleaned directory if it doesn't exist
if not os.path.exists(CLEANED_DIR):
    print(f"Creating directory: {CLEANED_DIR}")
    os.makedirs(CLEANED_DIR)

# Load datasets
print("Loading datasets...")
members = pd.read_csv(members_path)
payments = pd.read_excel(payments_path)

# Convert ID columns to numeric
members['ID Number'] = pd.to_numeric(members['ID Number'], errors='coerce')
members['NationalID'] = pd.to_numeric(members['ID Number'], errors='coerce')  # Assuming 'NationalID' is derived
payments['Account no'] = pd.to_numeric(payments['Account no'], errors='coerce')

# Merging datasets
print("Merging datasets...")
merged_data = pd.merge(members, payments, left_on='NationalID', right_on='Account no')

# Save merged data
merged_data_path = os.path.join(CLEANED_DIR, "merged_data.csv")
print(f"Merged data will be saved to: {merged_data_path}")
merged_data.to_csv(merged_data_path, index=False)
print("Merged dataset saved successfully.")

# Group and aggregate data
print("Aggregating data...")
grouped_data = merged_data.groupby(['Group Name', 'Ward']).agg(
    Total_Amount_Paid=('AMOUNT PAID', 'sum'),
    Total_Members_Paid=('NationalID', 'nunique')  # Count unique NationalIDs
).reset_index()

# Calculate total members in each group
member_counts = members.groupby('Group Name')['NationalID'].nunique().reset_index()
member_counts.columns = ['Group Name', 'Total Member Count']

# Merge aggregated data with member counts
final_group_totals = pd.merge(grouped_data, member_counts, on='Group Name', how='left')

# Reorder columns for readability
final_group_totals = final_group_totals[['Group Name', 'Ward', 'Total Member Count', 'Total_Members_Paid', 'Total_Amount_Paid']]

# Save final aggregated report
final_report_path = os.path.join(CLEANED_DIR, "final_report.csv")
print(f"Final report will be saved to: {final_report_path}")
final_group_totals.to_csv(final_report_path, index=False)
print("Final report saved successfully.")
print("✅ ETL pipeline completed!")
