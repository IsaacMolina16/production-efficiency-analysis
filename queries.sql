-- =========================
-- Production Summary + Risk (Improved)
-- =========================
WITH machine_summary AS (
    SELECT 
        machine_id,
        SUM(units_produced) AS total_units,
        SUM(downtime_minutes) AS total_downtime,
        SUM(defects) AS total_defects
    FROM production
    GROUP BY machine_id
),

metrics AS (
    SELECT *,
        total_units * 1.0 / NULLIF(total_units + total_downtime, 0) AS efficiency,
        total_defects * 1.0 / NULLIF(total_units, 0) AS defect_rate
    FROM machine_summary
),

threshold AS (
    SELECT AVG(defect_rate) AS avg_defect_rate
    FROM metrics
)

SELECT 
    m.machine_id,
    m.total_units,
    m.total_downtime,
    m.total_defects,
    m.efficiency,
    m.defect_rate,

    CASE 
        WHEN m.defect_rate > t.avg_defect_rate THEN 'High Risk'
        ELSE 'Low Risk'
    END AS risk_level

FROM metrics m
CROSS JOIN threshold t
ORDER BY m.defect_rate DESC;
