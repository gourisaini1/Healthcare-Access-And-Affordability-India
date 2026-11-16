# Project status — Version 3 exploratory extension

**Status:** Version 3 exploratory analyses completed; all eight notebooks and generated charts executed and saved successfully.  
**Evidence cut-off:** 16 November 2026.

## Completed analytical work

- Consolidated the repository to one canonical `Notebooks/` directory.
- Added and documented 2023 rural PHC doctor staffing data and the staffing-to-required-post ratio.
- Clarified that the staffing denominator is an administrative PHC post requirement, not population need or doctors per capita.
- Added small-denominator sensitivity analysis to Notebook 06.
- Added the staffing-versus-IMR visualisation and README explanation.
- Added NFHS-5 female literacy (women aged 15–49, 2019–21) and RBI per-capita NSDP (current prices, 2021–22) as state-level socioeconomic covariates.
- Added Notebook 07 with an OLS model using HC3 robust standard errors, complete-case handling, VIF diagnostics and a small-denominator sensitivity model.
- Added NHP-2023 government hospital bed counts dated 31 December 2022 and projected population as of 1 March 2021; calculated beds per 1,000 population for 36 states/UTs.
- Added Notebook 08, a per-capita beds visualisation and data dictionary.
- Updated the GitHub Actions workflow so output commits run only on pushes to `main`, are serialized to avoid concurrent push races, and use `[skip ci]` to prevent recursive workflow runs.

## Adjusted workforce–IMR model

The bivariate staffing/IMR match contains 34 observations. The adjusted complete-case model contains 32 observations; the two matched observations without a separate 2021–22 RBI NSDP value are the combined Dadra & Nagar Haveli and Daman & Diu UT and Lakshadweep. No imputation is used.

| Model | n | Staffing coefficient | HC3 SE | HC3 p-value | 95% CI |
|---|---:|---:|---:|---:|---|
| Unadjusted, common sample | 32 | -6.19 | 2.18 | 0.0046 | [-10.47, -1.91] |
| Adjusted: log NSDP + NFHS-5 female literacy | 32 | -3.40 | 2.72 | 0.211 | [-8.72, 1.93] |
| Adjusted, required PHC doctors >= 50 | 27 | -7.79 | 2.72 | 0.0042 | [-13.13, -2.46] |

- Adjusted model R-squared: 0.523; HC3 robust overall F-test p-value: 0.0042.
- Female literacy coefficient: -0.392 per percentage point (HC3 p=0.0376).
- Log NSDP coefficient: -4.19 (HC3 p=0.365).
- VIFs for the three predictors are low (approximately 1.22–1.50).

Interpretation: the staffing coefficient is about 45% smaller after adjustment and its confidence interval includes zero. The bivariate association is therefore partly accounted for by the included socioeconomic controls in this sample. The restricted-sample result is stronger, illustrating sensitivity to sample definition. All models are exploratory cross-sectional associations, not causal estimates.

## Government hospital beds per 1,000 population

- Numerator: NHP-2023 Table 6.2.2 government hospital beds, as of 31 December 2022.
- Denominator: NHP-2023 Table 1.1.2(d) projected population, as of 1 March 2021.
- State/UT count: 36.
- Median: 0.949 beds per 1,000 projected population.
- Mean: 1.285.
- Lowest: Bihar 0.215; highest: Lakshadweep 3.676.

The denominator is about 21 months earlier than the bed count. The rate covers government beds only. The 36 state/UT bed rows sum to 880,307, while the NHP India aggregate row reports 840,455 (a 39,852 discrepancy equal to the Andhra Pradesh row). The discrepancy is documented; no national aggregate rate is calculated from the inconsistent totals.

## Reproducibility and remaining limitations

- Eight notebooks are included in the canonical `Notebooks/` sequence.
- The validator checks datasets, notebook syntax, analytical joins and expected complete-case sample sizes.
- All notebooks are executed by GitHub Actions; executed cell outputs are committed on pushes to `main`.
- The output-commit step is skipped for pull requests and uses `[skip ci]` to avoid a workflow loop.
- Latest full validation and notebook-execution run: [GitHub Actions run 43886896461](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43886896461) — **success**.
- Dataset validation: passed; all eight notebooks executed; generated SVG charts and notebook outputs committed to `main`.

Remaining research limitations:
1. The adjusted model controls for only income and female literacy; maternal health, nutrition, sanitation, fertility, urbanisation, transport and service quality remain omitted.
2. Covariates predate the 2023 outcome (NFHS-5 2019–21; NSDP 2021–22).
3. Household catastrophic expenditure and impoverishment require household microdata.
4. The beds ratio has a 21-month numerator/denominator timing gap and an internal NHP aggregate reconciliation discrepancy.
5. The analyses do not establish causal effects.
