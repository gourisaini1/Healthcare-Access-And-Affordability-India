# Project status — Version 3 exploratory extension

**Status:** Eight analytical notebooks execute successfully; the main regression specification and robustness analysis are aligned across the notebook, README and research report.  
**Evidence cut-off:** 16 November 2026.  
**Latest successful full workflow:** [GitHub Actions run 43896609894](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43896609894).

## Completed analytical work

- Consolidated the repository to one canonical `Notebooks/` directory.
- Documented the 2023 rural PHC doctor staffing data and the in-position-to-required-post ratio.
- Clarified that the staffing denominator is an administrative PHC post requirement, not population need or doctors per capita.
- Added small-denominator sensitivity analysis to Notebook 06.
- Added NFHS-5 female literacy (women aged 15–49, 2019–21) and RBI per-capita NSDP (current prices, 2021–22) as state-level socioeconomic covariates.
- Added Notebook 07 with HC3-robust OLS, transparent complete-case handling, linear and log staffing-ratio specifications, VIF diagnostics, a restricted-sample comparison, leave-one-state/UT-out analysis and a joint Goa–Delhi exclusion.
- Set the log staffing ratio as the preferred adjusted specification because the raw ratio is right-skewed; retained the linear ratio as a functional-form sensitivity check.
- Added NHP-2023 government hospital bed counts dated 31 December 2022 and projected population as of 1 March 2021; calculated beds per 1,000 population for 36 states/UTs.
- Added Notebook 08, the per-capita beds visualisation and a data dictionary.
- Expanded the root README with a notebook guide, empirical strategy, interpretation notes, validation instructions and a research roadmap.
- Updated the research report to use the same regression specifications and sensitivity results as Notebook 07.
- Updated the GitHub Actions workflow to rebase before pushing executed notebook outputs, preventing documentation commits made during a workflow run from causing a non-fast-forward push rejection.

## Adjusted workforce–IMR model

The bivariate staffing/IMR match contains 34 observations. The adjusted complete-case model contains 32 observations; the two matched observations without a separate 2021–22 RBI NSDP value are the combined Dadra & Nagar Haveli and Daman & Diu UT and Lakshadweep. No imputation is used.

The outcome is 2023 infant mortality per 1,000 live births. Controls are log nominal per-capita NSDP (2021–22) and NFHS-5 female literacy among women aged 15–49 (2019–21). HC3 heteroskedasticity-robust standard errors are reported.

| Specification | n | Staffing coefficient | HC3 SE | HC3 p-value | 95% CI |
|---|---:|---:|---:|---:|---|
| Adjusted linear staffing ratio | 32 | −3.396 | 2.717 | 0.2114 | [−8.722, 1.930] |
| Adjusted log staffing ratio (main) | 32 | −7.619 | 3.603 | 0.0345 | [−14.681, −0.557] |
| Linear ratio; required doctors >= 50 | 27 | −7.793 | 2.721 | 0.0042 | [−13.125, −2.460] |
| Log ratio; required doctors >= 50 | 27 | −10.868 | 4.069 | 0.0076 | [−18.843, −2.892] |
| Log ratio; exclude Goa and Delhi jointly | 30 | −11.246 | 3.649 | 0.0021 | [−18.398, −4.095] |

- Preferred full-sample log-ratio model R-squared: 0.555; adjusted R-squared: 0.508.
- In the main log model, log NSDP coefficient: −4.180 (HC3 p=0.342); female literacy coefficient: −0.374 per percentage point (HC3 p=0.043).
- Predictor VIFs: log staffing ratio 1.195; log NSDP 1.480; female literacy 1.507.
- Leave-one-state/UT-out log-ratio coefficients range from −9.066 (excluding Goa; p=0.0246) to −5.771 (excluding Manipur; p=0.1594). The coefficient remains negative in every one-at-a-time deletion, but some p-values exceed 0.05.

**Interpretation:** the preferred log-ratio model and selected restricted-sample models show a negative adjusted association. The full-sample linear-ratio adjusted coefficient is not statistically distinguishable from zero. The result is therefore specification-sensitive. Log and linear coefficients are on different scales. These are small-sample cross-sectional associations, not causal effects. The leave-one-out and joint-exclusion checks are diagnostics, not grounds for discarding observations.

## Government hospital beds per 1,000 population

- Numerator: NHP-2023 Table 6.2.2 government hospital beds, as of 31 December 2022.
- Denominator: NHP-2023 Table 1.1.2(d) projected population, as of 1 March 2021.
- State/UT count: 36.
- Median: 0.949 beds per 1,000 projected population.
- Mean: 1.285.
- Lowest: Bihar 0.215; highest: Lakshadweep 3.676.

The denominator is about 21 months earlier than the bed count. The rate covers government beds only. The 36 state/UT bed rows sum to 880,307, while the NHP India aggregate row reports 840,455 (a 39,852 discrepancy equal to the Andhra Pradesh row). The discrepancy is documented; no national aggregate rate is calculated from the inconsistent totals.

## Reproducibility and validation

- Eight notebooks are included in the canonical `Notebooks/` sequence.
- The validator checks datasets, notebook syntax, analytical joins and expected sample properties.
- GitHub Actions executes all eight notebooks and saves notebook outputs and generated SVG charts on pushes to `main`.
- Pull-request runs validate and execute notebooks but do not attempt to push outputs.
- The output-commit step rebases against the latest `main` before pushing to handle concurrent documentation updates.
- Latest successful full validation and notebook-execution run: [run 43896609894](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43896609894).

## Remaining research limitations

1. The adjusted model controls for only income and female literacy; maternal health, nutrition, sanitation, fertility, urbanisation, transport and service quality remain omitted.
2. NFHS-5 literacy (2019–21) and NSDP (2021–22) predate the 2023 outcome.
3. The small state/UT cross-section limits precision and makes inference sensitive to specification and sample composition.
4. Household catastrophic expenditure and impoverishment require household microdata.
5. The beds ratio has a 21-month numerator/denominator timing gap and an internal NHP aggregate reconciliation discrepancy.
6. The analyses do not establish causal effects.

## Next research extensions

1. Add household-level expenditure microdata to estimate catastrophic health expenditure and impoverishment using explicit thresholds and denominator definitions.
2. Add comparable rural/urban healthcare utilisation measures.
3. Build a multi-year state panel with harmonised definitions before estimating fixed-effects models.
4. Add maternal health, nutrition, sanitation, fertility, transport and service-quality covariates where source coverage supports comparison.
5. Pursue causal inference only if a defensible policy or quasi-experimental identification strategy can be established.
