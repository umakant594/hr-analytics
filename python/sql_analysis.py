import duckdb
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "hr_employee_cleaned.csv"

# Connect to DuckDB
con = duckdb.connect()

# Create a table from the cleaned CSV
con.execute(f"""
    CREATE OR REPLACE TABLE employees AS
    SELECT *
    FROM read_csv_auto('{DATA_FILE}')
""")

print("=" * 70)
print("HR ANALYTICS - SQL ANALYSIS")
print("=" * 70)


# ---------------------------------------------------------
# 1. TOTAL EMPLOYEES
# ---------------------------------------------------------
print("\n1. TOTAL EMPLOYEES")

result = con.execute("""
    SELECT COUNT(*) AS total_employees
    FROM employees
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 2. ATTRITION COUNT
# ---------------------------------------------------------
print("\n2. ATTRITION COUNT")

result = con.execute("""
    SELECT
        attrition,
        COUNT(*) AS employee_count
    FROM employees
    GROUP BY attrition
    ORDER BY employee_count DESC
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 3. ATTRITION RATE
# ---------------------------------------------------------
print("\n3. ATTRITION RATE")

result = con.execute("""
    SELECT
        ROUND(
            100.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate
    FROM employees
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 4. AVERAGE SALARY
# ---------------------------------------------------------
print("\n4. AVERAGE SALARY")

result = con.execute("""
    SELECT
        ROUND(AVG(salary), 2) AS average_salary
    FROM employees
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 5. AVERAGE AGE AND EXPERIENCE
# ---------------------------------------------------------
print("\n5. AVERAGE AGE AND EXPERIENCE")

result = con.execute("""
    SELECT
        ROUND(AVG(age), 2) AS average_age,
        ROUND(AVG(experience), 2) AS average_experience
    FROM employees
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 6. DEPARTMENT ANALYSIS
# ---------------------------------------------------------
print("\n6. DEPARTMENT ANALYSIS")

result = con.execute("""
    SELECT
        department,
        COUNT(*) AS employee_count,
        ROUND(AVG(salary), 2) AS average_salary,
        ROUND(AVG(experience), 2) AS average_experience
    FROM employees
    GROUP BY department
    ORDER BY employee_count DESC
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 7. DEPARTMENT ATTRITION
# ---------------------------------------------------------
print("\n7. DEPARTMENT ATTRITION")

result = con.execute("""
    SELECT
        department,
        COUNT(*) AS total_employees,
        SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            AS employees_left,
        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate
    FROM employees
    GROUP BY department
    ORDER BY attrition_rate DESC
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 8. EXPERIENCE ANALYSIS
# ---------------------------------------------------------
print("\n8. EXPERIENCE ANALYSIS")

result = con.execute("""
    SELECT
        CASE
            WHEN experience <= 2 THEN '0-2 Years'
            WHEN experience <= 5 THEN '3-5 Years'
            WHEN experience <= 10 THEN '6-10 Years'
            ELSE '10+ Years'
        END AS experience_group,

        COUNT(*) AS employee_count,

        SUM(
            CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END
        ) AS employees_left,

        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate

    FROM employees

    GROUP BY experience_group

    ORDER BY
        CASE experience_group
            WHEN '0-2 Years' THEN 1
            WHEN '3-5 Years' THEN 2
            WHEN '6-10 Years' THEN 3
            ELSE 4
        END
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 9. PERFORMANCE ANALYSIS
# ---------------------------------------------------------
print("\n9. PERFORMANCE ANALYSIS")

result = con.execute("""
    SELECT
        performance,
        COUNT(*) AS employee_count,
        SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            AS employees_left,
        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate
    FROM employees
    GROUP BY performance
    ORDER BY performance
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 10. SATISFACTION ANALYSIS
# ---------------------------------------------------------
print("\n10. SATISFACTION ANALYSIS")

result = con.execute("""
    SELECT
        satisfaction,
        COUNT(*) AS employee_count,
        SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            AS employees_left,
        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate
    FROM employees
    GROUP BY satisfaction
    ORDER BY satisfaction
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 11. SALARY ANALYSIS
# ---------------------------------------------------------
print("\n11. SALARY ANALYSIS")

result = con.execute("""
    SELECT
        CASE
            WHEN salary < 400000 THEN 'Below 4L'
            WHEN salary < 600000 THEN '4L-6L'
            WHEN salary < 800000 THEN '6L-8L'
            ELSE '8L+'
        END AS salary_group,

        COUNT(*) AS employee_count,

        SUM(
            CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END
        ) AS employees_left,

        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate

    FROM employees

    GROUP BY salary_group

    ORDER BY
        CASE salary_group
            WHEN 'Below 4L' THEN 1
            WHEN '4L-6L' THEN 2
            WHEN '6L-8L' THEN 3
            ELSE 4
        END
""").fetchdf()

print(result.to_string(index=False))


# ---------------------------------------------------------
# 12. ABSENCE ANALYSIS
# ---------------------------------------------------------
print("\n12. ABSENCE ANALYSIS")

result = con.execute("""
    SELECT
        CASE
            WHEN absence_days <= 5 THEN '0-5 Days'
            WHEN absence_days <= 10 THEN '6-10 Days'
            WHEN absence_days <= 15 THEN '11-15 Days'
            ELSE '16+ Days'
        END AS absence_group,

        COUNT(*) AS employee_count,

        SUM(
            CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END
        ) AS employees_left,

        ROUND(
            100.0 *
            SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*),
            2
        ) AS attrition_rate

    FROM employees

    GROUP BY absence_group

    ORDER BY
        CASE absence_group
            WHEN '0-5 Days' THEN 1
            WHEN '6-10 Days' THEN 2
            WHEN '11-15 Days' THEN 3
            ELSE 4
        END
""").fetchdf()

print(result.to_string(index=False))


print("\n" + "=" * 70)
print("SQL ANALYSIS COMPLETED")
print("=" * 70)

con.close()