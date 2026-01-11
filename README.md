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


## ❓ Problem Statement

Most individuals and small teams struggle to extract meaningful insights from raw datasets. 
While tools like Excel, BI dashboards, or basic AI chatbots exist, they often fail in one or more of the following ways:

- They require users to already know *what questions to ask*
- They generate charts without explaining *why patterns exist*
- AI chatbots provide confident answers without validating them using real data
- Insights are descriptive, not actionable

As a result, users are left with:
- Unvalidated assumptions
- Misinterpreted correlations
- Time-consuming manual analysis
- Decisions based on intuition rather than evidence

There is a clear gap between **raw data** and **decision-ready insights**.

AnalystGPT was built to bridge this gap.


## ✅ Solution Overview

AnalystGPT acts as an AI-powered data analyst that:

- Automatically understands the structure and quality of any CSV dataset
- Generates meaningful, testable hypotheses instead of vague insights
- Validates each hypothesis using real statistical computation (not guesswork)
- Explains results in clear business language
- Suggests practical next steps based on evidence

Instead of asking users to analyze data,
the system analyzes the data *for them* — correctly and transparently.

## 💡 Use Cases

### 1️⃣ Business & Startup Analysis
- Analyze customer behavior and churn patterns
- Identify high-value customers based on spending and engagement
- Validate assumptions before making marketing or pricing decisions
- Quickly explore datasets without hiring a full-time analyst

### 2️⃣ Data Science & Machine Learning Education
- Helps students understand how hypotheses are formed from data
- Demonstrates real statistical validation instead of black-box AI answers
- Teaches the difference between correlation, causation, and assumption
- Acts as a learning companion for EDA and analytics concepts

### 3️⃣ Hackathons & Rapid Prototyping
- Instantly analyze unfamiliar datasets under time constraints
- Generate insights faster than manual analysis
- Impress judges with real computation + AI reasoning
- Move from data upload to decision insight within minutes

### 4️⃣ Portfolio & Interview Demonstrations
- Showcases real-world AI system design (not just model training)
- Demonstrates responsible AI (no hallucinated insights)
- Highlights integration of LLMs with traditional data analysis
- Useful for ML Engineer, Data Analyst, and AI Engineer roles

### 5️⃣ Non-Technical Users
- Enables founders, managers, and domain experts to understand data
- No need to write SQL, Python, or statistics formulas
- Converts raw CSV files into understandable business insights


## 🧭 Roadmap

📊 Auto-generate charts (scatter, bar, hist)
🧠 Action recommendation scoring system
📡 Multi-dataset upload support
🧾 Exportable PDF business report
🧬 Memory mode — AI remembers company data

## 👤 Author

- Developed by: Mohana Krishna Sesetti
- Role: ML Engineer — AI Systems Builder
- LinkedIn: https://www.linkedin.com/in/mohana-krishna-sesetti-a29aa3390/
