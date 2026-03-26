import pandas as pd


def load_transactions(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    expected = {"customer_id", "segment", "month", "spend", "visits"}
    if not expected.issubset(df.columns):
        raise ValueError("Missing required columns in transaction data")
    return df


def compute_loyalty_gap(df: pd.DataFrame) -> pd.DataFrame:
    """Compute average spend/visit by segment and gap from best segment."""
    agg = (
        df.groupby("segment")
        .agg(avg_spend_per_visit=("spend", lambda x: x.sum() / df.loc[x.index, "visits"].sum()),
             total_spend=("spend", "sum"),
             total_visits=("visits", "sum"))
        .reset_index()
    )

    best = agg["avg_spend_per_visit"].max()
    agg["loyalty_gap"] = best - agg["avg_spend_per_visit"]
    agg["suggested_action"] = agg.apply(
        lambda row: _suggest_action(row["segment"], row["loyalty_gap"]), axis=1
    )
    return agg.sort_values("loyalty_gap", ascending=False)


def _suggest_action(segment: str, gap: float) -> str:
    if gap <= 50:
        return "Maintain engagement"
    if gap <= 150:
        return "Increase personalized rewards"
    return "High priority retention program"
