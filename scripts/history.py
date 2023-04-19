import json
import os


class History:
    def __init__(self, name=None):
        if name is None:
            name = "history"
        self.name = name
        self.file_name = f"{self.name}.json"
        file_exists = False
        if os.path.isfile(self.file_name):
            file_exists = True
        with open(self.file_name, 'a') as file:
            if not file_exists:
                json.dump([], file)
                file.flush()
                file.close()

    def save_history(self, full_history=None):
        if full_history is None:
            full_history = []

        with open(self.file_name, "w") as file:
            json.dump(full_history, file)
            file.flush()
            file.close()

    def load_history(self):
        print(self.file_name)
        with open(self.file_name, "r") as file:
            return json.load(file)
