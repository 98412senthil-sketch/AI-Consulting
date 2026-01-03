# Decision Control Layer – Regime AI System

## Background
This document defines the Decision Control Layer for a regime-aware AI system.  
The objective of this layer is to translate probabilistic regime outputs into controlled, auditable, and risk-aware business actions.  
The model itself does not make decisions.  
It classifies latent business regimes and exposes uncertainty and drift.  
All business actions are governed by this control layer.

## Analysis
The Latent Regime Model identifies hidden operational states that are not directly observable through transactional KPIs.  
Each regime represents a materially different business risk posture.  
Drift within a regime represents deterioration of model reliability and business stability.  
Without a decision control layer, downstream systems may act aggressively during unstable or high-risk regimes, leading to financial and compliance exposure.

## Regime Governance Table

| Regime | Probability | Drift % | Business State | Allowed Actions | Forbidden Actions | Risk Level | Decision Owner | Review Required |
|-------|------------|--------|---------------|----------------|------------------|-----------|---------------|----------------|
| R0 | 0.72 | 3.2 | Stable | Upsell, Credit increase, Normal ops | Aggressive collections | Low | Portfolio Head | No |
| R1 | 0.21 | 8.7 | Warning | Soft nudges, Monitoring | Credit increase | Medium | Risk Manager | No |
| R2 | 0.07 | 17.9 | Stress | Restrict, Recovery actions | Marketing, New credit | High | CRO | Yes |
