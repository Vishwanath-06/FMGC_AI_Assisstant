# Pitch: The FMCG AI Assistant

## 🎯 The Core Problem
Business users across our functions (marketing, supply chain, regional management) frequently need data-driven insights:
- *"How did our BOGO promotion impact Spark Lemon sales last week?"*
- *"Are we facing stockouts in the North region?"*
- *"What is our top-performing category overall?"*

**Current Process**: Business users submit a ticket to the Data & Analytics team. The data team pulls the numbers, creates an ad-hoc dashboard, and returns the insight 3 days later. By then, the opportunity might have passed. Decision-making is delayed, and our analysts are bogged down with repetitive reporting.

---

## 💡 The Solution
Introducing the **FMCG AI Assistant** — a conversational AI workspace that puts the power of SQL directly into the hands of business users, securely and instantly.

Users simply type their questions in plain English. Our specialized AI model (leveraging Google Gemini or OpenAI) translates that intent into precise SQL, queries our data warehouse, and returns the answers in seconds.

### The "Wow" Factor
*No code. No SQL. No waiting.* 
A marketing manager can ask: *"Show me the revenue impact of the Price Cut on Spark Lemon in the North region"* and instantly receive the exact revenue figures and unit volumes, right in their browser.

---

## 🏗️ How We Built It (The Architecture)
We didn't just build a chatbot; we built a robust, data-aware agent.

1. **The Data Foundation**: A clean, star-schema data structure (Product Master, Store Master, Sales, Inventory) optimized for analytics. Good AI requires good data.
2. **The LangChain Agent**: We utilize an enterprise-grade agent framework that understands our specific FMCG context. It knows what "revenue" means, it knows what a "stockout" looks like, and it verifies queries before executing them.
3. **The User Interface**: A modern, interactive Streamlit frontend that feels like messaging a colleague.

---

## 🛡️ Mitigating Risks
We know that AI hallucination is a major concern for enterprise data. Here's how we solved it:
- **Read-Only Scope**: The AI is physically restricted from altering data. It can only `SELECT`.
- **Schema Validation**: The agent reads the exact database schema before answering, preventing it from inventing columns that don't exist.
- **Context Injection**: We engineered the prompt with strict guardrails (e.g., *"Always use LIKE '%keyword%' for product names"*).

---

## 🚀 The Future Roadmap (Version 2.0)
This prototype proves the concept. Where do we go next?
1. **Cloud DB Integration**: Seamlessly connect this to Snowflake or BigQuery with row-level security (so regional managers only see their regions).
2. **Dynamic Visualizations**: Empower the AI to not just return tables, but to generate real-time charts and graphs.
3. **Predictive Forecasting**: "Based on current stockout rates, what will our inventory look like next week?"

---

**Empower your business users. Free up your data analysts. Make decisions at the speed of conversation.**
