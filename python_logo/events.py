from flask_socketio import SocketIO

from .exceptions import (
    InterpreterInvalidCommandError,
    InterpreterInvalidTreeError,
    ParserInvalidCommandError,
    ParserUnexpectedTokenError,
)
from .utils import run


def register_events(socketio: SocketIO) -> None:
    """Registers the socketio events for the application.

    Args:
        socketio (SocketIO): The socketio object.
    """

    @socketio.on("run")
    def on_run(code: str) -> None:
        """Event handler for when a client sends a run event.

        Args:
            code (str): The Logo code to run.
        """
        try:
            logo_runner = run(code)
            for command in logo_runner:
                socketio.emit("execute", command)
        except (
            InterpreterInvalidCommandError,
            InterpreterInvalidTreeError,
            ParserInvalidCommandError,
            ParserUnexpectedTokenError,
        ) as err:
            socketio.emit("error", str(err))
