# M9: Reflection

## Version 2.0 Improvements
1. **Semantic Layer / Few-Shot Examples**: Currently, the agent relies heavily on the system prompt to understand the domain. In V2, I would implement a vector database containing few-shot examples of complex queries (e.g., "How to calculate YoY growth") to feed into the prompt dynamically, vastly improving accuracy on hard questions.
2. **Data Visualizations**: Text and tabular answers are good, but executives love charts. I would integrate a Python REPL tool alongside the SQL tool, allowing the agent to query the database and then write `matplotlib`/`plotly` code to return interactive charts in the Streamlit UI.
3. **Production Database Integration**: Migrate from the synthetic SQLite local file to a Snowflake or BigQuery instance, implementing row-level security so users only see data for their respective regions.

## Core Learnings
- **Agent Tool Calling is Powerful but Fragile**: Allowing an LLM to write and execute SQL is incredibly powerful for ad-hoc queries, but it requires strict schema definitions. I learned that having clean foreign keys and explicitly naming columns (e.g., `pack_size_ml` instead of just `size`) drastically reduces hallucinated queries.
- **Prompt Engineering as "Guardrails"**: Rather than just telling the AI what to do, the prompt became a list of guardrails (e.g., "Limit results to 10 rows", "Use LIKE for strings"). This shifted my perspective from prompt *design* to prompt *engineering*.

## System Failure Points
1. **Ambiguous Terminology**: If a user asks for "profit", the system will likely fail or hallucinate a calculation because the database only explicitly tracks "revenue" and "unit_price", lacking cost of goods sold (COGS). The agent isn't currently robust enough to say "I don't have cost data to calculate profit."
2. **Context Window Limits on Schema**: If this scaled to a massive Enterprise Data Warehouse with hundreds of tables, passing the entire schema in the prompt would exceed token limits and confuse the model. A semantic search step over the data dictionary would be required first.
3. **Complex Aggregations**: The LLM occasionally struggles with complex, multi-level aggregations (e.g., "What is the rolling 4-week average stockout rate compared to the same period last year?"). It might write syntactically valid SQL that returns logically incorrect math.
