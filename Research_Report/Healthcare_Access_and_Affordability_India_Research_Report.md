# Healthcare Access and Affordability in India
## Research report — Version 2 analytical expansion

**Author:** Gouri Saini  
**Discipline:** Economics / Health Economics  
**Evidence cut-off:** 16 November 2026

---

## Executive summary

This project studies national health-financing patterns and state-level differences in public health budgets, rural primary-care staffing and infant mortality. Version 2 adds a same-reference-year comparison of rural Primary Health Centre (PHC) doctor staffing and infant mortality using Reserve Bank of India (RBI) tables for 2023. It also consolidates the repository around one canonical notebook sequence and narrows the stated research scope to what the available data can support.

The national National Health Accounts (NHA) series shows that the out-of-pocket expenditure (OOPE) share of total health expenditure declined from 64.2% in 2013–14 to 42.7% in 2023–24, while the government health expenditure share increased from 28.6% to 43.5%. This represents a shift in the financing mix, but does not reveal which households still face catastrophic medical spending.

Across 31 states/UTs, the 2024–25 Revised Estimate (RE) for Medical and Public Health and Family Welfare averaged 6.1% of aggregate expenditure (median 5.9%). This measure captures budget composition, not per-capita spending or service delivery.

The new rural workforce dataset reports doctors in position at rural PHCs relative to the source-reported requirement. Among 34 matched states/UTs with a positive requirement, 10 were below the reported requirement and 24 were at or above it. The median ratio was 1.38. Across these 34 observations, the Pearson correlation between staffing coverage and 2023 infant mortality was −0.538; the Spearman rank correlation was −0.562. These are cross-sectional associations, not causal effects. They may reflect broader differences in income, maternal education, nutrition, sanitation, fertility, transport, health infrastructure and public administration.

The project does not claim to have measured household catastrophic health expenditure, rural–urban utilisation gaps or adjusted socioeconomic determinants. Those questions require additional household and comparable panel data.

## 1. Research questions and scope

The empirical questions addressed in this report are:

1. How has India's national health-financing mix changed from 2013–14 to 2023–24?
2. How do state/UT public health budget shares vary in 2024–25 Revised Estimates?
3. How does rural PHC doctor staffing compare with the staffing requirement reported by RBI for 2023?
4. Is rural PHC doctor staffing coverage associated with infant mortality in 2023?
5. What descriptive information is available on state/UT government hospital and bed counts?

The following questions are recognised as important but are **not answered by the current evidence**: the household incidence of catastrophic health expenditure; differences in rural and urban healthcare utilisation and affordability; and the independent contribution of socioeconomic variables to health outcomes.

## 2. Data and sources

| Dataset | Period | Source | Analytical use |
|---|---|---|---|
| National health financing indicators | FY2013–14 to FY2023–24 | NHSRC / MoHFW, National Health Accounts | National financing trends |
| State public health expenditure share | FY2023–24 and FY2024–25 RE | RBI, State Finances 2025–26, Statement 27 | Budget composition |
| Infant mortality rate | Calendar 2023 | SRS, reproduced in RBI Handbook 2024–25, Table 4 | State health outcome |
| Rural PHC doctor staffing | Calendar 2023 | RBI Handbook 2024–25, Table 16 | Staffing relative to reported requirement |
| Government hospitals and beds | Observation year not specified in RBI table | RBI Handbook 2024–25, Table 17 | Infrastructure description |

Official source links:
- [NHSRC National Health Accounts](https://nhsrcindia.org/national-health-accounts-records)
- [RBI State Finances 2025–26, Statement 27](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23736)
- [RBI Handbook Table 4: State-wise IMR](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23453)
- [RBI Handbook Table 16: Doctors and Specialists](https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23465)
- [RBI Handbook Table 17: Government Hospitals and Beds](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23466)

## 3. Methodology

The project uses descriptive time-series analysis, state/UT comparisons, a derived staffing ratio and bivariate correlation.

### 3.1 National financing trend

The NHA series is analysed using levels and percentage-point changes in the government and OOPE shares of total health expenditure. Per-capita expenditure is reported at current prices and is not interpreted as real growth.

### 3.2 State budget comparison

The state expenditure measure is Medical and Public Health and Family Welfare expenditure as a percentage of aggregate expenditure. The 2024–25 figures are Revised Estimates, not audited actuals. State fiscal structures and denominators differ, so the indicator is interpreted as budget composition.

### 3.3 Rural PHC staffing ratio

For each state/UT with a positive required staffing count:

`PHC staffing coverage = Doctors in position / Required rural PHC doctors`

- A ratio below 1 means the reported in-position count is below the reported requirement.
- A ratio equal to 1 means the reported requirement is met.
- A ratio above 1 means the in-position count exceeds the reported requirement.

The ratio is not capped at 1.0. Values above 1 may occur in the source data and are retained. The source's asterisk and dash markers are stored as missing, not zero. The Chandigarh row has no positive rural PHC requirement and is excluded from ratio analysis.

### 3.4 Association with infant mortality

The staffing ratio is joined to 2023 infant mortality by harmonised state/UT labels. The analysis reports Pearson's correlation (linear association) and Spearman's rank correlation. No causal interpretation is made and no multivariable controls are included.

## 4. Findings

### 4.1 National health financing

| Indicator | 2013–14 | 2023–24 | Change |
|---|---:|---:|---:|
| Government health expenditure share | 28.6% | 43.5% | +14.9 percentage points |
| OOPE share | 64.2% | 42.7% | −21.5 percentage points |

The composition of health financing shifted toward a larger government share and a smaller direct household payment share. However, OOPE still represented 42.7% of total health expenditure in 2023–24. Aggregate OOPE does not reveal the incidence or severity of household-level financial distress.

### 4.2 State public health budget shares

For the 31 states/UTs included in the RBI Statement 27 dataset, the unweighted mean of the 2024–25 RE share was 6.1% and the median was 5.9%. NCT Delhi recorded 12.3% and Punjab 3.0%.

This is a share of aggregate expenditure. It is not an absolute rupee amount, expenditure per resident, expenditure as a share of GSDP, or an outcome measure. It should not be used alone to rank the quality of state health systems.

### 4.3 Rural PHC doctor staffing

The 2023 RBI Table 16 data cover 36 state/UT rows. After matching to the 2023 IMR dataset and excluding observations without a positive required staffing denominator, 34 state/UTs have a calculable staffing ratio.

- Median in-position-to-required ratio: **1.38**.
- Below the reported requirement: **10 of 34**.
- At or above the reported requirement: **24 of 34**.

The lowest ratio in the matched sample is Odisha (916 doctors in position against 1,277 required; ratio 0.72). The highest is Goa (97 in position against 21 required; ratio 4.62). These values are relative to the administrative requirement in the source, not a population-based benchmark. A high ratio does not necessarily indicate equitable geographic distribution or effective service delivery.

### 4.4 Rural PHC staffing and infant mortality

Across the 34 matched state/UT observations:

| Statistic | Estimate | Interpretation |
|---|---:|---|
| Pearson correlation | −0.538 | Moderate negative linear association in this sample |
| Pearson p-value | 0.0010 | Evidence against zero bivariate linear correlation under the test assumptions |
| Spearman correlation | −0.562 | Negative rank association |
| Spearman p-value | 0.0005 | Evidence against zero rank association under the test assumptions |
| Observations | 34 | States/UTs with a positive requirement and matched IMR |

The negative association means that states/UTs with higher rural PHC doctor staffing relative to the reported requirement tended to have lower infant mortality in this sample. Statistical significance does not establish causality. The relationship may be confounded by socioeconomic conditions, maternal and child health programmes, nutrition, sanitation, transport, fertility, broader health infrastructure and state capacity. Small-state observations may also be more volatile.

This result is stronger than the earlier comparison between 2024–25 RE budget shares and 2023 IMR because the workforce and outcome variables share the same reference year and the staffing measure is closer to service availability. It is still a bivariate cross-sectional association, not an evaluation of the impact of hiring additional doctors.

### 4.5 Government hospitals and beds

The RBI Table 17 data provide state/UT absolute counts of government hospitals and beds, including rural/urban splits where reported. The table does not specify a distinct observation year. Therefore, this project does not label the counts as 2024–25 data and does not calculate population-adjusted access from them. Absolute counts are affected by state population size and cannot by themselves indicate adequacy.

## 5. Economic interpretation

The national NHA series documents a shift in the financing mix, but the persistence of OOPE makes financial protection an important research priority. State budget shares provide information about fiscal priorities but not actual service delivery or household affordability.

The new workforce analysis suggests that rural PHC doctor staffing relative to administrative requirements is associated with infant mortality across states/UTs. This is consistent with the proposition that primary-care capacity matters for health outcomes, but the design cannot isolate the contribution of staffing from broader social and institutional conditions.

A policy interpretation should therefore avoid single-indicator rankings. Better evidence would combine financial protection, population-adjusted capacity, workforce distribution, service utilisation and social determinants.

## 6. Limitations

1. NHA financing indicators are national aggregates and do not show household-level distribution.
2. The 2024–25 state health expenditure values are Revised Estimates.
3. The budget share is not expenditure per capita or as a share of GSDP.
4. The PHC staffing ratio uses administrative required staffing as its denominator, not population.
5. Rural PHC doctors represent only one part of the health workforce and exclude private providers, urban facilities and other cadres.
6. The staffing–IMR analysis is cross-sectional and bivariate; omitted-variable bias is likely.
7. The hospital/bed table does not state a distinct observation year; counts are absolute, not population-adjusted.
8. The project does not yet include household catastrophic expenditure or impoverishment measures.

## 7. Further research

The next empirical extension should add household-level medical expenditure data to calculate catastrophic health expenditure using explicit thresholds (for example, out-of-pocket health spending as a share of total household consumption or capacity to pay). A second extension should build a multi-year state panel of rural workforce, IMR, per-capita state income, maternal education, sanitation, nutrition and health expenditure. Fixed-effects models may then be considered if definitions, coverage and time periods are sufficiently consistent. Any causal claim would still require a defensible identification strategy.

## 8. Reproducibility

The repository contains six canonical Jupyter notebooks, source CSVs, data dictionaries, visualisations, a research report and a GitHub Actions workflow. The workflow validates source files, checks notebook syntax and executes all notebooks.
