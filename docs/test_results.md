# FMCG AI Assistant Feature Tests & Output Verification

This document outlines the specific tests we ran against the synthetic database to verify that the generated data correctly models the 4 core business features requested in the assessment.

## Testing Setup
We ran direct SQL queries against the local `fmcg_data.db` to verify the AI assistant will have the proper underlying data structures and values to correctly answer user queries.

---

### Feature 1: Promotional performance summaries
**What was tested**: Can we accurately sum revenue and units sold grouped by the type of promotion?
**Status**: PASSED

**Sample Output**:
```text
    promotion_type  total_revenue  total_units
0             None     2978939.10      1703730
1  Display Feature      318904.10       186599
2           Bundle      261281.23       176150
3        Price Cut      229210.16       166437
4             BOGO      135689.30       156323
```
*Note: This proves the agent can accurately contrast baseline sales (None) against various promotional strategies.*

---

### Feature 2: Inventory movement insights (Stockouts)
**What was tested**: Can we identify which products have experienced the most weeks out of stock?
**Status**: PASSED

**Sample Output**:
```text
                          product_name  total_stockout_weeks
0     Bolt Energy Drink Original 250ml                    14
1  VitaBoost Vitamin Water Lemon 500ml                    12
2   Spark Plain Sparkling Water 1000ml                    12
3              Zest Cola Regular 330ml                    11
4         CreamyFarm Whole Milk 1000ml                    11
```
*Note: Initially, our inventory generator was "too perfect" and never stocked out. We introduced a 5% supply-chain failure rate into the generation script, which correctly produced these realistic stockout numbers for the AI to find.*

---

### Feature 3: Regional sales comparisons
**What was tested**: Can we accurately aggregate total revenue by geographic region by joining the fact and dimension tables?
**Status**: PASSED

**Sample Output**:
```text
  region  total_revenue
0   East     1245431.91
1  South     1096604.82
2   West      924177.24
3  North      657809.92
```
*Note: This proves the `store_master` successfully linked to the `sales_and_promotions` table allowing regional rollups.*

---

### Feature 4: Product-level campaign impact
**What was tested**: How did promotions affect the average weekly unit sales for a specific product ("Spark Lemon")?
**Status**: PASSED

**Sample Output**:
```text
                        product_name  promotion_flag  avg_weekly_units
0  Spark Lemon Sparkling Water 500ml               0         87.498035
1  Spark Lemon Sparkling Water 500ml               1        204.335165
```
*Note: This verifies that the synthetic data accurately models demand lift. Without a promotion, Spark Lemon sold ~87 units/week. With a promotion, it sold ~204 units/week.*

---

## Final Status Report
- Promotional performance: **PASSED**
- Inventory movement: **PASSED**
- Regional sales: **PASSED**
- Product-level campaign impact: **PASSED**
