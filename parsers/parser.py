from typing import Protocol


class Parser(Protocol):
    """A basic parser"""

    def parse(self) -> str:
        """Parse some data"""
