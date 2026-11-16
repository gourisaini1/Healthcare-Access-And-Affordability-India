# State-wise government hospitals and beds

## Coverage
State/UT counts of government hospitals and beds, with rural/urban splits where reported, reproduced from Table 17 of the RBI *Handbook of Statistics on Indian States 2024–25*.

## Source
Reserve Bank of India, *Handbook of Statistics on Indian States 2024–25*, Table 17: State-wise Number of Government Hospitals and Beds. The RBI table cites the National Health Profile, Central Bureau of Health Intelligence, Ministry of Health and Family Welfare.

Official table: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23466

## Fields
- `state_ut`: State or Union Territory.
- `government_hospitals_rural`, `government_hospitals_urban`, `government_hospitals_total`: Counts of government hospitals.
- `beds_rural`, `beds_urban`, `beds_total`: Counts of government hospital beds.

## Important limitations
1. The RBI table as displayed does not specify a distinct observation year for these counts. The handbook edition is 2024–25, but this must not be interpreted as proof that the counts refer to financial year 2024–25.
2. A dash in the RBI table means not available; blank cells are retained as missing, not zero.
3. Hospital and bed counts are absolute totals. They are not population-adjusted measures and do not by themselves measure accessibility, quality, utilisation or staffing.
4. The RBI table defines government hospitals as including central government, state government and local government bodies.
5. Delhi and Chandigarh have no rural area, as noted by RBI.

## Source note
The source table reports an all-India total of 36,626 government hospitals and 840,455 beds. State-level rows in this CSV do not include that national aggregate row.
