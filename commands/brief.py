from utils.formatting import print_header, print_table
from api.yahoo import get_current_price
from api.coingecko import get_crypto_price

def execute_brief():
    print_header("SENTINEL MACRO BRIEF")
    spy = get_current_price("SPY")
    dxy = get_current_price("DX-Y.NYB")
    tnx = get_current_price("^TNX")
    gold = get_current_price("GC=F")
    btc = get_crypto_price("bitcoin")
    
    data = [
        ["SPY", f"${spy:.2f}"],
        ["DXY", f"{dxy:.2f}"],
        ["10Y Yield", f"{tnx:.2f}%"],
        ["Gold", f"${gold:.2f}"],
        ["Bitcoin", f"${btc:.2f}"]
    ]
    print_table("Current Market Snapshot", ["Asset", "Price/Level"], data)
