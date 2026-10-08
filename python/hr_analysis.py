import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "hr_employee_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "screenshots"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)

# Convert Yes/No attrition into 1/0

df["attrition_flag"] = (
df["attrition"]
.astype(str)
.str.strip()
.str.lower()
.map({"yes": 1, "no": 0})
)

print("=" * 70)
print("HR ANALYTICS - PYTHON ANALYSIS")
print("=" * 70)

# ============================================================

# 1. DATASET OVERVIEW

# ============================================================

print("\n1. DATASET OVERVIEW")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns) - 1}")

print("\nData types:")
print(df.drop(columns=["attrition_flag"]).dtypes)

print("\nMissing values:")
print(df.drop(columns=["attrition_flag"]).isnull().sum())

print("\nSummary statistics:")

print(
df[
[
"salary",
"age",
"experience",
"performance",
"satisfaction",
"absence_days"
]
].describe().round(2)
)

# ============================================================

# 2. ATTRITION ANALYSIS

# ============================================================

print("\n2. ATTRITION ANALYSIS")

print("\nAttrition count:")
print(df["attrition"].value_counts())

attrition_rate = df["attrition_flag"].mean() * 100

print(f"\nOverall attrition rate: {attrition_rate:.2f}%")

plt.figure(figsize=(7, 5))

sns.countplot(
data=df,
x="attrition"
)

plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "attrition_distribution.png",
dpi=300
)

plt.close()

# ============================================================

# 3. DEPARTMENT ANALYSIS

# ============================================================

print("\n3. DEPARTMENT COMPARISON")

department_analysis = (
df.groupby("department")
.agg(
employees=("employee_id", "count"),
average_salary=("salary", "mean"),
average_experience=("experience", "mean"),
attrition_rate=("attrition_flag", "mean")
)
.reset_index()
)

department_analysis["average_salary"] = (
department_analysis["average_salary"].round(2)
)

department_analysis["average_experience"] = (
department_analysis["average_experience"].round(2)
)

department_analysis["attrition_rate"] = (
department_analysis["attrition_rate"] * 100
).round(2)

print(
department_analysis.to_string(index=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
data=department_analysis,
x="employees",
y="department"
)

plt.title("Employees by Department")
plt.xlabel("Number of Employees")
plt.ylabel("Department")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "department_employee_count.png",
dpi=300
)

plt.close()

plt.figure(figsize=(10, 6))

sns.barplot(
data=department_analysis,
x="attrition_rate",
y="department"
)

plt.title("Attrition Rate by Department")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Department")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "department_attrition.png",
dpi=300
)

plt.close()

# ============================================================

# 4. SALARY ANALYSIS

# ============================================================

print("\n4. SALARY ANALYSIS")

print(f"Minimum salary: ₹{df['salary'].min():,.0f}")
print(f"Maximum salary: ₹{df['salary'].max():,.0f}")
print(f"Average salary: ₹{df['salary'].mean():,.0f}")
print(f"Median salary: ₹{df['salary'].median():,.0f}")

plt.figure(figsize=(10, 6))

sns.histplot(
data=df,
x="salary",
bins=30,
kde=True
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "salary_distribution.png",
dpi=300
)

plt.close()

# ============================================================

# 5. SALARY BY DEPARTMENT

# ============================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
data=df,
x="salary",
y="department"
)

plt.title("Salary Distribution by Department")
plt.xlabel("Salary")
plt.ylabel("Department")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "salary_by_department.png",
dpi=300
)

plt.close()

# ============================================================

# 6. EXPERIENCE ANALYSIS

# ============================================================

print("\n5. EXPERIENCE ANALYSIS")

df["experience_group"] = pd.cut(
df["experience"],
bins=[
-1,
2,
5,
10,
float("inf")
],
labels=[
"0-2 Years",
"3-5 Years",
"6-10 Years",
"10+ Years"
]
)

experience_analysis = (
df.groupby(
"experience_group",
observed=False
)
.agg(
employees=("employee_id", "count"),
attrition_rate=("attrition_flag", "mean")
)
.reset_index()
)

experience_analysis["attrition_rate"] = (
experience_analysis["attrition_rate"] * 100
).round(2)

print(
experience_analysis.to_string(index=False)
)

plt.figure(figsize=(9, 6))

sns.barplot(
data=experience_analysis,
x="experience_group",
y="attrition_rate"
)

plt.title("Attrition Rate by Experience")
plt.xlabel("Experience")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "experience_attrition.png",
dpi=300
)

plt.close()

# ============================================================

# 7. SATISFACTION ANALYSIS

# ============================================================

print("\n6. SATISFACTION ANALYSIS")

satisfaction_analysis = (
df.groupby("satisfaction")
.agg(
employees=("employee_id", "count"),
attrition_rate=("attrition_flag", "mean")
)
.reset_index()
)

satisfaction_analysis["attrition_rate"] = (
satisfaction_analysis["attrition_rate"] * 100
).round(2)

print(
satisfaction_analysis.to_string(index=False)
)

plt.figure(figsize=(9, 6))

sns.barplot(
data=satisfaction_analysis,
x="satisfaction",
y="attrition_rate"
)

plt.title("Attrition Rate by Satisfaction")
plt.xlabel("Satisfaction Score")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "satisfaction_attrition.png",
dpi=300
)

plt.close()

# ============================================================

# 8. PERFORMANCE ANALYSIS

# ============================================================

print("\n7. PERFORMANCE ANALYSIS")

performance_analysis = (
df.groupby("performance")
.agg(
employees=("employee_id", "count"),
attrition_rate=("attrition_flag", "mean")
)
.reset_index()
)

performance_analysis["attrition_rate"] = (
performance_analysis["attrition_rate"] * 100
).round(2)

print(
performance_analysis.to_string(index=False)
)

plt.figure(figsize=(9, 6))

sns.barplot(
data=performance_analysis,
x="performance",
y="attrition_rate"
)

plt.title("Attrition Rate by Performance")
plt.xlabel("Performance Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "performance_attrition.png",
dpi=300
)

plt.close()

# ============================================================

# 9. CORRELATION ANALYSIS

# ============================================================

print("\n8. CORRELATION ANALYSIS")

correlation_columns = [
"salary",
"age",
"experience",
"performance",
"satisfaction",
"absence_days",
"attrition_flag"
]

correlation_matrix = df[correlation_columns].corr()

print("\nCorrelation matrix:")

print(
correlation_matrix.round(2)
)

plt.figure(figsize=(10, 8))

sns.heatmap(
correlation_matrix,
annot=True,
fmt=".2f",
cmap="coolwarm"
)

plt.title("HR Metrics Correlation Matrix")

plt.tight_layout()

plt.savefig(
OUTPUT_DIR / "correlation_heatmap.png",
dpi=300
)

plt.close()

# ============================================================

# 10. EMPLOYEE SEGMENTATION

# ============================================================

print("\n9. EMPLOYEE SEGMENTATION")

df["employee_segment"] = np.select(
[
(
(df["performance"] >= 4)
&
(df["satisfaction"] >= 4)
),
(
(df["performance"] >= 4)
&
(df["satisfaction"] < 4)
),
(
(df["performance"] < 4)
&
(df["satisfaction"] >= 4)
),
(
(df["performance"] < 4)
&
(df["satisfaction"] < 4)
)
],
[
"High Performer - Highly Satisfied",
"High Performer - Low Satisfaction",
"Lower Performer - Satisfied",
"Lower Performer - Low Satisfaction"
],
default="Other"
)

segment_analysis = (
df.groupby("employee_segment")
.agg(
employees=("employee_id", "count"),
average_salary=("salary", "mean"),
attrition_rate=("attrition_flag", "mean")
)
.reset_index()
)

segment_analysis["average_salary"] = (
segment_analysis["average_salary"].round(2)
)

segment_analysis["attrition_rate"] = (
segment_analysis["attrition_rate"] * 100
).round(2)

print(
segment_analysis.to_string(index=False)
)

# ============================================================

# 11. SAVE ANALYSIS TABLES

# ============================================================

department_analysis.to_csv(
OUTPUT_DIR / "department_analysis.csv",
index=False
)

experience_analysis.to_csv(
OUTPUT_DIR / "experience_analysis.csv",
index=False
)

satisfaction_analysis.to_csv(
OUTPUT_DIR / "satisfaction_analysis.csv",
index=False
)

performance_analysis.to_csv(
OUTPUT_DIR / "performance_analysis.csv",
index=False
)

segment_analysis.to_csv(
OUTPUT_DIR / "employee_segments.csv",
index=False
)

# ============================================================

# COMPLETED

# ============================================================

print("\n" + "=" * 70)
print("PYTHON ANALYSIS COMPLETED")
print("=" * 70)

print("\nCharts and analysis files saved to:")
print(OUTPUT_DIR)
