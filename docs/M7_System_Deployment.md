# M7: System & Deployment

## Deployment Type
**Local Only** (Configured to be easily deployable to Streamlit Community Cloud)

## Deployed Backend API URL
*(Not applicable - built as a unified Streamlit application utilizing LangChain locally.)*

## Deployed UI / App URL
*(Not applicable - run locally via `streamlit run app/app.py`)*

## Deployment Notes
The system is built with minimal external dependencies. By maintaining a local SQLite database (`fmcg_data.db`) and placing all logic within the Streamlit lifecycle, the application can be trivially deployed to Streamlit Community Cloud or a Docker container simply by providing the `requirements.txt` and setting the appropriate API keys in the environment variables (or letting the user input them via the sidebar UI).
