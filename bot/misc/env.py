from abc import ABC
from dataclasses import dataclass
from os import environ
from typing import Final


@dataclass
class Env(ABC):
    TOKEN: Final = environ.get('TOKEN', 'TOKEN HERE')
