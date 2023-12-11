# Standard Library
from typing import Any


class Action:
    def __init__(self, name: str, description: str, args: dict) -> None:
        self.name = name
        self.description = description
        self.args = args

    def run(self, *args: Any) -> tuple[bytes, bytes]:
        raise NotImplementedError("Action.run() must be implemented by subclass")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
