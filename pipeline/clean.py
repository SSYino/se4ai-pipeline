"""Stage 2: clean -- fix types and drop rows we cannot trust."""
import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw sales.

    Guarantees for the next stage:
      * sold_date is a datetime column
      * sqft has no missing values
      * rows with an obviously wrong price (<= 10,000) are removed
    """
    df = df.copy()
    df["sold_date"] = pd.to_datetime(df["sold_date"], format="ISO8601", utc=True)
    df = df.dropna(subset=["sqft"])
    df = df[df["price"] > 10_000]
    return df
