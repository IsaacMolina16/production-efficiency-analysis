import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# CONFIG
# =========================
DATA_PATH = 'production_data.csv'
OUTPUT_PATH = 'outputs'
os.makedirs(OUTPUT_PATH, exist_ok=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# METRICS (MEJOR DEFINIDAS)
# =========================
df['defect_rate'] = df['defects'] / df['units_produced']

# Avoid division by zero cleanly
df['downtime_ratio'] = df['downtime_minutes'] / (df['units_produced'] + 1)

# =========================
# AGGREGATION
# =========================
machine_perf = df.groupby('machine_id').agg({
    'units_produced': 'sum',
    'downtime_minutes': 'sum',
    'defects': 'sum',
    'defect_rate': 'mean',
    'downtime_ratio': 'mean'
}).reset_index()

# =========================
# RISK CLASSIFICATION (DATA-DRIVEN)
# =========================
threshold = machine_perf['defect_rate'].mean()

machine_perf['risk'] = machine_perf['defect_rate'].apply(
    lambda x: 'High Risk' if x > threshold else 'Low Risk'
)

# =========================
# BAR CHART
# =========================
plt.figure()

plt.bar(machine_perf['machine_id'], machine_perf['defect_rate'])

plt.xlabel("Machine")
plt.ylabel("Defect Rate")
plt.title("Defect Rate by Machine")

plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}/defect_rate.png")
plt.close()

# =========================
# HISTOGRAM
# =========================
plt.figure()

plt.hist(df['defect_rate'], bins=5)

plt.xlabel("Defect Rate")
plt.ylabel("Frequency")
plt.title("Defect Rate Distribution")

plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}/distribution.png")
plt.close()

# =========================
# INSIGHTS
# =========================
worst_machine = machine_perf.sort_values(by='defect_rate', ascending=False).head(1)

print("\n=== WORST MACHINE ===")
print(worst_machine)

print("\n=== SUMMARY ===")
print(machine_perf)
