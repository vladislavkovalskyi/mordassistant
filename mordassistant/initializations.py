from mordassistant.tools import Recognizer
from mordassistant.commands import commands_list
recognizer = Recognizer()

for command_module in commands_list:
    recognizer.load_command(command_module.command)
