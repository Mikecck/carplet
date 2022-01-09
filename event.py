class Event:
    def __init__(self, title: str, desc: str) -> None:
        self._title = title
        self._desc = desc

    @property
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc
