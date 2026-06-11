# M5: Data Pipeline

## Core Datasets
1. **Product Master**: `product_id`, `product_name`, `brand`, `category`, `sub_category`, `pack_size_ml`, `unit_price`.
2. **Store Master**: `store_id`, `store_name`, `region`, `city`, `store_format`.
3. **Sales & Promotions**: `week_start_date`, `product_id`, `store_id`, `region`, `units_sold`, `revenue`, `promotion_flag`, `promotion_type`, `discount_pct`.
4. **Inventory**: `week_start_date`, `product_id`, `store_id`, `opening_stock`, `units_received`, `units_sold`, `closing_stock`, `stockout_flag`.

## Dataset Rationale
This structure uses a star-like schema tailored for rapid analytics. Having separate reference tables (`Product Master`, `Store Master`) allows the AI to filter precisely by region or category. The fact tables (`Sales`, `Inventory`) are joined via explicit primary keys. This schema is easily interpretable by standard LLMs used in text-to-SQL tasks.

## Generation Method
**Synthetic**

## Challenges
The main challenge was ensuring statistical plausibility across the synthetic data. Specifically:
- **Correlated Variance**: If a product went on promotion (e.g., 'BOGO'), the `units_sold` had to increase realistically compared to the baseline.
- **Inventory Math Check**: `closing_stock` precisely equals `opening_stock + units_received - units_sold`. Generating independent random variables would have broken this logic, so the generator script runs a procedural loop maintaining stock levels week-over-week per store/product.

## Artifact Uploads
*(Attach your dataset sample file and generation scripts in the portal).*
