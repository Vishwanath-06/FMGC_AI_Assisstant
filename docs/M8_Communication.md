# M8: Communication

## Presentation Structure

The slide deck (to be uploaded separately) is structured to effectively communicate both the business value and the technical architecture of the solution to leadership:

1. **Executive Summary (1 Slide)**: The core problem (delayed ad-hoc analysis) and the proposed AI-powered solution.
2. **The "Wow" Factor / Demo (1 Slide)**: Screenshots/GIFs of the Streamlit interface answering complex business questions (e.g., "Show me the revenue impact of the Price Cut on Spark Lemon in the North region").
3. **Data Foundation (1 Slide)**: Overview of the FMCG star-schema. Highlighting that good AI requires good data structures.
4. **System Architecture (1 Slide)**: A simple diagram showing the flow: User -> Streamlit -> LangChain SQL Agent -> LLM Engine -> Local Database.
5. **Mitigating Risks (1 Slide)**: Addressing hallucinations. How the SQL Agent validates queries against the schema before execution, and how we bounded the scope to read-only analytical queries.
6. **Future Roadmap (1 Slide)**: What version 2.0 looks like (Cloud DB integration, voice interface, predictive forecasting).

## Artifact Uploads
*(Upload your PPTX/PDF slide deck in the portal).*
