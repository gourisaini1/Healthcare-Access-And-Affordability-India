# NFHS-5 state-level household health insurance coverage

- **Variable:** percentage of households with at least one usual member covered by any health insurance or financing scheme.
- **Reference period:** NFHS-5, 2019–21.
- **Geography:** 36 states/UTs, including the combined Dadra & Nagar Haveli and Daman & Diu UT.
- **Source:** International Institute for Population Sciences (IIPS) and ICF, *National Family Health Survey (NFHS-5), 2019–21: India: Volume I*, Table 11.15, p. 476; the state/UT coverage indicator is also visualised in Figure 11.2, p. 448.
- **Official report:** https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf
- **Definition:** a household is counted as covered when at least one usual member is covered by any health insurance or financing scheme.
- **Interpretation:** this is a proxy for household reach of insurance/financing schemes, not a measure of benefit adequacy, claim approval, utilisation, out-of-pocket spending or catastrophic health expenditure. High coverage does not guarantee full financial protection.
- **Derived comparison:** the Pearson correlation with per-capita NSDP at current prices in FY2021–22 uses 33 state/UTs with a separate NSDP observation. Ladakh, Lakshadweep and the combined Dadra & Nagar Haveli and Daman & Diu UT are excluded from that correlation because NSDP is unavailable in the existing RBI series. No imputation is performed.
- **Data handling:** percentages are transcribed as published and are not recalculated or weighted. The all-India value (41.0%) is not included as a state observation.


## State scheme inventory fields

- **Fields:** `state_scheme_documented_in_inventory` and `state_scheme_name_or_note`.
- **Meaning:** `Yes` indicates a state-specific government health insurance scheme listed in Table 1 of [Wealth Status and Health Insurance Enrollment in India: An Empirical Analysis](https://www.mdpi.com/2227-9032/11/9/1343) (2023). `Not documented` means the reviewed inventory did not list a state-specific scheme; the article states that its list is not exhaustive, so this must not be interpreted as proof that no scheme existed.
- **Tripura:** RSBY/PM-JAY is identified in the inventory as a central programme and is not coded as a state-funded scheme.
- **Group comparison:** 22 state/UT observations with a documented state-specific scheme have mean coverage 50.8% and median 53.5%; 14 observations not documented as having one have mean 29.0% and median 25.4%. This is an unweighted descriptive contrast, not a causal estimate. Some schemes were merged with PM-JAY; the binary flag does not measure state financing share or programme intensity.
- **A&N cross-source check:** the national NFHS-5 India Report Table 11.15 gives 1.8%; the Government's Phase-I A&N fact sheet gives 1.6%. The CSV retains the national report's 1.8% for consistency with the all-state comparison table. The difference is flagged, not resolved.
- **Scheme inventory context:** the peer-reviewed inventory documents programmes in Andhra Pradesh, Telangana, Tamil Nadu, Rajasthan and other states, and notes mergers with PM-JAY. It is a secondary inventory, not a complete official census of programmes active on each survey date.
