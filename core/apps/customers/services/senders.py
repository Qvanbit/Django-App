from abc import ABC

from core.apps.customers.entities.entities import CustomerEntity


class BaseSenderService(ABC):
    def send_code(self, customer: CustomerEntity, code: str) -> None: ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}:, sent: {code}")
