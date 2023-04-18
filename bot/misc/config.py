from abc import ABC
from dataclasses import dataclass
from typing import Final


@dataclass
class Config(ABC):
    HELPER_URL: Final = '@InDigitalE8'
    MATRIX_PARSE_URL: Final = "https://matritsa-sudbi.ru/"
