# Government hospital beds data dictionary

- Beds: total government hospital beds (rural + urban), sourced from National Health Profile 2023, Table 6.2.2.
- Beds reference date: 31 December 2022 as stated in the NHP table title.
- Population: projected total population as on 1 March 2021 from NHP 2023, Table 1.1.2(d), units in thousands.
- Combined UT: projected 2021 population for Dadra & Nagar Haveli and Daman & Diu is the sum of the two separate NHP population projections (608 + 469 = 1,077 thousand); hospital beds are reported for the merged UT.
- Rate: total government hospital beds divided by projected population in thousands. Because the population field is already expressed in thousands, this directly gives beds per 1,000 residents.
- Population reference date is 1 March 2021, about 21 months before the bed-count reference date. The rate is therefore an approximate denominator-aligned availability indicator, not an exact same-date ratio.
- Government hospitals include central, state and local government bodies. This excludes private-sector beds.
- Source consistency note: the 36 state/UT bed rows sum to 880,307, while the NHP India aggregate row reports 840,455, a 39,852 discrepancy equal to the Andhra Pradesh row. State-level rates use the published state rows; no national rate is calculated from the inconsistent aggregate.
- Source: Central Bureau of Health Intelligence, National Health Profile 2023, Table 6.2.2 (p.263) and Table 1.1.2(d) (pp.15–16).
  https://cbhidghs.mohfw.gov.in/sites/default/files/NHP/NHP-2023-Last-Final.pdf

- Maharashtra source check: NHP-2023 Table 6.2.2 reports 10,920 rural beds + 16,417 urban beds = 27,337 total (0.2197 per 1,000 using the 2021 projected population of 124,437 thousand). This is second-lowest among the 36 state/UT rows, above only Bihar. The table notes contain no Maharashtra-specific footnote or adjustment; they define government hospitals and note that Delhi and Chandigarh have no rural area. The published Maharashtra value is therefore retained and explicitly flagged as unusual rather than altered.
