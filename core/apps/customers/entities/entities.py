import datetime
from dataclasses import dataclass


@dataclass
class CustomerEntity:
    phone: str
    created_at: datetime
