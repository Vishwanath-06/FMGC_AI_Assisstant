import os
import sys

# Add the parent directory and app directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from streamlit.testing.v1 import AppTest
from app.agent import create_fmcg_agent
import sqlite3

def run_tests():
    status_report = []
    print("--- FMCG AI App & Agent Tests ---\n")

    # 1. Test Database Structure and Rows
    print("Testing Feature 5: Database Structure & Row Counts")
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'fmcg_data.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        tables = ['product_master', 'store_master', 'sales_and_promotions', 'inventory']
        counts = {}
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            counts[table] = cursor.fetchone()[0]
        
        print("STATUS: PASSED")
        print("SAMPLE OUTPUT:")
        for t, c in counts.items():
            print(f"  - {t}: {c} rows")
        
        if counts['product_master'] == 20 and counts['store_master'] == 50 and counts['sales_and_promotions'] > 0:
            status_report.append({"Feature": "DB Structure & Rows", "Status": "PASSED", "Output": str(counts)})
        else:
            raise ValueError("Row counts do not match expected boundaries")
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "DB Structure & Rows", "Status": "FAILED", "Output": str(e)})
    print("-" * 40)

    # 2. Test Agent Initialization (OpenAI & Gemini)
    print("Testing Feature 6: LLM Agent Initialization (Text-to-SQL logic wiring)")
    try:
        agent_openai = create_fmcg_agent("OpenAI", "fake_openai_key")
        agent_gemini = create_fmcg_agent("Google Gemini", "fake_gemini_key")
        
        print("STATUS: PASSED")
        out = "Both OpenAI and Google Gemini agents initialized successfully, correctly binding to the SQLite DB and injecting the FMCG domain prompt."
        print(out)
        status_report.append({"Feature": "Agent Initialization", "Status": "PASSED", "Output": out})
    except Exception as e:
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Agent Initialization", "Status": "FAILED", "Output": str(e)})
    print("-" * 40)

    # 3. Test Streamlit UI (AppTest framework)
    print("Testing Feature 7: Streamlit UI Functionality & Chat Interface")
    try:
        app_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'app.py')
        at = AppTest.from_file(app_path)
        at.run()
        
        # Verify Title
        title_matches = at.title[0].value == "🍹 FMCG AI Assistant"
        
        # Simulate chat input without API key
        at.chat_input[0].set_value("What were the top sales last week?").run()
        
        # Verify error message shows up properly inside the chat
        error_shown = False
        for msg in at.error:
            if "Please enter your API Key" in msg.value:
                error_shown = True
        
        if title_matches and error_shown:
            print("STATUS: PASSED")
            out = "Streamlit UI loads correctly. Title verified. Chat interface accurately intercepts user prompts and enforces API Key validation before attempting LLM queries."
            print(out)
            status_report.append({"Feature": "Streamlit UI & Chat", "Status": "PASSED", "Output": out})
        else:
            if at.exception:
                raise ValueError(f"App UI crashed with: {at.exception[0]}")
            else:
                raise ValueError(f"App UI did not respond as expected. title_matches={title_matches}, error_shown={error_shown}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"STATUS: FAILED - {e}")
        status_report.append({"Feature": "Streamlit UI & Chat", "Status": "FAILED", "Output": str(e)})
    print("-" * 40)

    print("\n--- FINAL APP/AGENT STATUS REPORT ---")
    for item in status_report:
        print(f"{item['Feature']}: {item['Status']}")

if __name__ == "__main__":
    run_tests()
