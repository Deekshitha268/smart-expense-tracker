from utils import load_expenses, save_expenses


def get_all_expenses():
    return load_expenses()


def add_expense(expense):
    expenses = load_expenses()

    next_id = 1
    if expenses:
        next_id = max(exp["id"] for exp in expenses) + 1

    expense["id"] = next_id

    expenses.append(expense)

    save_expenses(expenses)

    return expense


def delete_expense(expense_id):
    expenses = load_expenses()

    updated = [exp for exp in expenses if exp["id"] != expense_id]

    if len(updated) == len(expenses):
        return False

    save_expenses(updated)

    return True


def filter_by_category(category):
    expenses = load_expenses()

    return [
        exp
        for exp in expenses
        if exp["category"].lower() == category.lower()
    ]


def calculate_total(category=None):
    expenses = load_expenses()

    if category:
        expenses = [
            exp
            for exp in expenses
            if exp["category"].lower() == category.lower()
        ]

    total = sum(exp["amount"] for exp in expenses)

    return total