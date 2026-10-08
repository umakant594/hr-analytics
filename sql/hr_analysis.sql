-- ============================================================
-- HR ANALYTICS - SQL ANALYSIS
-- ============================================================

-- 1. Total Employees
SELECT COUNT(*) AS total_employees
FROM employees;


-- 2. Attrition Count
SELECT
    attrition,
    COUNT(*) AS employee_count
FROM employees
GROUP BY attrition;


-- 3. Attrition Rate
SELECT
    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees;


-- 4. Average Salary
SELECT
    ROUND(AVG(salary), 2) AS average_salary
FROM employees;


-- 5. Department Analysis
SELECT
    department,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS average_salary,
    ROUND(AVG(experience), 2) AS average_experience
FROM employees
GROUP BY department
ORDER BY employee_count DESC;


-- 6. Department Attrition
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY department
ORDER BY attrition_rate DESC;


-- 7. Experience Analysis
SELECT
    CASE
        WHEN experience <= 2 THEN '0-2 Years'
        WHEN experience <= 5 THEN '3-5 Years'
        WHEN experience <= 10 THEN '6-10 Years'
        ELSE '10+ Years'
    END AS experience_group,

    COUNT(*) AS employee_count,

    SUM(
        CASE WHEN attrition = TRUE THEN 1 ELSE 0 END
    ) AS employees_left,

    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate

FROM employees

GROUP BY experience_group;


-- 8. Performance Analysis
SELECT
    performance,
    COUNT(*) AS employee_count,

    SUM(
        CASE WHEN attrition = TRUE THEN 1 ELSE 0 END
    ) AS employees_left,

    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate

FROM employees

GROUP BY performance

ORDER BY performance;


-- 9. Satisfaction Analysis
SELECT
    satisfaction,
    COUNT(*) AS employee_count,

    SUM(
        CASE WHEN attrition = TRUE THEN 1 ELSE 0 END
    ) AS employees_left,

    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate

FROM employees

GROUP BY satisfaction

ORDER BY satisfaction;


-- 10. Salary Analysis
SELECT
    CASE
        WHEN salary < 400000 THEN 'Below 4L'
        WHEN salary < 600000 THEN '4L-6L'
        WHEN salary < 800000 THEN '6L-8L'
        ELSE '8L+'
    END AS salary_group,

    COUNT(*) AS employee_count,

    SUM(
        CASE WHEN attrition = TRUE THEN 1 ELSE 0 END
    ) AS employees_left,

    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate

FROM employees

GROUP BY salary_group;


-- 11. Absence Analysis
SELECT
    CASE
        WHEN absence_days <= 5 THEN '0-5 Days'
        WHEN absence_days <= 10 THEN '6-10 Days'
        WHEN absence_days <= 15 THEN '11-15 Days'
        ELSE '16+ Days'
    END AS absence_group,

    COUNT(*) AS employee_count,

    SUM(
        CASE WHEN attrition = TRUE THEN 1 ELSE 0 END
    ) AS employees_left,

    ROUND(
        100.0 *
        SUM(CASE WHEN attrition = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate

FROM employees

GROUP BY absence_group;