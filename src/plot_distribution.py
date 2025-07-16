import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/wallet_scores.csv")
bins = list(range(0, 1100, 100))
df['score_range'] = pd.cut(df['credit_score'], bins)
df['score_range'].value_counts().sort_index().plot(kind='bar')
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("output/score_distribution.png")
plt.show()
