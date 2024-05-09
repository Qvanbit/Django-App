from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CodeException(ServiceException):
    @property
    def message(self):
        return "Application exception accured"


@dataclass(eq=False)
class CodeNotFoundException(CodeException):
    code: str

    @property
    def message(self):
        return "Code not found"


@dataclass(eq=False)
class CodeNotEqualException(CodeException):
    code: str
    cache_code: str
    customer_phone: str

    @property
    def message(self):
        return "Code is not equal"
