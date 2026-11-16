# Project status — Version 2 baseline validated

**Status:** Baseline reproducibility checks and execution passed; two requested extensions remain open.  
**Evidence cut-off:** 16 November 2026.

## Completed and validated

- Consolidated the repository to one canonical `Notebooks/` directory containing six ordered notebooks.
- Removed the duplicate notebook tree under `Dataset/Notebooks/` and the malformed nested README.
- Added the state/UT dataset for rural PHC doctors in position, sanctioned positions and reported requirements for 2023, sourced from RBI Handbook Table 16.
- Added a data dictionary documenting source fields, missing markers and the staffing-coverage ratio.
- Repaired Notebook 06 cell structure, added the small-denominator sensitivity analysis, and clarified that the denominator is the source-reported PHC post requirement rather than population need.
- Added the staffing-versus-IMR visualisation and embedded it in the README.
- Updated the research report and README to distinguish evidence supported by current data from questions not yet answered.
- Added GitHub Actions execution with in-place notebook output saving and a commit step.
- Executed all six notebooks successfully; saved execution counts and outputs are present in the committed notebooks.
- Passed the dataset, notebook syntax and analytical validation checks.

## Validated workforce result

For 34 matched states/UTs with a positive reported rural PHC doctor requirement:
- Median in-position-to-required ratio: 1.38.
- 10 of 34 observations were below the reported requirement.
- Pearson correlation with 2023 IMR: approximately -0.538.
- Spearman correlation with 2023 IMR: approximately -0.562.
- With required PHC doctor denominator >= 50 (27 observations), Pearson r is approximately -0.498 and Spearman rho approximately -0.368.

These are bivariate cross-sectional associations, not causal effects. The ratio is an administrative staffing-benchmark ratio, not population-adjusted doctor density. Small-denominator sensitivity is reported in Notebook 06.

## Remaining extensions — not represented as completed

1. **Adjusted workforce–IMR regression:** Not yet estimated. Official per-capita NSDP values for 2022–23 are unavailable for a number of states/UTs, while the available female-literacy series is from Census 2011. Combining these would create a materially smaller complete-case sample and a wide reference-year gap relative to 2023 IMR. A regression can be run only after the final matched sample, source years and missingness are transparently documented; no missing values should be imputed merely to retain observations.
2. **Population-adjusted government hospital beds:** Not yet estimated. RBI Handbook Table 17 reports absolute hospital/bed counts but does not specify a distinct observation year in the extracted table. Dividing those counts by a population estimate from a different year would create a misleading rate. A dated facility-count source or a verified observation year is needed.
3. **Household affordability and catastrophic expenditure:** Not measured by national NHA aggregates; household microdata are required.
4. **Rural–urban utilisation/access gaps:** Not measured by the current state aggregates; comparable facility/household data are required.

## Reproducibility

The latest GitHub Actions run completed successfully:
- Run: https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43881263925
- Dataset and notebook validation: passed.
- All six notebooks: executed successfully.
- Notebook outputs: saved in the repository by the workflow.

## Interpretation boundary

The project is a secondary-data, descriptive and correlational analysis. It does not estimate causal effects or claim that the current aggregate indicators measure household-level access, financial hardship or service quality.
