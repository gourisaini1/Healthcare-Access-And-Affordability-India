# Dataset catalogue

This folder contains the source-derived datasets used in the project. Read each data dictionary before combining datasets: reference years, units, coverage and definitions differ.

| File | Coverage | Main source |
|---|---|---|
| `national_health_accounts_india_2013_14_to_2023_24.csv` | India, 2013–14 to 2023–24 | NHSRC / MoHFW, National Health Accounts |
| `state_health_expenditure_share_rbi_2024_25_re.csv` | 31 states/UTs, 2023–24 and 2024–25 RE | RBI, State Finances 2025–26, Statement 27 |
| `state_infant_mortality_rate_2023.csv` | States/UTs, calendar 2023 | SRS, reproduced in RBI Handbook 2024–25, Table 4 |
| `state_government_hospitals_and_beds_rbi_handbook_2024_25.csv` | States/UTs; source table reference year unspecified | National Health Profile, reproduced in RBI Handbook 2024–25, Table 17 |
| `state_health_spending_imr_matched_exploratory.csv` | 31 matched states/UTs | Derived join of RBI Statement 27 and SRS IMR |

## Data handling rules

- Blank values represent unavailable/not separately reported data; they are not zeros.
- 2024–25 state health expenditure values are Revised Estimates (RE), not final audited actuals.
- The 2023 IMR series is not relabelled as 2024–25.
- Hospital and bed counts are not labelled 2024–25 because the RBI table does not state a distinct observation year.
- Derived datasets retain source reference periods and are used for descriptive analysis only.

See the accompanying `*_DATA_DICTIONARY.md` files for definitions, source links and limitations.
