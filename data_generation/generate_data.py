import pandas as pd
import numpy as np
from datetime import timedelta
import sqlite3
import os

# Set seed for reproducibility
np.random.seed(42)

# --- Configuration ---
NUM_WEEKS = 24
NUM_STORES = 50
START_DATE = pd.to_datetime('2024-01-01')
REGIONS = ['North', 'South', 'East', 'West']

# --- Generate Product Master ---
products_data = [
    ('BEV-001', 'Spark Lemon Sparkling Water 500ml', 'Spark', 'Carbonated', 'Sparkling Water', 500, 1.50),
    ('BEV-002', 'Spark Berry Sparkling Water 500ml', 'Spark', 'Carbonated', 'Sparkling Water', 500, 1.50),
    ('BEV-003', 'Spark Plain Sparkling Water 1000ml', 'Spark', 'Carbonated', 'Sparkling Water', 1000, 2.00),
    ('BEV-004', 'Nectar Orange Juice 250ml', 'Nectar', 'Juice', 'Fruit Juice', 250, 1.20),
    ('BEV-005', 'Nectar Apple Juice 250ml', 'Nectar', 'Juice', 'Fruit Juice', 250, 1.20),
    ('BEV-006', 'Nectar Mixed Fruit Juice 1000ml', 'Nectar', 'Juice', 'Fruit Juice', 1000, 3.50),
    ('BEV-007', 'AquaPure Spring Water 500ml', 'AquaPure', 'Water', 'Still Water', 500, 0.80),
    ('BEV-008', 'AquaPure Spring Water 1500ml', 'AquaPure', 'Water', 'Still Water', 1500, 1.50),
    ('BEV-009', 'Bolt Energy Drink Original 250ml', 'Bolt', 'Energy', 'Energy Drink', 250, 2.50),
    ('BEV-010', 'Bolt Energy Drink Zero 250ml', 'Bolt', 'Energy', 'Energy Drink', 250, 2.50),
    ('BEV-011', 'CreamyFarm Whole Milk 1000ml', 'CreamyFarm', 'Dairy', 'Milk', 1000, 1.80),
    ('BEV-012', 'CreamyFarm Skim Milk 1000ml', 'CreamyFarm', 'Dairy', 'Milk', 1000, 1.80),
    ('BEV-013', 'CreamyFarm Chocolate Milk 500ml', 'CreamyFarm', 'Dairy', 'Flavored Milk', 500, 1.50),
    ('BEV-014', 'Zest Cola Regular 330ml', 'Zest', 'Carbonated', 'Cola', 330, 1.00),
    ('BEV-015', 'Zest Cola Diet 330ml', 'Zest', 'Carbonated', 'Cola', 330, 1.00),
    ('BEV-016', 'Zest Cola Regular 2000ml', 'Zest', 'Carbonated', 'Cola', 2000, 2.80),
    ('BEV-017', 'VitaBoost Vitamin Water Lemon 500ml', 'VitaBoost', 'Water', 'Enhanced Water', 500, 1.80),
    ('BEV-018', 'VitaBoost Vitamin Water Berry 500ml', 'VitaBoost', 'Water', 'Enhanced Water', 500, 1.80),
    ('BEV-019', 'NatureBrew Iced Tea Peach 500ml', 'NatureBrew', 'Juice', 'Iced Tea', 500, 1.60),
    ('BEV-020', 'NatureBrew Iced Tea Lemon 500ml', 'NatureBrew', 'Juice', 'Iced Tea', 500, 1.60),
]

product_df = pd.DataFrame(products_data, columns=[
    'product_id', 'product_name', 'brand', 'category', 'sub_category', 'pack_size_ml', 'unit_price'
])

# --- Generate Store Master ---
store_formats = ['Supermarket', 'Hypermarket', 'Convenience', 'Wholesale']
stores_data = []
for i in range(1, NUM_STORES + 1):
    store_id = f'STR-{i:03d}'
    store_name = f'Store {store_id}'
    region = np.random.choice(REGIONS)
    city = f'{region} City {np.random.randint(1, 6)}'
    store_format = np.random.choice(store_formats, p=[0.4, 0.2, 0.3, 0.1])
    stores_data.append((store_id, store_name, region, city, store_format))

store_df = pd.DataFrame(stores_data, columns=[
    'store_id', 'store_name', 'region', 'city', 'store_format'
])

# --- Generate Sales & Promotions and Inventory ---
dates = [START_DATE + timedelta(weeks=i) for i in range(NUM_WEEKS)]
sales_data = []
inventory_data = []

promotion_types = ['Price Cut', 'BOGO', 'Display Feature', 'Bundle']

for _, store in store_df.iterrows():
    store_id = store['store_id']
    region = store['region']
    
    # Store-specific baseline multipliers (larger formats sell more)
    store_multiplier = {'Supermarket': 1.0, 'Hypermarket': 2.5, 'Convenience': 0.5, 'Wholesale': 4.0}[store['store_format']]
    
    for _, product in product_df.iterrows():
        product_id = product['product_id']
        unit_price = product['unit_price']
        
        # Product popularity multiplier
        product_multiplier = np.random.uniform(0.5, 1.5)
        
        # Initial stock setup
        current_stock = int(np.random.uniform(100, 500) * store_multiplier)
        
        for date in dates:
            # Determine if promotion is active (approx 15% chance per week)
            is_promo = np.random.random() < 0.15
            promo_type = np.random.choice(promotion_types) if is_promo else None
            
            # Determine discount
            if promo_type == 'Price Cut': discount_pct = 0.20
            elif promo_type == 'BOGO': discount_pct = 0.50
            elif promo_type == 'Bundle': discount_pct = 0.15
            else: discount_pct = 0.0
            
            # Base units sold
            base_demand = np.random.normal(50, 10) * store_multiplier * product_multiplier
            
            # Promotion lift
            promo_lift = 1.0
            if is_promo:
                promo_lift = np.random.uniform(1.5, 3.0) # 50% to 200% lift
            
            # Calculate actual demand
            demand = int(max(0, base_demand * promo_lift))
            
            # Inventory receiving logic (restock when low)
            units_received = 0
            if current_stock < demand * 1.5:
                # 5% chance of supply chain issue causing zero restock
                if np.random.random() < 0.05:
                    units_received = 0
                else:
                    # Restock enough for ~3 weeks of average demand
                    units_received = int((base_demand * 3) + np.random.uniform(20, 50))
                
            opening_stock = current_stock
            
            # Limit sales by available stock
            units_sold = min(demand, opening_stock + units_received)
            
            revenue = round(units_sold * unit_price * (1 - discount_pct), 2)
            
            closing_stock = opening_stock + units_received - units_sold
            stockout_flag = (closing_stock == 0)
            
            sales_data.append((
                date.strftime('%Y-%m-%d'), product_id, store_id, region, units_sold,
                revenue, is_promo, promo_type, discount_pct
            ))
            
            inventory_data.append((
                date.strftime('%Y-%m-%d'), product_id, store_id, opening_stock,
                units_received, units_sold, closing_stock, stockout_flag
            ))
            
            # Update for next week
            current_stock = closing_stock

sales_df = pd.DataFrame(sales_data, columns=[
    'week_start_date', 'product_id', 'store_id', 'region', 'units_sold',
    'revenue', 'promotion_flag', 'promotion_type', 'discount_pct'
])

inventory_df = pd.DataFrame(inventory_data, columns=[
    'week_start_date', 'product_id', 'store_id', 'opening_stock',
    'units_received', 'units_sold', 'closing_stock', 'stockout_flag'
])

# --- Save to SQLite ---
db_path = os.path.join(os.path.dirname(__file__), 'fmcg_data.db')
conn = sqlite3.connect(db_path)

product_df.to_sql('product_master', conn, index=False, if_exists='replace')
store_df.to_sql('store_master', conn, index=False, if_exists='replace')
sales_df.to_sql('sales_and_promotions', conn, index=False, if_exists='replace')
inventory_df.to_sql('inventory', conn, index=False, if_exists='replace')

conn.close()

print(f"Synthetic data generation complete. Database saved to: {db_path}")
print(f"- Product Master: {len(product_df)} rows")
print(f"- Store Master: {len(store_df)} rows")
print(f"- Sales & Promotions: {len(sales_df)} rows")
print(f"- Inventory: {len(inventory_df)} rows")
