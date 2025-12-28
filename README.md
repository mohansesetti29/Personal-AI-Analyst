# 📊 AnalystGPT — AI-Powered Personal Data Analyst
AnalystGPT is a real-time AI system that **analyzes any CSV dataset**, generates **data-driven hypotheses**, **validates them using real numerical computation**, and provides **business-ready insights & explanations** — just like a professional analyst.

This is not a basic chatbot.  
It is a **decision-support engine** — combining:
✔ Large Language Models (Groq – Llama-3.1-8B)  
✔ Pandas-powered statistical validation  
✔ Automatic data profiling (EDA)  
✔ Hypothesis generation + validation  
✔ Analyst-level business reasoning  

---

## 🚀 Features
| Feature | Description |
|--------|-------------|
| 📁 CSV Upload | Analyze any dataset instantly |
| 🔍 Auto-EDA | Extracts schema, summary stats, missing values |
| 🧠 Hypothesis Generation | AI creates 3 business-focused, testable hypotheses |
| 🔬 Hypothesis Validation | Correlation test, mean comparison, churn check |
| 👔 Analyst Explanation | Executive-style actionable insights |
| 🧱 Local Processing | CSV stays on your device |
| 💻 Streamlit UI | Interactive dashboard – demo friendly |

---

## 🧠 Architecture Diagram
        ┌────────────── ┐
        │   User CSV    │
        └───────┬───────┘
                │
        ┌───────▼───────── ┐
        │ Auto-EDA (Pandas)│
        └───────┬───────── ┘
                │ dataset summary
        ┌───────▼──────────────┐
        │ LLM: Hypothesis Gen  │  (Groq – Llama-3.1-8B)
        └───────┬──────────────┘
                │ user selects
        ┌───────▼──────────────┐
        │ Python Validator      │ (Real math)
        └───────┬──────────────┘
                │
        ┌───────▼──────────────┐
        │ AI Analyst Explanation│
        └───────────────────────┘

---

## 📂 Folder Structure

analystgpt/
│ app.py
│ README.md
│ requirements.txt
│ .env
└── backend/
    ├── agent.py
    ├── llm.py
    ├── memory.py
    └── tools/
        ├── eda.py
        ├── stats.py
        ├── plots.py
        └── validate.py


## 🧪 Example Output

Hypothesis:
"High spending customers place more orders."

Validation:
Correlation = 0.82 → strong positive relationship

Business Interpretation:
Customers who spend more also tend to order more.

Action:
Launch loyalty perks or bundle discounts for users with >8 orders.

Risk:
Dataset small → seasonal trends unknown.


## 🛠 Installation & Setup

1️⃣ Clone Repo
git clone <your_repo_url>
cd analystgpt

2️⃣ Create Virtual Env
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Mac/Linux

3️⃣ Install requirements
pip install -r requirements.txt

4️⃣ Add API Key
Create .env and add:
GROQ_API_KEY=your_key_here

5️⃣ Run Application
streamlit run app.py


## 🎯 Why This Project Matters


Most AI tools only generate text — they do NOT compute or validate anything.

AnalystGPT is different:
- It performs true mathematical validation (correlations, averages, churn analysis)
- Uses AI only for reasoning, not fake answers
- Turns any CSV into business decisions
- Useful for students, founders, analysts, hackathons, and ML portfolios

In short: 
Upload a CSV → AI tells what matters → proves it → tells what action to take.


## 🧭 Roadmap

📊 Auto-generate charts (scatter, bar, hist)
🧠 Action recommendation scoring system
📡 Multi-dataset upload support
🧾 Exportable PDF business report
🧬 Memory mode — AI remembers company data

## 👤 Author

Developed by: Mohana Krishna Sesetti
Role: ML Engineer — AI Systems Builder
LinkedIn: https://www.linkedin.com/in/mohana-krishna-sesetti-a29aa3390/
