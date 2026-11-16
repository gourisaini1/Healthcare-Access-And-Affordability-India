# Healthcare Access and Affordability in India
## Final research report

**Author:** Gouri Saini  
**Discipline:** Economics / Health Economics  
**Evidence cut-off:** 16 November 2026

---

## Executive summary

This project studies national health-financing patterns and state-level differences in public health budgets, rural primary-care staffing and infant mortality. The final consolidated analysis includes an exploratory multivariable model of rural PHC staffing and infant mortality, using NFHS-5 female literacy and RBI per-capita NSDP as socioeconomic controls. It also replaces the earlier undated RBI bed-count series for this question with dated National Health Profile (NHP) 2023 government bed counts and a projected population denominator.

The national National Health Accounts (NHA) series shows that the out-of-pocket expenditure (OOPE) share of total health expenditure declined from 64.2% in 2013–14 to 42.7% in 2023–24, while the government health expenditure share increased from 28.6% to 43.5%. This represents a shift in the financing mix, but does not reveal which households still face catastrophic medical spending.

Across 31 states/UTs, the 2024–25 Revised Estimate (RE) for Medical and Public Health and Family Welfare averaged 6.1% of aggregate expenditure (median 5.9%). This measure captures budget composition, not per-capita spending or service delivery.

The new rural workforce dataset reports doctors in position at rural PHCs relative to the source-reported requirement. Among 34 matched states/UTs with a positive requirement, 10 were below the reported requirement and 24 were at or above it. The median ratio was 1.38. Across these 34 observations, the Pearson correlation between staffing coverage and 2023 infant mortality was −0.538; the Spearman rank correlation was −0.562. These are cross-sectional associations, not causal effects. They may reflect broader differences in income, maternal education, nutrition, sanitation, fertility, transport, health infrastructure and public administration.

The adjusted analysis uses 32 complete-case state/UT observations and compares two functional forms on the same sample. With the unlogged staffing ratio, the adjusted coefficient is −3.40 (HC3 p=0.211; 95% CI −8.72 to 1.93). With the natural log of the staffing ratio as the preferred specification, the coefficient is −7.62 (HC3 p=0.0345; 95% CI −14.68 to −0.56). The preferred log model has R-squared 0.555. In the sample with at least 50 required PHC doctors (n=27), the log-ratio coefficient is −10.87 (HC3 p=0.0076), while the linear-ratio coefficient is −7.79 (HC3 p=0.0042). Jointly excluding Goa and Delhi from the full log-ratio sample gives −11.25 (n=30; HC3 p=0.0021). Leave-one-state/UT-out coefficients range from −9.07 to −5.77, although some corresponding p-values exceed 0.05. These diagnostics show an inverse association under the main log specification and selected sensitivity specifications, but also show dependence on functional form and sample definition. NFHS-5 household insurance/financing coverage is also examined as a state-level financial-protection proxy: the national estimate is 41.0%, and state/UT coverage ranges from 1.8% to 87.8%. The correlation with nominal per-capita NSDP is close to zero (Pearson r=0.052, p=0.776; n=33). This measure indicates scheme reach, not adequacy of benefits or actual household out-of-pocket burden. The project still does not calculate catastrophic health expenditure or measure rural–urban utilisation gaps.

## 1. Research questions and scope

The empirical questions addressed in this report are:

1. How has India's national health-financing mix changed from 2013–14 to 2023–24?
2. How do state/UT public health budget shares vary in 2024–25 Revised Estimates?
3. How does rural PHC doctor staffing compare with the staffing requirement reported by RBI for 2023?
4. Is rural PHC doctor staffing coverage associated with infant mortality in 2023?
5. How does government hospital-bed availability vary after adjusting for projected population?
6. Does the staffing–IMR association persist after controlling for per-capita state income and female literacy?
7. How does household health insurance/financing coverage vary across states/UTs, and how is it associated with per-capita NSDP?

The following questions are recognised as important but are **not answered by the current evidence**: the household incidence of catastrophic health expenditure; differences in rural and urban healthcare utilisation and affordability; and causal effects of staffing or the full set of socioeconomic determinants of health outcomes.

## 2. Data and sources

| Dataset | Period | Source | Analytical use |
|---|---|---|---|
| National health financing indicators | FY2013–14 to FY2023–24 | NHSRC / MoHFW, National Health Accounts | National financing trends |
| State public health expenditure share | FY2023–24 and FY2024–25 RE | RBI, State Finances 2025–26, Statement 27 | Budget composition |
| Infant mortality rate | Calendar 2023 | SRS, reproduced in RBI Handbook 2024–25, Table 4 | State health outcome |
| Rural PHC doctor staffing | Calendar 2023 | RBI Handbook 2024–25, Table 16 | Staffing relative to reported requirement |
| Per-capita NSDP | FY2021–22, current prices | RBI Handbook 2023–24, Table 26 | Income control |
| Female literacy | NFHS-5, 2019–21, women aged 15–49 | IIPS / MoHFW, NFHS-5 India Report, Table 3.4.1 | Education control |
| Household health insurance/financing coverage | NFHS-5, 2019–21 | IIPS / ICF, NFHS-5 India Report, Table 11.15 and Figure 11.2 | State-level financial-protection proxy |
| Government hospital beds | 31 December 2022 | CBHI, National Health Profile 2023, Table 6.2.2 | Beds numerator |
| Projected population | 1 March 2021 | CBHI, National Health Profile 2023, Table 1.1.2(d) | Population denominator for beds per 1,000 |

Official source links:
- [NHSRC National Health Accounts](https://nhsrcindia.org/national-health-accounts-records)
- [RBI State Finances 2025–26, Statement 27](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23736)
- [RBI Handbook Table 4: State-wise IMR](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23453)
- [RBI Handbook Table 16: Doctors and Specialists](https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23465)
- [RBI Handbook 2023–24, Table 26: Per-capita NSDP](https://nhm.tn.gov.in/wp-content/uploads/2026/Key_Statistics/RBI/RBI%20Statistics%20Handbook%202023-24.pdf)
- [NFHS-5 India Report, Table 3.4.1](https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf)
- [National Health Profile 2023, CBHI](https://cbhidghs.mohfw.gov.in/sites/default/files/NHP/NHP-2023-Last-Final.pdf)

## 3. Methodology

The project uses descriptive time-series analysis, state/UT comparisons, a derived staffing ratio, bivariate correlation and exploratory multivariable OLS regression.

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

### 3.4 Bivariate association with infant mortality

The staffing ratio is joined to 2023 infant mortality by harmonised state/UT labels. The analysis reports Pearson's correlation (linear association) and Spearman's rank correlation. No causal interpretation is made.

### 3.5 Exploratory adjusted regression

The dependent variable is 2023 IMR (deaths per 1,000 live births). The principal predictor in the preferred specification is the natural logarithm of the 2023 rural PHC in-position-to-required doctor ratio. The log specification was adopted after an initial linear-ratio analysis, following a robustness review; the linear result is reported alongside it for that reason. The raw ratio is right-skewed; the log transformation compresses its upper tail and models proportional rather than absolute differences. The original unlogged ratio is retained as a functional-form sensitivity specification. Controls are (i) the natural logarithm of per-capita NSDP at current prices in FY2021–22 (₹), from RBI Handbook 2023–24 Table 26, and (ii) NFHS-5 percentage literate among women aged 15–49 in 2019–21, from Table 3.4.1. Models are estimated by OLS with HC3 heteroskedasticity-consistent standard errors. Both full-sample adjusted specifications use the same complete-case sample of 32 observations. Two matched observations (Dadra & Nagar Haveli and Daman & Diu combined; Lakshadweep) have no separate 2021–22 NSDP value and are excluded rather than imputed. The notebook estimates both linear- and log-ratio models in the restricted sample with at least 50 required PHC doctors (n=27), performs leave-one-state/UT-out estimation of the main log model, and jointly excludes Goa and Delhi as an additional influence check. This is an exploratory cross-section; covariate years predate the outcome and the model does not establish causality.

### 3.6 Household health insurance/financing coverage

The state-level coverage measure is the percentage of households with at least one usual member covered by any health insurance or financing scheme, from NFHS-5 Table 11.15 (2019–21). It is interpreted as scheme reach, not as the adequacy of cover, successful claim payment, utilisation or a reduction in out-of-pocket spending. The correlation with nominal per-capita NSDP at current prices in FY2021–22 is calculated on the 33 state/UTs with a separate NSDP observation; missing NSDP values are not imputed.

### 3.7 Population-adjusted government hospital beds

Government hospital bed counts are taken from NHP-2023 Table 6.2.2, whose title dates the counts to 31 December 2022. The denominator is projected state/UT population as of 1 March 2021 from NHP-2023 Table 1.1.2(d), in thousands. Beds per 1,000 population are calculated as beds divided by population in thousands. The combined Dadra & Nagar Haveli and Daman & Diu population is the sum of the two separately projected populations. The 21-month reference-date gap is disclosed; the indicator is approximate.

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

This result is a bivariate cross-sectional association, not an evaluation of the impact of hiring additional doctors.

### 4.5 Adjusted workforce–IMR regression

The complete-case sample contains 32 states/UTs. The original unadjusted staffing coefficient on this common sample is −6.19 (HC3 standard error 2.18, p=0.0046; 95% CI −10.47 to −1.91). Once controls are added, the estimated staffing coefficient depends on functional form:

| Specification | n | Staffing coefficient | HC3 SE | HC3 p-value | 95% CI |
|---|---:|---:|---:|---:|---|
| Adjusted linear staffing ratio | 32 | −3.396 | 2.717 | 0.2114 | [−8.722, 1.930] |
| Adjusted log staffing ratio (main) | 32 | −7.619 | 3.603 | 0.0345 | [−14.681, −0.557] |
| Linear ratio; required doctors >= 50 | 27 | −7.793 | 2.721 | 0.0042 | [−13.125, −2.460] |
| Log ratio; required doctors >= 50 | 27 | −10.868 | 4.069 | 0.0076 | [−18.843, −2.892] |
| Log ratio; exclude Goa and Delhi jointly | 30 | −11.246 | 3.649 | 0.0021 | [−18.398, −4.095] |

The preferred full-sample log-ratio model has R-squared 0.555 and adjusted R-squared 0.508. In that specification, the log-NSDP coefficient is −4.180 (HC3 p=0.342) and the female-literacy coefficient is −0.374 per percentage point (HC3 p=0.043). Predictor VIFs are low: 1.195 for log staffing ratio, 1.480 for log NSDP and 1.507 for female literacy.

The leave-one-state/UT-out log-ratio coefficient ranges from −9.066 (excluding Goa; HC3 p=0.0246) to −5.771 (excluding Manipur; HC3 p=0.1594). The coefficient remains negative in every one-at-a-time deletion, but some p-values exceed 0.05; the uncertainty is therefore sensitive to individual observations. The joint Goa–Delhi exclusion is a targeted diagnostic, not evidence that either observation is erroneous.

The log coefficient also has a direct proportional interpretation: doubling the staffing ratio changes its natural log by \(\\ln 2\\approx0.693\), so the estimate implies about \(7.62\\times\\ln 2\\approx5.3\) fewer infant deaths per 1,000 live births, conditional on the controls. This is an adjusted association, not a causal prediction. The log specification was adopted after an initial linear-ratio analysis, following a robustness review; the linear result is reported alongside it for that reason.

The correct interpretation is specification-sensitive evidence of an inverse association: the preferred log-ratio model and both restricted log/linear models are statistically distinguishable from zero at conventional levels, while the full-sample linear-ratio adjusted estimate is not. The log and linear coefficients are on different scales and should not be compared as if they measured the same unit. The result does not establish that increasing PHC staffing causes infant mortality to fall. The sample is small, covariates predate the outcome, and maternal health, nutrition, sanitation, fertility, urbanisation, transport, service quality and other potential confounders remain omitted.

### 4.6 Government hospital beds per 1,000 population

Across 36 states/UTs, the median government hospital bed availability is 0.949 beds per 1,000 projected population; the mean is 1.285. The lowest rates are Bihar (0.215), Maharashtra (0.220), Chhattisgarh (0.326) and Uttar Pradesh (0.345). The highest are Lakshadweep (3.676), Andaman & Nicobar Islands (3.523), Chandigarh (3.340), Ladakh (2.700) and Sikkim (2.674). Small-population UTs may show volatile rates.

The numerator is dated 31 December 2022; the population denominator is projected as of 1 March 2021, about 21 months earlier. The indicator covers government beds only and does not measure private beds, occupancy, staffing, quality or geographic accessibility. There is also a source-table reconciliation issue: the 36 state/UT rows sum to 880,307 beds, while the NHP India aggregate row reports 840,455, a difference of 39,852 equal to the Andhra Pradesh row. State-level rates use the published state rows; no national aggregate rate is calculated from these inconsistent totals.

### 4.7 Household health insurance/financing coverage

NFHS-5 reports that 41.0% of households nationally had at least one usual member covered by a health insurance or financing scheme. Across the 36 state/UT rows, coverage ranges from 1.8% in Andaman & Nicobar Islands to 87.8% in Rajasthan. For the 33 state/UTs with a separate FY2021–22 per-capita NSDP observation, Pearson correlation between nominal per-capita NSDP and household coverage is 0.052 (p=0.776). This is close to zero in this small, unweighted cross-section. It should not be interpreted as evidence that income is irrelevant to financial protection: the measure is an aggregate household coverage rate, the income series is nominal and not contemporaneous, and the analysis does not adjust for state policy, demographic or scheme design differences. Insurance coverage does not guarantee adequate benefits or eliminate out-of-pocket spending.

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
6. The staffing–IMR analysis is cross-sectional; the adjusted model controls for only two socioeconomic variables and omitted-variable bias remains likely.
7. NFHS-5 literacy (2019–21) and NSDP (2021–22) predate the 2023 outcome; they are not perfectly contemporaneous.
8. Two matched observations without a separate 2021–22 NSDP value are excluded from the adjusted model; no imputation is used.
9. Hospital-bed rates combine a 2022-12-31 numerator with a 2021-03-01 projected population denominator.
10. The NHP state-row bed sum does not reconcile with the published India aggregate; the discrepancy is disclosed.
11. NFHS-5 household insurance coverage measures whether any usual member is covered, not benefit adequacy, claim payment, out-of-pocket expenditure or catastrophic spending.
12. The project does not yet calculate household catastrophic expenditure or impoverishment measures.

## 7. Further research

The next empirical extension should add household-level medical expenditure data to calculate catastrophic health expenditure using explicit thresholds (for example, out-of-pocket health spending as a share of total household consumption or capacity to pay). A stronger workforce analysis would build a multi-year state panel of rural workforce, IMR, per-capita state income, maternal education, sanitation, nutrition and health expenditure. Fixed-effects models may then be considered if definitions, coverage and time periods are sufficiently consistent. Any causal claim would still require a defensible identification strategy.

## 8. Reproducibility

The repository contains nine canonical Jupyter notebooks, source CSVs, data dictionaries, visualisations, a research report and a GitHub Actions workflow. The workflow validates source files, checks notebook syntax and executes all notebooks; executed notebooks and generated SVG visualisations are committed on pushes to main. Pull-request runs do not attempt to push. The output commit uses a CI-skip marker to prevent recursive workflow runs.
