from fpdf import FPDF
import os

class SlideDeck(FPDF):
    def header(self):
        # Logo or Title on every slide
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'FMCG AI Assistant - Executive Presentation', border=False, align='R')
        self.ln(20)

    def footer(self):
        # Page numbers
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Slide {self.page_no()}', align='C')

    def slide_title(self, title):
        self.set_font('helvetica', 'B', 24)
        self.set_text_color(0, 51, 102)
        self.cell(0, 15, title, new_x="LMARGIN", new_y="NEXT", align='L')
        self.ln(10)

    def slide_body(self, text):
        self.set_font('helvetica', '', 14)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, text)
        self.ln()

    def add_slide(self, title, body):
        self.add_page(orientation='L')
        self.slide_title(title)
        self.slide_body(body)

def generate_presentation():
    pdf = SlideDeck()
    
    # Title Slide
    pdf.add_page(orientation='L')
    pdf.set_y(80)
    pdf.set_font('helvetica', 'B', 36)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 20, 'FMCG AI Assistant', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font('helvetica', 'I', 18)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, 'Empowering Business Decisions through Conversational AI', new_x="LMARGIN", new_y="NEXT", align='C')

    # Slide 1: Executive Summary
    pdf.add_slide(
        "1. Executive Summary",
        "The Core Problem:\n"
        "Business users frequently request ad-hoc analysis for promotions, inventory, and sales. "
        "These requests rely heavily on manual dashboarding by data analysts, leading to delayed "
        "decision-making and analytical bottlenecks.\n\n"
        "The Proposed Solution:\n"
        "An AI-powered conversational workspace. Business users ask plain-English questions, and the "
        "AI securely translates them into SQL to extract instant insights from the FMCG data warehouse."
    )

    # Slide 2: The "Wow" Factor / Demo
    pdf.add_slide(
        "2. The 'Wow' Factor / Demo",
        "Imagine a marketing manager asking:\n"
        "\"Show me the revenue impact of the Price Cut on Spark Lemon in the North region.\"\n\n"
        "Within seconds, the Streamlit interface returns the exact revenue figures and unit volumes, "
        "without writing a single line of SQL or opening a complicated BI tool.\n\n"
        "(Refer to the Streamlit App Demo for the live interface)"
    )

    # Slide 3: Data Foundation
    pdf.add_slide(
        "3. Data Foundation",
        "Good AI requires excellent data structures. Our foundation is built on an FMCG Star Schema:\n\n"
        "- Product Master: Dimension table for categories, sub-categories, and pricing.\n"
        "- Store Master: Dimension table for geographic regions and store formats.\n"
        "- Sales & Promotions: Fact table capturing weekly revenue and promotional lifts.\n"
        "- Inventory: Fact table capturing stock movement and stockout flags.\n\n"
        "This structured approach enables the LLM to write highly accurate, deterministic SQL queries."
    )

    # Slide 4: System Architecture
    pdf.add_slide(
        "4. System Architecture",
        "Our architecture ensures a seamless flow from intent to insight:\n\n"
        "1. User Interface: A modern Streamlit chat interface.\n"
        "2. Orchestration: LangChain SQL Agent processes the request.\n"
        "3. Intelligence Engine: Google Gemini or OpenAI parses the semantic intent.\n"
        "4. Execution: Validated SQL runs securely against the local SQLite database.\n"
        "5. Response: Data is synthesized back into natural language for the user."
    )

    # Slide 5: Mitigating Risks
    pdf.add_slide(
        "5. Mitigating Risks",
        "Enterprise AI demands strict guardrails to prevent hallucinations and data leaks:\n\n"
        "- Read-Only Execution: The agent is bounded by database credentials that can only SELECT.\n"
        "- Schema Validation: Queries are validated against the actual schema before execution.\n"
        "- Context Injection: The prompt enforces strict domain rules (e.g., matching text with LIKE "
        "to handle minor misspellings, using specific columns for 'revenue')."
    )

    # Slide 6: Future Roadmap
    pdf.add_slide(
        "6. Future Roadmap (Version 2.0)",
        "This prototype lays the groundwork for enterprise-wide scaling:\n\n"
        "- Cloud Integration: Migrate from local SQLite to Snowflake/BigQuery.\n"
        "- Governance: Implement Row-Level Security so users only query their authorized regions.\n"
        "- Dynamic Visualizations: Allow the AI to generate Python-based charts on the fly.\n"
        "- Predictive Capabilities: Forecast stockouts before they happen based on current trajectories."
    )

    # Save PDF
    out_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'presentation.pdf')
    pdf.output(out_path)
    print(f"Presentation generated at {out_path}")

if __name__ == '__main__':
    generate_presentation()
