from typing import List


class Card:
    def __init__(self, title: str, desc: str, effects: List[int]) -> None:
        if title == "":
            raise ValueError("Card title cannot be empty string")
        if desc == "":
            raise ValueError("Card description cannot be empty string")

        for e in effects:
            if e < 0:
                raise ValueError("Card effects must not be negative")

        self._title = title
        self._desc = desc
        self._effects = effects

    @property
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

    @property
    def effects(self):
        return self._effects