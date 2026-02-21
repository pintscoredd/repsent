import numpy as np

def find_analog(asset: str, current_trend: list) -> str:
    analogs = {
        "Dot Com Bubble (2000)": [1, 2, 3, 4, -1, -3, -5],
        "GFC (2008)": [1, 1, -1, -2, -4, -6, -8],
        "COVID Crash (2020)": [2, 1, -5, -10, 5, 8, 10],
        "Post-COVID Rally (2021)": [2, 3, 2, 4, 3, 5, 2]
    }
    
    best_match = "No strong analog"
    highest_corr = -1.0
    
    if len(current_trend) < 7:
        current_trend = (current_trend + [0]*7)[:7]
        
    curr_arr = np.array(current_trend[-7:])
    std_curr = np.std(curr_arr)
    if std_curr == 0:
        return best_match
        
    for name, pattern in analogs.items():
        pat_arr = np.array(pattern)
        if np.std(pat_arr) == 0:
            continue
        corr = np.corrcoef(curr_arr, pat_arr)[0, 1]
        if corr > highest_corr and corr > 0.6:
            highest_corr = corr
            best_match = f"{name} (Correlation: {corr:.2f})"
            
    return best_match
