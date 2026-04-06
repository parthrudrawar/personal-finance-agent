# personal-finance-agent

A personal finance assistant built with Python. Tracks expenses from a CSV, allocates budgets by category, checks spending against limits, flags upcoming bill reminders, and gives simple suggestions based on where you're over or under budget.

---

## What it does

**Expense Tracking** — Loads transactions from a CSV file, auto-categorizes them by keyword matching on the description field (e.g. "supermarket" → Groceries, "doctor" → Health), and summarizes total spending per category.

**Budget Allocation** — Takes your income and selected categories, assigns default percentage-based limits (Rent 30%, Groceries 20%, Entertainment 10%, etc.), and returns a per-category budget.

**Budget Check** — Compares actual spending against the budget and reports how much is over or under for each category.

**Suggestions** — Generates plain-text spending suggestions based on the budget report. Over-budget categories get a nudge to reduce, under-budget ones get a confirmation.

**Bill Reminders** — Reads bills from a JSON config file and returns any bills due within the next 7 days (configurable window).

---

## Project Structure
```
personal-finance-agent/
├── modules/
│   ├── budget.py           # Budget creation and check
│   ├── expense_tracker.py  # CSV loading, categorization, summarization
│   ├── reminder.py         # Bill reminder from JSON config
│   └── suggestion.py       # Suggestions based on budget report
├── Test/
│   ├── test_budget.py
│   ├── test_expense_tracker.py
│   ├── test_reminder.py
│   └── test_suggestion.py
├── requirements.txt
└── README.md
```

---

## Input Format

**Expenses CSV** — expects at minimum:
| Column | Description |
|--------|-------------|
| `Description` | Transaction description (used for categorization) |
| `Amount` | Transaction amount |

**Bills JSON** — expects a list of bill objects:
```json
[
  { "name": "Electricity", "due_date": "2025-05-10" },
  { "name": "Internet",    "due_date": "2025-05-14" }
]
```

---

## Supported Categories

| Category | Default Budget % |
|----------|-----------------|
| Rent | 30% |
| Groceries | 20% |
| Entertainment | 10% |
| Transportation | 10% |
| Health | 5% |
| Clothing | 5% |
| Other | 5% |

---

## Tech Stack

- **Python**
- **Streamlit** — UI
- **LangChain + OpenAI** — LLM integration
- **Langflow** — agent workflow
- **pandas** — CSV processing
- **schedule** — task scheduling
- **python-dotenv** — environment config
- **pytest** — unit tests

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

## Author

[parthrudrawar](https://github.com/parthrudrawar)
