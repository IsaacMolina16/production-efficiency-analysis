-- =========================
-- Query 1: Production Summary + Risk
-- =========================
SELECT 
    machine_id,
    SUM(units_produced) AS total_units,
    SUM(downtime_minutes) AS total_downtime,
    SUM(defects) AS total_defects,

    SUM(units_produced) / (SUM(downtime_minutes) + 1) AS efficiency,

    CASE 
        WHEN SUM(units_produced) / (SUM(downtime_minutes) + 1) < 8 THEN 'High Risk'
        ELSE 'Low Risk'
    END AS risk_level

FROM production
GROUP BY machine_id
ORDER BY efficiency ASC;


-- =========================
-- Query 2: Defect Rate Analysis
-- =========================
SELECT 
    machine_id,
    SUM(defects) * 1.0 / SUM(units_produced) AS defect_rate
FROM production
GROUP BY machine_id
ORDER BY defect_rate DESC;