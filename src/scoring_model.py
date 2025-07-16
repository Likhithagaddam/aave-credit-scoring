def compute_scores(df):
    def score_row(row):
        score = 0
        if row['deposit_total'] > 1000:
            score += 150
        elif row['deposit_total'] > 100:
            score += 100
        else:
            score += 50

        if row['repay_ratio'] >= 0.9:
            score += 200
        elif row['repay_ratio'] >= 0.5:
            score += 100
        else:
            score += 30

        score += max(0, 200 - row['liquidation_count'] * 70)

        if row['borrow_total'] > 500:
            score += 100

        if row['activity_days'] > 30:
            score += 100
        elif row['activity_days'] > 10:
            score += 50

        score += min(row['redeem_count'] * 10, 50)

        return min(score, 1000)

    return df.apply(score_row, axis=1)
