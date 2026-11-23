from dataclasses import dataclass
import datetime
from decimal import Decimal

@dataclass(frozen=True)
class Transaction:
    date: datetime.date
    amount: Decimal
    currency: str
    raw_description: str
    source: str