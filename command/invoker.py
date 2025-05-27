class CLIInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results