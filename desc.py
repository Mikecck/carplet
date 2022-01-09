class Description:
    def __init__(self, event_display: str):
        self.event_display = event_display
    
    def update(self, event_updated: str):
        self.event_display = event_updated
    
    def display(self):
        return self.event_display
