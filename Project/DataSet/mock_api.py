###############################################################
# Mock API Server for Workshop
# Serves synthetic API data at:
#   http://127.0.0.1:8000/transactions
#
# Start using:
#   uvicorn mock_api:app --reload --host 127.0.0.1 --port 8000
###############################################################

import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# -------- CONFIG --------
DATA_DIR = Path(__file__).resolve().parent
API_CSV = DATA_DIR / "api.csv"

# -------- LOAD DATA ONCE --------
if not API_CSV.exists():
    raise FileNotFoundError(f"API CSV not found: {API_CSV}")

df_api = pd.read_csv(API_CSV, dtype=str).fillna("")

# -------- FASTAPI APP --------
app = FastAPI(title="Mock Visa API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------- ENDPOINT --------
@app.get("/transactions")
def get_transactions(
    count: int = Query(1000, ge=1, le=5000),
    page: int = Query(1, ge=1)
):
    """
    Returns paginated synthetic transaction data.
    Workshop client fetches using:
        http://127.0.0.1:8000/transactions?count=1000&page=1
    """
    total_rows = len(df_api)
    start = (page - 1) * count
    end = start + count

    if start >= total_rows:
        # no more data
        return {
            "page": page,
            "count": 0,
            "data": []
        }

    batch = df_api.iloc[start:end].to_dict(orient="records")

    return {
        "page": page,
        "count": len(batch),
        "data": batch
    }

# Optional: health check
@app.get("/")
def health():
    return {"status": "ok", "rows_loaded": len(df_api)}
