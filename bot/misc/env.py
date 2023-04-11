from os import environ
from abc import ABC
from typing import Final


class Env(ABC):
    TOKEN: Final = environ.get('TOKEN', 'TOKEN HERE')
