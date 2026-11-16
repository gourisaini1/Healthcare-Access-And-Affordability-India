# Dataset catalogue and handling guide

This directory contains the source-derived CSV files used by the eight analysis notebooks, alongside data dictionaries documenting definitions, units, source references and limitations.

**Important:** the datasets do not all describe the same year, geography or unit of analysis. Read the relevant dictionary before joining or comparing files. Missing, suppressed or not-reported values remain missing; they are not zeros.

## Analysis-ready CSV catalogue

| File | Coverage / reference period | Role in the project | Documentation |
|---|---|---|---|
| `national_health_accounts_india_2013_14_to_2023_24.csv` | India, FY2013–14 to FY2023–24 | National health-financing mix and OOPE trend | [NHA dictionary](NHA_DATA_DICTIONARY.md) |
| `state_health_expenditure_share_rbi_2024_25_re.csv` | 31 states/UTs, FY2023–24 and FY2024–25 Revised Estimates | State public-health budget composition | [State expenditure dictionary](STATE_HEALTH_EXPENDITURE_DATA_DICTIONARY.md) |
| `state_infant_mortality_rate_2023.csv` | State/UT, calendar 2023 | Infant mortality per 1,000 live births | [IMR dictionary](IMR_DATA_DICTIONARY.md) |
| `state_rural_phc_doctors_2023.csv` | 36 state/UT rows, calendar 2023 | Rural PHC doctors in position and reported requirement | [PHC doctors dictionary](PHC_DOCTORS_DATA_DICTIONARY.md) |
| `state_socioeconomic_covariates_nfhs5_rbi.csv` | State/UT; female literacy NFHS-5 2019–21; per-capita NSDP FY2021–22 | Socioeconomic controls for Notebook 07 | [Socioeconomic covariates dictionary](SOCIOECONOMIC_COVARIATES_DATA_DICTIONARY.md) |
| `state_government_hospitals_and_beds_rbi_handbook_2024_25.csv` | State/UT; source table does not specify a distinct observation year | Earlier government hospital and bed-count comparison | [Hospitals and beds dictionary](HOSPITALS_BEDS_DATA_DICTIONARY.md) |
| `state_government_hospital_beds_nhp2023_per_1000.csv` | 36 states/UTs; beds 31 Dec 2022; projected population 1 Mar 2021 | Government hospital beds per 1,000 projected population | [NHP beds dictionary](HOSPITAL_BEDS_NHP2023_DATA_DICTIONARY.md) |
| `state_health_spending_imr_matched_exploratory.csv` | 31 matched states/UTs | Derived state budget-share / IMR comparison used in exploratory analysis | See source dictionaries for component definitions |

## How the datasets are used

- **National financing:** Notebook 01 examines the national time series. OOPE and government shares describe the composition of health financing; they are not household-level catastrophic expenditure measures.
- **State budgets and outcomes:** Notebooks 02, 03 and 05 compare state budget composition and infant mortality. The budget share is not per-capita spending or health-system quality.
- **Hospital infrastructure:** Notebook 04 analyses the earlier RBI hospital/bed table. Notebook 08 uses the dated NHP-2023 bed count and projected population to calculate beds per 1,000.
- **Rural PHC workforce:** Notebook 06 calculates doctors in position divided by the source-reported requirement. Notebook 07 combines that ratio with 2023 IMR and two socioeconomic controls.
- **Derived matched data:** `state_health_spending_imr_matched_exploratory.csv` is a prepared analytical join, not an independent primary source.

## Data handling rules

1. **Preserve missingness.** Blank, dash, asterisk or suppressed source values are not interpreted as zero unless the source explicitly defines them as zero.
2. **Respect reference periods.** The 2024–25 expenditure observations are Revised Estimates (RE), not final audited actuals. The rural PHC staffing and IMR datasets refer to calendar year 2023.
3. **Do not overstate the staffing ratio.** The PHC coverage ratio is doctors in position divided by the source-reported required rural PHC doctor posts. It is not doctors per capita, population need or a measure of equitable distribution.
4. **Keep nominal values nominal.** Per-capita NSDP is at current prices for FY2021–22; it is not inflation-adjusted real income or household consumption.
5. **Keep survey definitions intact.** Female literacy is the NFHS-5 measure for women aged 15–49 (2019–21), not Census literacy for all women.
6. **Disclose the bed-count date gap.** NHP-2023 beds are dated 31 December 2022; the projected population denominator is dated 1 March 2021, about 21 months earlier.
7. **Do not reconcile away source inconsistencies.** The NHP state/UT bed rows do not sum to the published India aggregate. The discrepancy is documented in Notebook 08 and the research report; state rates use published state rows, and no national rate is calculated from the inconsistent totals.
8. **Do not infer causality from joins or correlations.** All state-level associations are exploratory and may reflect omitted socioeconomic, demographic or health-system factors.

## Raw source staging

The `Raw_Data/` subdirectory contains source-retrieval notes and instructions for preserving original downloads. It is a staging/documentation area; the analysis notebooks use the documented CSV files in this directory. Do not overwrite original source files when updating a transcription. Record retrieval date, source table/page, units, original labels and any transformation applied.

See [Raw_Data/README.md](Raw_Data/README.md) for source acquisition notes.
