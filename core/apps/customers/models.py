from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.entities import CustomerEntity


class Customer(TimedBaseModel):
    phone = models.CharField(verbose_name="Номер телефона", max_length=20, unique=True)
    token = models.CharField(
        max_length=255,
        verbose_name="Пользовательский токен",
        default=uuid4,
        unique=True,
    )

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(phone=self.phone, created_at=self.created_at)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self) -> str:
        return self.phone
