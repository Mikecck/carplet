import json
import os
from typing import List
from event import Event
from card import Card


class ImportSetting:
    def __init__(self, json_file: str) -> None:
        if not os.path.exists(json_file):
            raise FileNotFoundError("File not found")  # one file, one plot

        with open(json_file, 'r') as f:
            self._json_data = json.load(f)  # Expects an array of events

    def read_plot(self) -> List[Event]:
        events = []
        for raw_event in self._json_data:
            cards = []
            for raw_card in raw_event['cards']:
                cards.append(Card(raw_card['title'], raw_card['desc'], raw_card['effects'], raw_card['cons']))
            events.append(Event(raw_event['title'], raw_event['desc'], cards))

        return events
