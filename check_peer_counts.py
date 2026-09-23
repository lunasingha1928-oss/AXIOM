import sys
sys.path.insert(0, ".")

import pandas as pd
from app.services.benchmark_service import (
    SENTINEL_PROJECT_DEFAULTS,
    get_paimana_cohort_df,
    normalize_sector,
    peer_benchmark,
)

df = get_paimana_cohort_df()
print(f"Total projects in cohort df: {len(df)}")
print("Sector distribution across unique PAIMANA projects:")
print(df["normalized_sector"].value_counts().to_dict())
print()

results = []
for pid, meta in SENTINEL_PROJECT_DEFAULTS.items():
    res = peer_benchmark(pid, limit=6)
    results.append({
        "project_id": pid,
        "name": meta["name"][:35],
        "assigned_sector": meta["sector"],
        "canonical_sector": res["sector"],
        "peer_count": res["peer_count"],
        "cross_sector_fallback": res["cross_sector_fallback"],
    })

res_df = pd.DataFrame(results)
print("Sentinel 11 projects peer counts:")
print(res_df.to_string())
