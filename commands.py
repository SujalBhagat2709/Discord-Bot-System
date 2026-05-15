commands = {
    "!hello": "Hello user!",
    "!help": "Available commands: !hello, !help",
    "!ai": "AI systems are awesome."
}

def handle_command(command):
    
    return commands.get(
        command,
        "Unknown command"
    )


if __name__ == "__main__":
    
    print(handle_command("!hello"))