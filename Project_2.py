import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# DEBUG: Ver archivos
# =========================
print("Files in directory:", os.listdir())

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("production_data.csv")

print("\nSample Data:\n")
print(df.head())

# =========================
# KPI: Efficiency
# =========================
df['efficiency'] = df['units_produced'] / (df['downtime_minutes'] + 1)

# =========================
# AGGREGATION BY MACHINE
# =========================
machine_perf = df.groupby('machine_id').agg({
    'units_produced': 'sum',
    'downtime_minutes': 'sum',
    'defects': 'sum',
    'efficiency': 'mean'
}).reset_index()

print("\nMachine Performance:\n")
print(machine_perf)

# =========================
# RISK CLASSIFICATION
# =========================
machine_perf['risk'] = machine_perf['efficiency'].apply(
    lambda x: 'High Risk' if x < 8 else 'Low Risk'
)

print("\nRisk Classification:\n")
print(machine_perf[['machine_id', 'efficiency', 'risk']])

# =========================
# BAR CHART WITH RISK
# =========================
plt.figure()

colors = machine_perf['risk'].map({
    'High Risk': 'red',
    'Low Risk': 'green'
})

plt.bar(machine_perf['machine_id'], machine_perf['efficiency'])

plt.xlabel("Machine")
plt.ylabel("Efficiency")
plt.title("Machine Efficiency with Risk Classification")

plt.tight_layout()
plt.savefig("efficiency_chart.png")
plt.show()

# =========================
# HIGH RISK MACHINES
# =========================
high_risk = machine_perf[machine_perf['risk'] == 'High Risk']

print("\nHigh Risk Machines:\n")
print(high_risk)

# =========================
# HISTOGRAM (DISTRIBUTION)
# =========================
plt.figure()

plt.hist(df['efficiency'], bins=5)

plt.xlabel("Efficiency")
plt.ylabel("Frequency")
plt.title("Efficiency Distribution")

plt.tight_layout()
plt.savefig("efficiency_distribution.png")
plt.show()