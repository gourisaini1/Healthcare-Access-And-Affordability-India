# Project status — Version 1.0

**Status:** Version 1.0 research project complete  
**Last validation:** 16 November 2026  
**Validation:** GitHub Actions run succeeded; all five notebooks executed successfully.

## Completed deliverables

- Research framework, questions and conceptual model.
- National NHA dataset for 2013–14 to 2023–24 with data dictionary.
- State/UT health expenditure share dataset for 2024–25 Revised Estimates.
- State/UT infant mortality dataset for 2023.
- State/UT government hospital and bed dataset from RBI Handbook Table 17.
- Derived 31-observation expenditure–IMR matched dataset.
- Five Jupyter notebooks covering national financing, state expenditure, health outcomes, hospital infrastructure and exploratory correlation/regression.
- Eight committed SVG visualisations.
- Main GitHub README with embedded visualisations.
- Full written research report.
- CSV/notebook syntax validation script and GitHub Actions workflow.

## Reproducibility result

The GitHub Actions workflow:
1. Installs the project dependencies.
2. Validates CSV structure and key analytical checks.
3. Parses all notebooks for Python syntax.
4. Executes all five notebooks.

Latest successful run: https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43877464216

## Research scope and limitations

Version 1.0 is a completed exploratory secondary-data project. It does not claim to be a complete causal evaluation of healthcare access or household affordability.

The current evidence includes national OOPE financing shares, state budget shares, infant mortality and government hospital/bed counts. It does not yet include a comparable state-level panel of catastrophic health expenditure, household-level medical spending, facility utilisation, private-sector capacity or population-adjusted workforce/bed coverage. The RBI hospital/bed table does not specify a distinct observation year; its counts are not labelled as 2024–25.

## Optional Version 2 extensions

These would deepen the project but are not required for the Version 1.0 deliverable:
- Add household survey measures of medical spending and catastrophic health expenditure.
- Add state-level health workforce indicators from RBI Table 16 / Health Dynamics of India.
- Add population-adjusted bed and workforce indicators after harmonising reference years.
- Build a multi-year state panel with income, education, sanitation, nutrition and health-system controls.
- Estimate panel models only after confirming consistent definitions and adequate time coverage.
