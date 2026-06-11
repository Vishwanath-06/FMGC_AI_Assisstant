# M6: Build & Code

## GitHub Repository Link
*(Please insert your GitHub URL here before final submission)*

## Biggest Technical Issue
**Context injection for string matching in SQL generation.**
Initially, when users asked "How many units of Spark Lemon did we sell?", the LLM formulated a strict SQL query like `SELECT units_sold FROM sales_and_promotions WHERE product_id = (SELECT product_id FROM product_master WHERE product_name = 'Spark Lemon')`. Because the actual product name is `'Spark Lemon Sparkling Water 500ml'`, the query returned zero results.

## Resolution Documentation
1. **Diagnosis**: Reviewed the intermediate tool execution logs in LangChain (`verbose=True`). Identified that exact string matching on user inputs was failing against full product names in the database.
2. **Experimentation**: Tested generic instructions to "always look up product names first", but this consumed too many LLM tokens and increased latency.
3. **Implementation**: Updated the `agent.py` prefix prompt explicitly with: `ALWAYS use LIKE '%keyword%' when searching for product names, brands, or cities to ensure case-insensitive and partial matching.` 
4. **Verification**: After applying the custom instruction, the LLM successfully generated queries like `WHERE product_name LIKE '%Spark Lemon%'`, immediately resolving the issue without complex intermediate lookup tools.

## Artifact Uploads
*(Attach your Vibe Coding Tool chats in the portal).*
