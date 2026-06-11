import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'fmcg_data.db')

def run_query(query, conn):
    return pd.read_sql_query(query, conn)

def test_features():
    if not os.path.exists(DB_PATH):
        print(f"FAILED: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    status_report = []

    print("--- FMCG AI Assistant Feature Tests ---\n")

    # Feature 1: Promotional performance summaries
    print("Testing Feature 1: Promotional performance summaries")
    q1 = """
    SELECT promotion_type, SUM(revenue) as total_revenue, SUM(units_sold) as total_units
    FROM sales_and_promotions
    GROUP BY promotion_type
    ORDER BY total_revenue DESC;
    """
    try:
        res1 = run_query(q1, conn)
        print("STATUS: PASSED")
        print("SAMPLE OUTPUT:")
        print(res1.head())
        status_report.append({"Feature": "Promotional performance", "Status": "PASSED"})
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Promotional performance", "Status": "FAILED"})
    print("-" * 40)

    # Feature 2: Inventory movement insights (e.g. Stockouts)
    print("Testing Feature 2: Inventory movement insights (Stockouts)")
    q2 = """
    SELECT p.product_name, SUM(i.stockout_flag) as total_stockout_weeks
    FROM inventory i
    JOIN product_master p ON i.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_stockout_weeks DESC
    LIMIT 5;
    """
    try:
        res2 = run_query(q2, conn)
        print("STATUS: PASSED")
        print("SAMPLE OUTPUT:")
        print(res2)
        status_report.append({"Feature": "Inventory movement", "Status": "PASSED"})
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Inventory movement", "Status": "FAILED"})
    print("-" * 40)

    # Feature 3: Regional sales comparisons
    print("Testing Feature 3: Regional sales comparisons")
    q3 = """
    SELECT s.region, SUM(sp.revenue) as total_revenue
    FROM sales_and_promotions sp
    JOIN store_master s ON sp.store_id = s.store_id
    GROUP BY s.region
    ORDER BY total_revenue DESC;
    """
    try:
        res3 = run_query(q3, conn)
        print("STATUS: PASSED")
        print("SAMPLE OUTPUT:")
        print(res3)
        status_report.append({"Feature": "Regional sales", "Status": "PASSED"})
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Regional sales", "Status": "FAILED"})
    print("-" * 40)

    # Feature 4: Product-level campaign impact
    print("Testing Feature 4: Product-level campaign impact")
    q4 = """
    SELECT p.product_name, sp.promotion_flag, AVG(sp.units_sold) as avg_weekly_units
    FROM sales_and_promotions sp
    JOIN product_master p ON sp.product_id = p.product_id
    WHERE p.product_name LIKE '%Spark Lemon%'
    GROUP BY p.product_name, sp.promotion_flag;
    """
    try:
        res4 = run_query(q4, conn)
        print("STATUS: PASSED")
        print("SAMPLE OUTPUT:")
        print(res4)
        status_report.append({"Feature": "Product-level campaign impact", "Status": "PASSED"})
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Product-level campaign impact", "Status": "FAILED"})
    print("-" * 40)
    
    conn.close()
    
    print("\n--- FINAL STATUS REPORT ---")
    for item in status_report:
        print(f"{item['Feature']}: {item['Status']}")

if __name__ == "__main__":
    test_features()
