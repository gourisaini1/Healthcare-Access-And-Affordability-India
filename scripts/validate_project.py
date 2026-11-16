from pathlib import Path
import json
import pandas as pd
from scipy.stats import pearsonr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Dataset"
NOTEBOOKS = ROOT / "Notebooks"

nha = pd.read_csv(DATA / "national_health_accounts_india_2013_14_to_2023_24.csv")
spend = pd.read_csv(DATA / "state_health_expenditure_share_rbi_2024_25_re.csv")
imr = pd.read_csv(DATA / "state_infant_mortality_rate_2023.csv")
beds = pd.read_csv(DATA / "state_government_hospitals_and_beds_rbi_handbook_2024_25.csv")
matched = pd.read_csv(DATA / "state_health_spending_imr_matched_exploratory.csv")

assert len(nha) == 11 and nha.financial_year.is_monotonic_increasing
assert nha.financial_year.iloc[-1] == "2023-24"
assert spend.state_ut.is_unique and len(spend) == 31
assert spend.health_expenditure_share_aggregate_2024_25_re_pct.between(0, 100).all()
assert imr.state_ut.is_unique
assert beds.state_ut.is_unique
assert len(matched) == 31
r, p = pearsonr(matched.health_expenditure_share_2024_25_re_pct,
                matched.infant_mortality_rate_2023_per_1000_live_births)
assert abs(r - 0.0443) < 0.002, r

for path in NOTEBOOKS.glob("*.ipynb"):
    with path.open(encoding="utf-8") as f:
        nb = json.load(f)
    assert nb.get("nbformat") == 4, path.name
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            compile("".join(cell.get("source", [])), f"{path.name}:cell", "exec")

print("CSV, notebook syntax and analytical checks passed.")
print(f"NHA rows: {len(nha)}; state budget rows: {len(spend)}; matched state rows: {len(matched)}")
print(f"Pearson r: {r:.4f}; p-value: {p:.4f}")
print("Note: this static QA does not replace end-to-end notebook execution.")
