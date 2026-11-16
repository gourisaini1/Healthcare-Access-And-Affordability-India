# Dataset catalogue

All source-derived data used in the analysis are stored here. Check each data dictionary before combining files: reference periods, units, coverage and definitions differ.

| File | Coverage / reference period | Use |
|---|---|---|
| `national_health_accounts_india_2013_14_to_2023_24.csv` | India, FY2013–14 to FY2023–24 | National financing mix and OOPE trend |
| `state_health_expenditure_share_rbi_2024_25_re.csv` | 31 states/UTs, FY2023–24 and FY2024–25 RE | State public health budget shares |
| `state_infant_mortality_rate_2023.csv` | States/UTs, calendar 2023 | Infant mortality comparison |
| `state_rural_phc_doctors_2023.csv` | 36 state/UT rows, calendar 2023 | Rural PHC doctor staffing relative to reported requirement |
| `state_government_hospitals_and_beds_rbi_handbook_2024_25.csv` | States/UTs; source observation year unspecified | Absolute public hospital and bed counts |
| `state_health_spending_imr_matched_exploratory.csv` | 31 matched states/UTs | Derived exploratory join of budget shares and IMR |

## Data handling rules

- Blank values represent unavailable, suppressed or not separately reported values; they are not zeros.
- The 2024–25 expenditure values are Revised Estimates (RE), not final audited actuals.
- The 2023 IMR and rural PHC staffing datasets refer to calendar year 2023.
- The RBI hospital/bed table does not state a distinct observation year; do not label it as 2024–25 observations.
- The PHC staffing coverage ratio is in-position rural PHC doctors divided by the source-reported requirement. It is not doctors per capita.
- Derived datasets preserve their reference periods and are used for descriptive analysis only.

See the relevant `*_DATA_DICTIONARY.md` files for definitions, source links and limitations.
