"""Object-oriented models for a domestic financial management system."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List


@dataclass(frozen=True)
class Transaction:
    """Represents one household financial event."""

    amount: float
    category: str
    description: str
    transaction_date: date
    is_income: bool = False

    def signed_amount(self) -> float:
        """Return a signed value: positive for income, negative for expense."""
        return self.amount if self.is_income else -self.amount


@dataclass
class Account:
    """Represents a financial account used by a household."""

    name: str
    starting_balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    @property
    def current_balance(self) -> float:
        return self.starting_balance + sum(t.signed_amount() for t in self.transactions)

    def expenses_by_category(self) -> Dict[str, float]:
        totals: Dict[str, float] = {}
        for transaction in self.transactions:
            if transaction.is_income:
                continue
            totals[transaction.category] = totals.get(transaction.category, 0.0) + transaction.amount
        return totals


@dataclass
class MonthlyBudget:
    """Stores planned spending caps per category."""

    month_label: str
    limits: Dict[str, float] = field(default_factory=dict)

    def set_limit(self, category: str, amount: float) -> None:
        self.limits[category] = amount

    def remaining(self, category: str, spent: float) -> float:
        if category not in self.limits:
            raise KeyError(f"No budget configured for category '{category}'.")
        return self.limits[category] - spent


class DomesticFinanceManager:
    """Coordinator class that applies OOP over accounts, budgets, and reporting."""

    def __init__(self) -> None:
        self.accounts: Dict[str, Account] = {}
        self.budget: MonthlyBudget | None = None

    def add_account(self, account: Account) -> None:
        self.accounts[account.name] = account

    def configure_budget(self, budget: MonthlyBudget) -> None:
        self.budget = budget

    def record_transaction(self, account_name: str, transaction: Transaction) -> None:
        if account_name not in self.accounts:
            raise KeyError(f"Account '{account_name}' is not registered.")
        self.accounts[account_name].add_transaction(transaction)

    def total_net_worth(self) -> float:
        return sum(account.current_balance for account in self.accounts.values())

    def monthly_summary(self) -> dict:
        total_income = 0.0
        total_expenses = 0.0
        category_spending: Dict[str, float] = {}

        for account in self.accounts.values():
            for transaction in account.transactions:
                if transaction.is_income:
                    total_income += transaction.amount
                else:
                    total_expenses += transaction.amount
                    category_spending[transaction.category] = (
                        category_spending.get(transaction.category, 0.0) + transaction.amount
                    )

        report = {
            "total_income": round(total_income, 2),
            "total_expenses": round(total_expenses, 2),
            "net_savings": round(total_income - total_expenses, 2),
            "category_spending": category_spending,
        }

        if self.budget is not None:
            budget_status: Dict[str, float] = {}
            for category, limit in self.budget.limits.items():
                spent = category_spending.get(category, 0.0)
                budget_status[category] = round(limit - spent, 2)
            report["budget_remaining"] = budget_status

        return report
