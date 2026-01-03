import csv
from datetime import datetime

LOG_FILE = "decision_log.csv"

def log_decision(decision):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            decision.regime,
            decision.probability,
            decision.drift,
            decision.decision_state,
            decision.risk_level,
            decision.owner,
            decision.escalation_required
        ])
 
