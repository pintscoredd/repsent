from datetime import datetime
try:
    import pytz
except ImportError:
    pytz = None

def get_pst_time() -> str:
    if pytz:
        pst = pytz.timezone('America/Los_Angeles')
        return datetime.now(pst).strftime("%Y-%m-%d %H:%M:%S PST")
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S System Time")
