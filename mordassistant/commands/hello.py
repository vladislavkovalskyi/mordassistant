from mordassistant.tools import Command

command = Command()


@command.new(["привет", "hello", "здравствуй", "здравствуйте", "прив"])
def hello():
    print(f"[BOT] Привет!")
