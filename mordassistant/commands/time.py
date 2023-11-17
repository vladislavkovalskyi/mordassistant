from mordassistant.tools import Command
from time import strftime

command = Command()


@command.new(["время", "скажи время", "который час", "сколько времени", "сколько время", "маякни время"])
def current_time():
    print(f"[BOT] Сейчас: {strftime('%H:%M')}")
