from ninja import Schema

from core.api.filtres import DefaultFilter

class ProductFilters(Schema):
    search: str | None = None