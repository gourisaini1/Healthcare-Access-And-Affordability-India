# Analysis notebooks

Run from this directory in numerical order. Each notebook reads source files from `../Dataset/`.

| Notebook | Purpose |
|---|---|
| `01_National_Health_Accounts_Analysis.ipynb` | National financing trends, 2013–14 to 2023–24 |
| `02_State_Health_Expenditure_Analysis.ipynb` | State/UT public health budget shares, 2023–24 and 2024–25 RE |
| `03_Health_Outcomes_and_Expenditure.ipynb` | State infant mortality and exploratory budget-share comparison |
| `04_State_Hospital_Infrastructure_Analysis.ipynb` | Initial government hospital and bed infrastructure analysis |
| `05_Correlation_and_Regression_Analysis.ipynb` | Pearson, Spearman and simple regression for the budget-share/IMR comparison |
| `06_Rural_Workforce_and_Health_Outcomes.ipynb` | 2023 rural PHC doctor staffing benchmark and infant mortality; denominator sensitivity |
| `07_Adjusted_Workforce_IMR_Regression.ipynb` | Exploratory HC3-robust regression controlling for NFHS-5 female literacy and RBI per-capita NSDP |
| `08_Government_Hospital_Beds_Per_Capita.ipynb` | NHP-2023 government hospital beds per 1,000 projected population |

Notebook 07 is the principal multivariable extension. It uses a 2023 workforce/outcome cross-section with NFHS-5 literacy (2019–21) and RBI per-capita NSDP (2021–22); two matched observations without an RBI 2021–22 NSDP value are excluded, not imputed (32 complete cases). Notebook 08 uses NHP-2023 bed counts dated 31 December 2022 and projected population as of 1 March 2021, so the denominator timing gap is disclosed.
