ERROR_SUFFIX = """Please use one of the commands provided below:

    (forward | fd) <number>
    (backward | bk) <number>
    (left | lt) <number>
    (right | rt) <number>
    showturtle | st
    hideturtle | ht
    penup | pu
    pendown | pd"""

INVALID_COMMAND_ERROR_MESSAGE = f"Invalid command. {ERROR_SUFFIX}"

UNEXPECTED_TOKEN_ERROR_MESSAGE = f"Unexpected token. {ERROR_SUFFIX}"
