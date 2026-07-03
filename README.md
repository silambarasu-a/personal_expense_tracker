# Personal Expense Tracker

A simple command-line expense tracker written in pure Python (no external dependencies). Expenses are stored locally as JSON, making this a lightweight tool for recording and reviewing day-to-day spending.

## Features

- **Add Expense** — record an expense with title, amount, category, date, payment method, and optional notes. Each entry gets a unique ID and creation timestamp.
- **View All Expenses** — *coming soon*
- **View Expense Summary** — *coming soon*
- **Set Monthly Budget** — *coming soon*

### Categories

Food, Travel, Shopping, Bills, Entertainment, Health, Education, Rent, Others

### Payment Methods

Cash, UPI, Credit Card, Debit Card, Bank Transfer, Other

## Requirements

- Python 3.x (standard library only — `json`, `uuid`, `datetime`)

## Getting Started

```bash
cd personal_expense_tracker
python main.py
```

You'll see an interactive menu:

```
1. Add Expense
2. View All Expenses
3. View Expense Summary
4. Set Monthly Budget
5. Exit
```

Enter a number to pick an option and follow the prompts.

> **Note:** Run the program from inside the `personal_expense_tracker` directory so it can find the `data/` folder.

## Project Structure

```
personal_expense_tracker/
├── main.py              # Entry point — menu loop and user choices
├── expense_manager.py   # Core features: add/view expenses, summary, budget
├── storage.py           # Load, save, and append data to the JSON store
├── validators.py        # Input validation (e.g. YYYY-MM-DD date format)
├── constants.py         # Expense categories and payment methods
├── utils.py             # Shared helpers
└── data/
    ├── expenses.json    # Saved expenses
    └── settings.json    # App settings (e.g. monthly budget)
```

## Data Format

Each expense is stored in `data/expenses.json` as:

```json
{
    "_id": "a1b2c3d4-...",
    "title": "Groceries",
    "amount": 450.0,
    "category": "Food",
    "date": "2026-07-03",
    "payment_method": "UPI",
    "notes": "Weekly shopping",
    "created_at": "2026-07-03 10:15:30.123456"
}
```

## Roadmap

- [ ] View all expenses in a formatted list
- [ ] Expense summary (totals by category / month)
- [ ] Monthly budget with overspend warnings
- [ ] Edit and delete expenses
