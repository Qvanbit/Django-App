from abc import ABC
from dataclasses import dataclass
from typing import Iterable

from core.apps.customers.entities.entities import CustomerEntity


class BaseSenderService(ABC):
    def send_code(self, customer: CustomerEntity, code: str) -> None: ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}:, sent: {code}")


class EmailSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code code {code} to user: customer_email")


class PushSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code sent code {code} to user in push notification")


@dataclass
class ComposedSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer, code)
