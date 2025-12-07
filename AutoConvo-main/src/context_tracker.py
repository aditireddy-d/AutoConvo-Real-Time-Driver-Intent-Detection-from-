class ContextTracker:
    def __init__(self):
        self.memory = {}

    def update(self, intent, entities):
        self.memory['last_intent'] = intent
        self.memory['entities'] = entities

    def resolve(self, text):
        if "him" in text and 'name' in self.memory.get("entities", {}):
            name = self.memory["entities"]["name"]
            return text.replace("him", name)
        return text
