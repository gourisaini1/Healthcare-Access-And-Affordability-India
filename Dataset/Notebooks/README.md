# Analytical Notebooks

Run these notebooks in order from the repository root.

1. **01_Data_Acquisition.ipynb** — download national health-financing series from the World Bank Indicators API (WHO Global Health Expenditure Database).
2. **02_Data_Quality_and_Preparation.ipynb** — validate and clean the downloaded series.
3. **03_Health_Financing_Trends.ipynb** — plot national out-of-pocket and government financing trends.
4. **04_State_Level_Healthcare_Infrastructure.ipynb** — analyse reviewed state-level Rural Health Statistics data.
5. **05_NFHS_Health_and_Affordability_Indicators.ipynb** — analyse NFHS-5 state factsheet indicators.
6. **06_Statistical_and_Regional_Analysis.ipynb** — exploratory state-level correlations.
7. **07_Findings_and_Policy_Implications.ipynb** — synthesise verified evidence.

No observations or findings are fabricated. Notebook 01 downloads live API data. RHS and NFHS state-level source files must be downloaded from official portals and added to `Dataset/Raw_Data/`; see `Dataset/Raw_Data/README.md`. The state-level notebooks stop with clear instructions when source inputs are missing.

Generated data are saved under `Dataset/Processed_Data/`; charts are saved under `Dataset/Notebooks/Visualisations/`.