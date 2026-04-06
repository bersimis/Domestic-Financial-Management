from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List


# -------------------- Transaction --------------------
@dataclass(frozen=True)
class Transaction:
    amount: float
    category: str
    description: str
    transaction_date: date
    is_income: bool = False

    def signed_amount(self) -> float:
        return self.amount if self.is_income else -self.amount


# -------------------- Account --------------------
@dataclass
class Account:
    name: str
    starting_balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_balance(self) -> float:
        return self.starting_balance + sum(t.signed_amount() for t in self.transactions)


# -------------------- Budget --------------------
@dataclass
class MonthlyBudget:
    month: str
    limits: Dict[str, float] = field(default_factory=dict)

    def set_limit(self, category: str, amount: float):
        self.limits[category] = amount


# -------------------- Manager --------------------
class FinanceManager:

    def __init__(self):
        self.accounts = {}
        self.budget = None

    def add_account(self, account: Account):
        self.accounts[account.name] = account

    def set_budget(self, budget: MonthlyBudget):
        self.budget = budget

    def add_transaction(self, account_name: str, transaction: Transaction):
        if account_name in self.accounts:
            self.accounts[account_name].add_transaction(transaction)

    def total_balance(self):
        return sum(acc.get_balance() for acc in self.accounts.values())
