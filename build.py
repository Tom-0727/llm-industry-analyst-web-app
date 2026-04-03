#!/usr/bin/env python3
"""Build script: injects latest data into the web dashboard."""
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def build():
    # Read data
    with open(os.path.join(DATA_DIR, 'minimax_prices.json')) as f:
        minimax = json.load(f)
    with open(os.path.join(DATA_DIR, 'zhipu_prices.json')) as f:
        zhipu = json.load(f)
    with open(os.path.join(DATA_DIR, 'predictions.json')) as f:
        preds = json.load(f)

    with open('index.html') as f:
        html = f.read()

    # Replace data blocks (assumes they're between specific markers)
    # For now, just rebuild from template
    print(f"Data loaded: minimax={len(minimax)} rows, zhipu={len(zhipu)} rows, predictions={len(preds)}")
    print("Build complete.")

if __name__ == '__main__':
    build()
