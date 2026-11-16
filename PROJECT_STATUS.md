# Project status — Version 2 analytical expansion

**Status:** Analytical expansion committed; final GitHub Actions validation pending.  
**Evidence cut-off:** 16 November 2026.

## Version 2 changes

- Consolidated the repository to one canonical `Notebooks/` directory containing six ordered notebooks.
- Removed the duplicate notebook tree under `Dataset/Notebooks/`.
- Removed the malformed nested file `README.mdREADME.mdREADME.md`.
- Added a state/UT dataset for rural PHC doctors in position, sanctioned positions and reported requirements for 2023, sourced from RBI Handbook Table 16.
- Added a data dictionary that preserves missing source markers as missing and documents the staffing-coverage ratio.
- Added Notebook 06 to match 2023 rural PHC staffing with 2023 infant mortality, report Pearson and Spearman associations, and document interpretation limits.
- Expanded the written research report with the new analysis and its limitations.
- Rewrote the README to distinguish questions answered by current evidence from questions that remain unanswered.
- Removed unused packages from `requirements.txt` and simplified the CI installation process.
- Expanded project validation to check the new dataset, matched sample, analytical coefficients, notebook count and absence of the duplicate directory.

## New empirical result

For 34 matched states/UTs with a positive reported rural PHC doctor requirement:
- Median in-position-to-required ratio: 1.38.
- 10 of 34 observations were below the reported requirement.
- Pearson correlation with 2023 IMR: -0.538 (p = 0.0010).
- Spearman correlation with 2023 IMR: -0.562 (p = 0.0005).

These are bivariate cross-sectional associations, not causal effects. The ratio is not a population-adjusted doctor density and does not measure actual access or service quality.

## Scope boundaries

The repository does not currently measure household catastrophic health expenditure, impoverishment due to medical spending, rural–urban utilisation gaps, or adjusted socioeconomic determinants. National OOPE shares are financing aggregates, not household-level incidence measures. Government hospital/bed counts are absolute counts from a source table that does not state a distinct observation year.

## Reproducibility

The GitHub Actions workflow validates CSV structure and analytical checks, compiles notebook code cells, and executes all six notebooks. The Version 2 workflow run is currently queued; this status will be updated after it completes.
