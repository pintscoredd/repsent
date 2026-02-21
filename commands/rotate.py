from utils.formatting import print_header, print_table
from engines.cross_asset import compute_rolling_correlations

def execute_rotate():
    print_header("CROSS-ASSET ROTATION & CORRELATION (60-DAY)")
    corr = compute_rolling_correlations()
    if corr.empty:
        return
        
    corr = corr.reset_index()
    columns = ["Asset"] + list(corr.columns[1:])
    rows = []
    for _, row in corr.iterrows():
        rows.append([row[c] if isinstance(row[c], str) else f"{row[c]:.2f}" for c in columns])
        
    print_table("Asset Correlations", columns, rows)
