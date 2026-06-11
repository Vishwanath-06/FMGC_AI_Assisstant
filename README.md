[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.14-green.svg)](https://python.langchain.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**FMCG AI Assistant** is an AI-powered conversational workspace designed specifically for business users in the Consumer Goods (FMCG) Beverages category. Built using **LangChain** and **Streamlit**, it provides an intuitive Text-to-SQL interface to instantly query promotional performance, inventory movement, regional sales, and product-level campaign impacts without needing manual dashboarding or data analysts.

## ✨ Features
- 🌐 **Conversational Interface**: Ask natural language questions about your business data.
- 🚀 **Text-to-SQL Engine**: Powered by LangChain's SQL Agent to automatically write and execute accurate database queries.
- 📊 **Synthetic Data Pipeline**: Includes a built-in generator mimicking real-world FMCG sales, promotions, and inventory patterns.
- 🔄 **Multi-LLM Support**: Seamlessly switch between **Google Gemini** and **OpenAI** based on your API key.
- 🎨 **Streamlit UI**: Elegant, interactive chat layout with built-in history and state management.
- ✅ **Robust Testing**: Comprehensive test suite validating database integrity and agent initialization.

## 🏗️ Architecture
```text
┌─────────────────────────────────────────────────────────────┐
│ FMCG AI Assistant │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────┐ ┌─────────────────────────┐ │
│ │ Streamlit UI │◄────────────►│ LangChain SQL Agent │ │
│ │ (Chat Interface)│ │ (Prompt + Schema Context) │ │
│ └─────────────────┘ └──────────┬──────────────┘ │
│ │ │
│ ┌─────────▼─────────┐ ┌─────────▼─────────┐ │
│ │ LLM Provider │ │ SQLite Database │ │
│ │ (OpenAI / Gemini) │ │ (FMCG Star Schema)│ │
│ └───────────────────┘ └───────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 📋 Prerequisites
- **Python 3.10+**
- **OpenAI API Key** OR **Google Gemini API Key**

### 1. Clone the Repository
```bash
git clone https://github.com/Vishwanath-06/FMGC_AI_Assisstant.git
cd FMGC_AI_Assisstant
```

### 2. Set Up Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate the FMCG Database
Generate the synthetic 24,000-row dataset containing products, stores, weekly sales, and inventory metrics:
```bash
python data_generation/generate_data.py
```

### 5. Run the Application
```bash
streamlit run app/app.py
```
*Access at: http://localhost:8501*

## 📁 Project Structure
```text
fmgc_ai/
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── app/                        # Application Code
│   ├── app.py                  # Streamlit frontend & UI logic
│   ├── agent.py                # LangChain SQL Agent configuration
│   └── __init__.py             
│
├── data_generation/            # Data Engineering
│   ├── generate_data.py        # Pandas/NumPy synthetic data generator
│   └── fmcg_data.db            # Generated SQLite database (Ignored in Git)
│
├── docs/                       # Assessment Documentation
│   ├── M4_System_Design.md     # Discovery & Architecture choices
│   ├── M5_Data_Pipeline.md     # Schema & Generation logic
│   ├── M6_Build_and_Code.md    # Technical execution details
│   ├── M7_System_Deployment.md # Deployment strategy
│   ├── M8_Communication.md     # Presentation structure
│   ├── M9_Reflection.md        # V2 Improvements & Learnings
│   └── test_results.md         # Validated test outputs
│
└── tests/                      # Testing Suite
    ├── test_features.py        # Verifies FMCG business logic via SQL
    └── test_app_and_agent.py   # Validates Streamlit UI & Agent wiring
```

## 🧪 Testing
We provide extensive testing to ensure data accuracy and application stability.

```bash
# Run business feature tests (Tests promotional impacts, stockouts, etc.)
python tests/test_features.py

# Run application & integration tests (Tests Agent init and Streamlit UI)
python tests/test_app_and_agent.py
```

## 📄 License
This project is licensed under the MIT License.

## 📞 Contact
- ### T. Vishwanath -  *[GitHub](https://github.com/Vishwanath-06)*

Built with ❤️ for Data Analytics | Transforming FMCG Insights 🍹
