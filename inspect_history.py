import pandas as pd

# Check how many unique projects in project_monthly_history.csv and snapshot counts
hist = pd.read_csv('backend/data/infrasight/project_monthly_history.csv')
print(f"Total rows: {len(hist)}")
print(f"Unique projects: {hist['project_id'].nunique()}")
print(f"Month column unique sample: {sorted(hist['month'].dropna().astype(str).unique())[:10]}")
print()

# Check how many months of data a sample project has
sample = hist[hist['project_id'] == hist['project_id'].iloc[0]]
print(f"Sample project {hist['project_id'].iloc[0]}: {len(sample)} snapshot months")
print(sample[['month','physical_progress_percentage','revised_cost','current_expenditure']].head(5).to_string())
print()

# Check Sentinel project ids in the snapshot file - do any appear?
sentinel_ids = [
    'PS-RD-1042','PS-RL-2217','PS-PW-3308','PS-WT-4471','PS-RD-1088',
    'PS-RL-2340','PS-PW-3355','PS-WT-4502','PS-RD-1120','PS-RL-2401','PS-PW-3390'
]
snap = pd.read_csv('backend/data/infrasight/paimana_monthly_snapshots.csv',
                   usecols=['project_id','project_name','snapshot_date','approved_cost_cr',
                            'revised_cost_cr','cumulative_expenditure_cr','physical_progress',
                            'financial_progress','planned_completion_date','revised_completion_date','source_url'])
print(f"Paimana snapshots rows: {len(snap)}")
print(f"Paimana unique projects: {snap['project_id'].nunique()}")

# Check approved InfraSight matches
approved = {'N18000335': 'PS-PW-3355', 'N22000406': 'PS-RL-2340'}
for infra_id in approved:
    found = snap[snap['project_id'].astype(str) == str(infra_id)]
    hist_found = hist[hist['project_id'].astype(str) == str(infra_id)]
    print(f"  {infra_id}: {len(found)} paimana rows, {len(hist_found)} monthly_history rows")

# Also check N-format ids in project_monthly_history
sample_n = hist[hist['project_id'].astype(str).str.startswith('N')].head(3)
print("\nSample N-format ids in project_monthly_history:")
print(sample_n[['project_id','project_name','month']].head())
