from pathlib import Path
import json
import pandas as pd
from scipy.stats import pearsonr, spearmanr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Dataset"
NOTEBOOKS = ROOT / "Notebooks"

nha = pd.read_csv(DATA / "national_health_accounts_india_2013_14_to_2023_24.csv")
spend = pd.read_csv(DATA / "state_health_expenditure_share_rbi_2024_25_re.csv")
imr = pd.read_csv(DATA / "state_infant_mortality_rate_2023.csv")
beds = pd.read_csv(DATA / "state_government_hospitals_and_beds_rbi_handbook_2024_25.csv")
matched = pd.read_csv(DATA / "state_health_spending_imr_matched_exploratory.csv")
staff = pd.read_csv(DATA / "state_rural_phc_doctors_2023.csv")
socio = pd.read_csv(DATA / "state_socioeconomic_covariates_nfhs5_rbi.csv")
beds_pc = pd.read_csv(DATA / "state_government_hospital_beds_nhp2023_per_1000.csv")
insurance = pd.read_csv(DATA / "state_health_insurance_coverage_nfhs5.csv")

assert len(nha) == 11 and nha.financial_year.is_monotonic_increasing
assert nha.financial_year.iloc[-1] == "2023-24"
assert spend.state_ut.is_unique and len(spend) == 31
assert spend.health_expenditure_share_aggregate_2024_25_re_pct.between(0, 100).all()
assert imr.state_ut.is_unique
assert beds.state_ut.is_unique
assert len(matched) == 31
assert staff.state_ut.is_unique and len(staff) > 0
assert staff.reference_year.eq(2023).all()
assert staff.required_rural_phc_doctors.ge(0).all()
assert socio.state_ut.is_unique and len(socio) > 0
assert socio.female_literacy_nfhs5_pct.between(0, 100).all()
assert socio.per_capita_nsdp_2021_22_inr.notna().sum() == 33
assert insurance.state_ut.is_unique and len(insurance) == 36
assert insurance.households_any_member_covered_pct.between(0, 100).all()
assert insurance.reference_period.eq("2019-21").all()
assert beds_pc.state_ut.is_unique and len(beds_pc) > 0
assert beds_pc.beds_reference_date.eq("2022-12-31").all()
assert beds_pc.population_reference_date.eq("2021-03-01").all()
assert (beds_pc.beds_per_1000_population - beds_pc.beds_total_nhp2023 / beds_pc.population_2021_projected_thousands).abs().max() < 0.00011

r_budget, p_budget = pearsonr(
    matched.health_expenditure_share_2024_25_re_pct,
    matched.infant_mortality_rate_2023_per_1000_live_births,
)
assert abs(r_budget - 0.0443) < 0.002, r_budget

imr_states = imr.loc[~imr.state_ut.eq("All India")].dropna(
    subset=["infant_mortality_rate_2023_per_1000_live_births"]
).copy()
staff = staff.copy()
staff["state_key"] = staff.state_ut.replace({
    "Dadra & Nagar Haveli & Daman & Diu":
    "Dadra & Nagar Haveli (includes Daman & Diu)"
})
imr_states["state_key"] = imr_states.state_ut
workforce = staff.merge(
    imr_states[["state_key", "infant_mortality_rate_2023_per_1000_live_births"]],
    on="state_key",
    how="inner",
    validate="one_to_one",
)
workforce["coverage_ratio"] = (
    workforce.in_position_rural_phc_doctors
    / workforce.required_rural_phc_doctors.where(
        workforce.required_rural_phc_doctors > 0
    )
)
workforce = workforce.dropna(subset=["coverage_ratio"])
r_staff, p_staff = pearsonr(
    workforce.coverage_ratio,
    workforce.infant_mortality_rate_2023_per_1000_live_births,
)
rho_staff, p_rho_staff = spearmanr(
    workforce.coverage_ratio,
    workforce.infant_mortality_rate_2023_per_1000_live_births,
)
socio_analysis = workforce.merge(socio, on="state_ut", how="left", validate="one_to_one")
socio_analysis["log_nsdp"] = __import__("numpy").log(
    pd.to_numeric(socio_analysis.per_capita_nsdp_2021_22_inr, errors="coerce")
)
adjusted_sample = socio_analysis.dropna(
    subset=["female_literacy_nfhs5_pct", "log_nsdp"]
)
# Guard against broken joins or unexpected sample loss, not merely empty outputs.
assert 30 <= len(workforce) <= 36, len(workforce)
assert 28 <= len(adjusted_sample) <= 34, len(adjusted_sample)
assert -0.70 < r_staff < -0.35, r_staff
assert -0.70 < rho_staff < -0.35, rho_staff
assert adjusted_sample[["female_literacy_nfhs5_pct", "log_nsdp"]].notna().all().all()

notebooks = sorted(NOTEBOOKS.glob("*.ipynb"))
assert len(notebooks) == 9, [p.name for p in notebooks]
assert not (DATA / "Notebooks").exists(), "Duplicate notebook tree should not exist"
for path in notebooks:
    with path.open(encoding="utf-8") as f:
        nb = json.load(f)
    assert nb.get("nbformat") == 4, path.name
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            compile("".join(cell.get("source", [])), f"{path.name}:cell", "exec")

print("CSV, notebook syntax, duplicate-tree and analytical checks passed.")
print(f"NHA rows: {len(nha)}; state budget rows: {len(spend)}; matched budget/IMR rows: {len(matched)}")
print(f"Budget-share vs IMR: Pearson r={r_budget:.4f}, p={p_budget:.4f}")
print(f"Rural PHC staffing vs IMR: n={len(workforce)}, Pearson r={r_staff:.4f}, p={p_staff:.4f}")
print(f"Rural PHC staffing vs IMR: Spearman rho={rho_staff:.4f}, p={p_rho_staff:.4f}")
print(f"Socioeconomic covariates: {len(socio)} rows; NSDP non-missing={socio.per_capita_nsdp_2021_22_inr.notna().sum()}")
print(f"Government beds per 1,000 population: {len(beds_pc)} state/UT rows")
print(f"NFHS-5 household insurance coverage: {len(insurance)} state/UT rows; coverage–NSDP Pearson r={r_insurance_nsdp:.4f}, p={p_insurance_nsdp:.4f}, n={len(insurance_analysis)}")
print(f"Adjusted complete-case model sample: {len(adjusted_sample)}; excluded: {sorted(set(workforce.state_ut) - set(adjusted_sample.state_ut))}")
