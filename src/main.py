from preprocess import load_and_engineer_features
from scoring_model import compute_scores
import pandas as pd

df = load_and_engineer_features("data/user_transactions.json")
df["credit_score"] = compute_scores(df)
df.to_csv("output/wallet_scores.csv", index=False)
print("✅ Scores written to output/wallet_scores.csv")
