# Analysis notebooks

Run the notebooks from this directory in numerical order. Each notebook reads its analysis-ready source files from `../Dataset/` and writes generated figures to `../Visualisations/`.

## Notebook sequence

| Notebook | Research question / task | Main outputs |
|---|---|---|
| `01_National_Health_Accounts_Analysis.ipynb` | How has India's national health-financing mix changed from FY2013–14 to FY2023–24? | Financing trends, government and OOPE shares, national expenditure charts |
| `02_State_Health_Expenditure_Analysis.ipynb` | How does state/UT health budget composition vary? | State expenditure share comparisons for FY2023–24 and FY2024–25 RE |
| `03_Health_Outcomes_and_Expenditure.ipynb` | How do state health budget shares and infant mortality compare? | State-level outcome and expenditure comparisons |
| `04_State_Hospital_Infrastructure_Analysis.ipynb` | How is government hospital infrastructure distributed? | State/UT hospital and bed count analysis |
| `05_Correlation_and_Regression_Analysis.ipynb` | Is the budget-share measure associated with 2023 infant mortality? | Pearson and Spearman correlations and simple regression |
| `06_Rural_Workforce_and_Health_Outcomes.ipynb` | How does rural PHC doctor staffing compare with reported requirements, and how does it relate to IMR? | Staffing coverage ratio, bivariate associations and small-denominator sensitivity |
| `07_Adjusted_Workforce_IMR_Regression.ipynb` | Does the rural PHC staffing–IMR association persist after socioeconomic controls? | HC3-adjusted OLS, linear/log specifications, restricted-sample models, VIF and leave-one-out diagnostics |
| `08_Government_Hospital_Beds_Per_Capita.ipynb` | How does government bed availability vary after population adjustment? | Beds per 1,000 projected population and source consistency checks |
| `09_State_Health_Insurance_Coverage.ipynb` | How does household health insurance/financing coverage vary across states/UTs, and is it associated with per-capita NSDP? | NFHS-5 household coverage chart and descriptive Pearson/Spearman correlations |

## Notebook 07: model specification and sample

Notebook 07 is the principal multivariable extension. It relates the 2023 rural PHC in-position-to-required doctor ratio to 2023 infant mortality, controlling for log nominal per-capita NSDP (FY2021–22, current prices) and NFHS-5 female literacy among women aged 15–49 (2019–21).

The preferred model uses the natural log of the staffing ratio because the raw ratio is right-skewed. The original linear-ratio model is retained as a functional-form sensitivity check. Both use HC3 heteroskedasticity-robust standard errors.

- Bivariate matched sample: 34 states/UTs.
- Adjusted complete-case sample: 32 states/UTs.
- Excluded from the adjusted sample because no separate 2021–22 NSDP observation is available: Lakshadweep and the combined Dadra & Nagar Haveli and Daman & Diu UT.
- No missing covariates are imputed.
- The leave-one-state/UT-out estimates are diagnostics, not a causal identification strategy.

### Adjusted staffing coefficient summary

| Specification | n | Coefficient | HC3 p-value |
|---|---:|---:|---:|
| Linear staffing ratio, full sample | 32 | −3.396 | 0.2114 |
| Log staffing ratio, full sample (main) | 32 | −7.619 | 0.0345 |
| Linear ratio, required PHC doctors >= 50 | 27 | −7.793 | 0.0042 |
| Log ratio, required PHC doctors >= 50 | 27 | −10.868 | 0.0076 |
| Log ratio, exclude Goa and Delhi jointly | 30 | −11.246 | 0.0021 |

The leave-one-out log-ratio coefficient ranges from −9.066 (excluding Goa) to −5.771 (excluding Manipur); some corresponding p-values exceed 0.05. Read the full table and confidence intervals in Notebook 07 rather than relying on a single p-value. The coefficient units differ between the linear and log specifications.

### Important interpretation boundary

The analysis is cross-sectional and exploratory. The PHC staffing denominator is the source-reported administrative post requirement, not population need. The socioeconomic controls predate the 2023 outcome. The model does not control for maternal health, nutrition, sanitation, fertility, urbanisation, transport, health-system quality or all other confounders. No causal effect is identified.

## Reproduce

From the repository root:

```bash
pip install -r requirements.txt
python scripts/validate_project.py
cd Notebooks
jupyter lab
```

Open the notebooks in numerical order and run all cells. The automated GitHub Actions workflow performs dataset and notebook-syntax checks, executes all eight notebooks, and saves executed outputs and generated SVG figures to the main branch on successful pushes.
