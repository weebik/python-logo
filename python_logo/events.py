from flask_socketio import SocketIO

from .exceptions import (
    InterpreterInvalidCommandError,
    InterpreterInvalidTreeError,
    ParserInvalidCommandError,
    ParserUnexpectedTokenError,
)
from .interpreter import Interpreter
from .parser import parse


def register_events(socketio: SocketIO) -> None:
    """Registers the socketio events for the application.

    Args:
        socketio (SocketIO): The socketio object.
    """

    @socketio.on("run")
    def run(code: str) -> None:
        """Event handler for when a client sends a run event.

        Args:
            code (str): The Logo code to run.
        """
        try:
            tree = parse(code)
        except (ParserInvalidCommandError, ParserUnexpectedTokenError) as e:
            socketio.emit("error", str(e))
            return

        try:
            interpreter = Interpreter(tree)
        except InterpreterInvalidTreeError as e:
            socketio.emit("error", str(e))
            return

        try:
            for command in interpreter:
                socketio.emit("execute", command)
        except (InterpreterInvalidTreeError, InterpreterInvalidCommandError) as e:
            socketio.emit("error", str(e))
            return
