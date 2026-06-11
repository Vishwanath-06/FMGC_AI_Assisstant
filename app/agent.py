import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_generation', 'fmcg_data.db')
    return SQLDatabase.from_uri(f"sqlite:///{db_path}")

def get_llm(provider, api_key):
    if provider == 'OpenAI':
        return ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)
    elif provider == 'Google Gemini':
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, google_api_key=api_key)
    else:
        raise ValueError("Unsupported provider")

def create_fmcg_agent(provider, api_key):
    db = get_db_connection()
    llm = get_llm(provider, api_key)
    
    # Custom instructions for FMCG context
    instructions = """
    You are an expert AI data assistant for an FMCG (Fast-Moving Consumer Goods) company, specifically for the Beverages category.
    Your goal is to help business users analyze their database containing sales, promotions, inventory, products, and store data.
    
    You have access to a SQLite database with the following tables:
    1. product_master: Contains product details (product_id, product_name, brand, category, sub_category, pack_size_ml, unit_price).
    2. store_master: Contains store details (store_id, store_name, region, city, store_format).
    3. sales_and_promotions: Weekly sales data (week_start_date, product_id, store_id, region, units_sold, revenue, promotion_flag, promotion_type, discount_pct).
    4. inventory: Weekly stock data (week_start_date, product_id, store_id, opening_stock, units_received, units_sold, closing_stock, stockout_flag).
    
    Important rules to follow:
    - ALWAYS use `LIKE '%keyword%'` when searching for product names, brands, or cities to ensure case-insensitive and partial matching.
    - If asked about "revenue", use the `revenue` column in `sales_and_promotions`.
    - If asked about "stockouts", use the `stockout_flag` column in `inventory`.
    - If asked to compare regions, join with `store_master` or use the `region` column in `sales_and_promotions`.
    - Limit your SQL query results to 10 rows unless the user explicitly asks for more.
    - Before writing a query, make sure to look at the schema using your tools.
    - If the user asks a conversational question, answer in a friendly, helpful tone.
    - Try to provide analytical insights, not just raw data, when summarizing.
    """
    
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools" if provider == 'OpenAI' else "tool-calling",
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": True},
        prefix=instructions
    )
    
    return agent_executor
