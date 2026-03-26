import os

from auth import IAMGate, AuthError
from loyalty_gap import load_transactions, compute_loyalty_gap


def run(role: str = "analyst"):
    gate = IAMGate(role)
    gate.check("run_loyalty_gap_analysis")

    base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_path = os.path.join(base, "data", "sample_transactions.csv")

    df = load_transactions(data_path)
    result = compute_loyalty_gap(df)

    print(f"=== Loyalty Gap Analysis for role: {role} ===")
    print(result.to_string(index=False, float_format="{:.2f}".format))


if __name__ == "__main__":
    try:
        run("analyst")
    except AuthError as e:
        print(f"Authorization failed: {e}")
