import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("decision_log.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 1. Regime Distribution
df["regime"].value_counts().plot(kind="bar", title="Regime Distribution")
plt.savefig("regime_distribution.png")
plt.clf()

# 2. High Risk Escalations
df[df["escalation_required"] == True]["regime"].value_counts().plot(
    kind="bar", title="Escalations by Regime"
)
plt.savefig("escalations_by_regime.png")
plt.clf()

# 3. Drift Monitoring
df.groupby("regime")["drift"].mean().plot(kind="bar", title="Average Drift by Regime")
plt.savefig("avg_drift_by_regime.png")
plt.clf()

