# personal-finance-agent

> Tracking personal finances manually across spreadsheets is error-prone and slow. This agent automates expense categorization, allocates budgets from income, checks spending limits, flags upcoming bills, and generates plain-text suggestions — all from a CSV file and a JSON config.

---

## The Problem it Solves

Most people either don't track expenses at all, or maintain spreadsheets that go stale. This project builds a modular finance agent that reads real transaction data, categorizes it automatically by keyword matching, compares it against income-based budget limits, and tells you exactly where you're over or under — without manual input beyond your transaction CSV and bill dates.

---

## How it Works

```
transactions.csv (expense data)
        ↓
expense_tracker.py  →  Loads CSV, keyword-matches descriptions
                        to categories, summarizes spend per category
        ↓
budget.py  →  Takes income + selected categories,
              allocates percentage-based limits per category
        ↓
budget check  →  Compares actual spend vs budget per category
                 Returns status: Over / Under + difference
        ↓
suggestion.py  →  Reads check report, generates plain-text
                  nudges for over-budget categories
        ↓
reminder.py  →  Reads bills.json, returns bills due
                within next 7 days (configurable window)
```

---

## Module Breakdown

| Module | Responsibility |
|--------|---------------|
| `expense_tracker.py` | Loads CSV, maps description keywords to categories, groups total spend per category |
| `budget.py` | Allocates budget from income using default percentages, checks actual vs budgeted spend |
| `suggestion.py` | Generates a plain-text suggestion per category based on Over/Under status |
| `reminder.py` | Parses bills from JSON, flags any due within a configurable day window (default 7) |

---

## Budget Allocation Logic

Budget limits are assigned as a percentage of monthly income. Categories not in the default map fall back to 5%:

| Category | Default % of Income |
|----------|-------------------|
| Rent | 30% |
| Groceries | 20% |
| Entertainment | 10% |
| Transportation | 10% |
| Health | 5% |
| Clothing | 5% |
| Other (default) | 5% |

---

## Expense Categorization Logic

Categorization works by keyword matching on the `Description` field of the CSV. No ML, no API — deterministic and transparent:

| Keyword in Description | Assigned Category |
|----------------------|-------------------|
| groceries, supermarket | Groceries |
| restaurant, dining | Restaurants |
| gas | Gas |
| entertainment, movie, theater | Entertainment |
| transportation, bus, car | Transportation |
| health, doctor, pharmacy | Health |
| clothing, shoes, dress | Clothing |
| anything else | Other |

---

## Technical Decisions Worth Noting

**Keyword matching over ML classification** — For personal finance at this scale, deterministic keyword matching is faster, more predictable, and requires no training data. Every categorization decision is traceable to a single string check.

**Separation of budget creation and budget checking** — `create_budget()` and `check_budget()` are intentionally two separate functions. Budget allocation (from income) and spend comparison (from transactions) are independent concerns — one can be rerun without affecting the other.

**Partial credit in suggestion tone** — `suggestion.py` doesn't just flag failures. Under-budget categories get a positive confirmation alongside over-budget warnings. This makes the output actionable rather than just a list of problems.

**Bill reminder uses a configurable window** — `check_bill_reminders()` takes `window_days=7` as a parameter. The default is 7 days but can be changed per call without modifying the function — designed for reuse across different reminder schedules.

**No external API dependency** — The entire pipeline runs locally. No LLM, no cloud service, no rate limits. The only external libraries are `pandas`, `schedule`, and `python-dotenv`.

---

## Input Formats

**Transactions CSV** — minimum required columns:

| Column | Description |
|--------|-------------|
| `Description` | Transaction text used for keyword categorization |
| `Amount` | Spend amount in any currency |

**Bills JSON** — list of bill objects:

```json
[
  { "name": "Electricity", "due_date": "2025-05-10" },
  { "name": "Internet",    "due_date": "2025-05-14" }
]
```

---

## Project Structure

```
personal-finance-agent/
├── modules/
│   ├── budget.py           # Budget allocation + spend check
│   ├── expense_tracker.py  # CSV loading, categorization, summarization
│   ├── reminder.py         # Bill reminder from JSON config
│   └── suggestion.py       # Plain-text suggestions from budget report
├── Test/
│   ├── test_budget.py
│   ├── test_expense_tracker.py
│   ├── test_reminder.py
│   └── test_suggestion.py
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone https://github.com/parthrudrawar/personal-finance-agent.git
cd personal-finance-agent

pip install -r requirements.txt

echo "OPENAI_API_KEY=your_key_here" > .env

streamlit run modules/app.py
```

## Running Tests

```bash
pytest Test/
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Streamlit** | UI |
| **LangChain + OpenAI** | LLM integration |
| **Langflow** | Agent workflow |
| **pandas** | CSV loading and spend summarization |
| **schedule** | Reminder scheduling |
| **python-dotenv** | Environment config |
| **pytest** | Unit tests per module |

---

## Author

[parthrudrawar](https://github.com/parthrudrawar)
