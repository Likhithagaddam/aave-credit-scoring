import json
import pandas as pd
from collections import defaultdict
from tqdm import tqdm

def load_and_engineer_features(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    wallet_data = defaultdict(lambda: {
        'deposit_count': 0, 'deposit_total': 0.0,
        'borrow_count': 0, 'borrow_total': 0.0,
        'repay_count': 0, 'repay_total': 0.0,
        'redeem_count': 0, 'redeem_total': 0.0,
        'liquidation_count': 0,
        'timestamps': []
    })

    for tx in tqdm(data):
        w = tx['userWallet']
        act = tx['action'].lower()
        amt = float(tx.get('actionData', {}).get('amount', 0))
        ts = tx.get('timestamp', None)

        if ts:
            wallet_data[w]['timestamps'].append(ts)

        if act == 'deposit':
            wallet_data[w]['deposit_count'] += 1
            wallet_data[w]['deposit_total'] += amt
        elif act == 'borrow':
            wallet_data[w]['borrow_count'] += 1
            wallet_data[w]['borrow_total'] += amt
        elif act == 'repay':
            wallet_data[w]['repay_count'] += 1
            wallet_data[w]['repay_total'] += amt
        elif act == 'redeemunderlying':
            wallet_data[w]['redeem_count'] += 1
            wallet_data[w]['redeem_total'] += amt
        elif act == 'liquidationcall':
            wallet_data[w]['liquidation_count'] += 1

    processed_data = []

    for wallet, stats in wallet_data.items():
        repay_ratio = stats['repay_total'] / stats['borrow_total'] if stats['borrow_total'] > 0 else 1.0
        duration = (max(stats['timestamps']) - min(stats['timestamps'])) / (3600 * 24) if stats['timestamps'] else 0
        processed_data.append({
            'wallet': wallet,
            'deposit_count': stats['deposit_count'],
            'deposit_total': stats['deposit_total'],
            'borrow_count': stats['borrow_count'],
            'borrow_total': stats['borrow_total'],
            'repay_count': stats['repay_count'],
            'repay_total': stats['repay_total'],
            'redeem_count': stats['redeem_count'],
            'redeem_total': stats['redeem_total'],
            'liquidation_count': stats['liquidation_count'],
            'repay_ratio': repay_ratio,
            'activity_days': duration
        })

    return pd.DataFrame(processed_data)
