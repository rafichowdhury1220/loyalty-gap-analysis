# Loyalty Gap Analysis (IAM Engineer Demo)

A very simple Python project demonstrating a single feature: loyalty gap analysis with an IAM-style role-based permission guard. 

## Overview
- `src/auth.py`: basic role-based guard for feature access.
- `src/loyalty_gap.py`: business logic computing loyalty gap metrics.
- `src/main.py`: script entrypoint with a scenario run.
- `data/sample_transactions.csv`: sample transaction records.

## Feature
- Compute customer loyalty gap score by segment (High/Mid/Low) and identify closing opportunities.
- Use role `analyst` to allow analysis; `guest` denied.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## Notes
- Designed for `IAM Engineer` thinking:
  - minimal access control policy simulation
  - separation of concerns (auth + analysis)
  - extensible to real IAM providers later
