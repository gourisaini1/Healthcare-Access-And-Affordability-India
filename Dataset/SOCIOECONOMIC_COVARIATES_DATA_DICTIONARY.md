# State-level socioeconomic covariates

## NFHS-5 female literacy

- Variable: percentage of women aged 15–49 classified as literate in NFHS-5.
- Reference period: 2019–21.
- Definition in NFHS-5 India Report, Table 3.4.1: women who can read a whole or part sentence, plus women who completed Standard 9 or higher (assumed literate).
- This is a survey-based literacy measure for women aged 15–49, not the Census population literacy rate for all women.
- Source: International Institute for Population Sciences (IIPS) and Ministry of Health and Family Welfare, NFHS-5 India Report, Table 3.4.1.
  https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf

## Per-capita NSDP

- Variable: per-capita Net State Domestic Product at current prices (₹).
- Reference year: 2021–22.
- Source: Reserve Bank of India, Handbook of Statistics on Indian States 2023–24, Table 26, base 2011–12; underlying source NSO, MoSPI.
  https://nhm.tn.gov.in/wp-content/uploads/2026/Key_Statistics/RBI/RBI%20Statistics%20Handbook%202023-24.pdf
- Missing values are retained as missing. RBI does not report a separate 2021–22 observation for Ladakh, Lakshadweep, or the combined Dadra & Nagar Haveli and Daman & Diu UT in this table.
- The model uses the natural logarithm of per-capita NSDP to reduce scale skew. It is a nominal current-price measure; it is not adjusted for state-specific cost of living.

## Join and interpretation

The 2023 IMR and 2023 PHC staffing indicators are matched to NFHS-5 2019–21 literacy and 2021–22 NSDP. The socioeconomic variables predate the 2023 outcome by approximately 1–3 years. The complete-case model excludes observations without a published NSDP value; no imputation is performed.
