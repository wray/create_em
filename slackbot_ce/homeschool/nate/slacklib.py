# Put your commands here
COMMAND1 = "go away"
COMMAND2 = "go away now"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "never"
    elif command.find(COMMAND2) >=0:
        response = "no"
        
    return response = "never"
