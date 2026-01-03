# decision_policy.py

from dataclasses import dataclass

@dataclass
class DecisionResult:
    regime: str
    probability: float
    drift: float
    decision_state: str
    allowed_actions: list
    forbidden_actions: list
    risk_level: str
    escalation_required: bool
    owner: str


def decision_policy_engine(regime, prob, drift):
    # R2 – Stress regime
    if regime == "R2":
        return DecisionResult(
            regime=regime,
            probability=prob,
            drift=drift,
            decision_state="STRESS",
            allowed_actions=["Restrict", "Recovery"],
            forbidden_actions=["Marketing", "New Credit"],
            risk_level="High",
            escalation_required=(drift >= 15),
            owner="CRO"
        )

    # R1 – Warning regime
    elif regime == "R1":
        return DecisionResult(
            regime=regime,
            probability=prob,
            drift=drift,
            decision_state="WARNING",
            allowed_actions=["Soft Nudge", "Monitoring"],
            forbidden_actions=["Credit Increase"],
            risk_level="Medium",
            escalation_required=False,
            owner="Risk Manager"
        )

    # R0 – Stable regime
    else:
        return DecisionResult(
            regime=regime,
            probability=prob,
            drift=drift,
            decision_state="STABLE",
            allowed_actions=["Upsell", "Credit Increase", "Normal Ops"],
            forbidden_actions=["Aggressive Collections"],
            risk_level="Low",
            escalation_required=False,
            owner="Portfolio Head"
        )
 
