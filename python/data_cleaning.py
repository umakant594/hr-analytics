import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

input_file = DATA_DIR / "hr_employee_data.csv"
output_file = DATA_DIR / "hr_employee_cleaned.csv"

# Load dataset
df = pd.read_csv(input_file)

print("=" * 60)
print("HR ANALYTICS - DATA CLEANING")
print("=" * 60)

print("\nOriginal dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# Convert numeric columns
numeric_columns = [
    "salary",
    "age",
    "experience",
    "performance",
    "satisfaction",
    "absence_days"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Check missing values after conversion
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Remove rows with missing critical values
critical_columns = [
    "employee_id",
    "department",
    "job_role",
    "salary",
    "age",
    "experience",
    "performance",
    "attrition",
    "satisfaction"
]

existing_critical_columns = [
    column for column in critical_columns
    if column in df.columns
]

df = df.dropna(subset=existing_critical_columns)

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"Cleaned rows: {len(df):,}")
print(f"Cleaned columns: {len(df.columns)}")
print(f"Saved to: {output_file}")

print("\nFinal columns:")
print(df.columns.tolist())

print("\nFinal dataset preview:")
print(df.head())