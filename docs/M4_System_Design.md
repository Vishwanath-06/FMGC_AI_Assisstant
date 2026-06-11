# M4: System Design & Discovery

## Key Design Decisions
1. **Agentic Framework**: Chose LangChain with its standard SQL Agent (`create_sql_agent`) instead of a fully custom agent loop. This leverages robust parsing of LLM outputs into executable queries while retaining the flexibility to adapt to both OpenAI and Gemini models depending on the user's API key.
2. **Database Engine**: Opted for a local `sqlite` database populated by a Python script rather than relying on heavy infrastructure like PostgreSQL. This ensures the prototype is entirely self-contained, easy to run, and highly portable for demonstration.
3. **User Interface**: Selected Streamlit for the front-end to rapidly prototype a functional conversational AI interface. Streamlit's chat elements provide native, clean structures for message history, eliminating the need to write custom HTML/JS.

## Pivots & Approach Changes
- **Initial Thought**: Building custom text-to-SQL prompting from scratch. 
- **Pivot**: Realized that LangChain's existing SQL database toolkit handles dialect-specific quirks and schema context-injection automatically. Pivoted to using the toolkit, but overrode the default prompt prefix to ensure the LLM understands FMCG domain concepts (e.g., how to interpret "revenue" or "stockout").

## Artifact Uploads
*(Attach your Initial Design Brief / Scratchpad and Thinking Transcripts directly in the portal).*
