
class Command:
    def __init__(self):
        self.commands = {}

    def new(self, keywords: list[str]):
        def decorator(func):
            for keyword in keywords:
                self.commands[keyword] = func
            return func
        return decorator


