*Production Efficiency & Machine Risk Analysis*

-Project Overview-
This project analyzes production data to evaluate machine performance, identify inefficiencies, and classify operational risk using data analysis techniques in Python and SQL.

-Objective-
*Analyze production performance across machines
*Identify underperforming machines based on efficiency
*Classify machines by operational risk
*Support decision-making for maintenance and optimization
*Dataset

-The dataset includes:-

*Machine ID
*Units produced
*Downtime (minutes)
*Number of defects

-Tools & Technologies-
*Python (Pandas, Matplotlib)
*SQL

-Analysis Performed-
1. Efficiency KPI
Calculated machine efficiency using:

units_produced / downtime_minutes

2. Aggregated Machine Performance
Grouped data by machine to evaluate:

*Total production
*Total downtime
*Total defects
*Average efficiency

3. Risk Classification
Machines were classified based on efficiency:

*High Risk → Low efficiency
*Low Risk → High efficiency

This enables prioritization of maintenance efforts.

4. SQL Analysis

Developed SQL queries to:

*Aggregate production metrics
*Calculate efficiency
*Classify machines by risk level
*Analyze defect rate

-Visualizations-
Machine Efficiency
Efficiency Distribution

-Key Insights-
*Some machines produce high output but suffer from excessive downtime
*Efficiency varies significantly across machines
*High-risk machines can be identified using simple KPIs
*Defect rate analysis highlights quality issues

-Business Impact-
*Enables identification of underperforming machines
*Supports targeted maintenance decisions
*Improves resource allocation
*Provides foundation for predictive maintenance

-Future Improvements-
*Implement predictive models for failure detection
*Integrate real-time production data
*Build interactive dashboards