from flask_socketio import SocketIO

from .interpreter import LogoInterpreter
from .parser import parse_logo


def register_events(socketio: SocketIO) -> None:
    """Registers the socketio events for the application.

    Args:
        socketio (SocketIO): The socketio object.
    """

    @socketio.on("connect")
    def connect() -> None:
        """Event handler for when a client connects to the server."""
        print("Client connected")

    @socketio.on("run")
    def run(code: str) -> None:
        """Event handler for when a client sends a run event.

        Args:
            code (str): The Logo code to run.
        """
        logo_tree = parse_logo(code)
        interpreter = LogoInterpreter()
        for command in interpreter.generator(logo_tree):
            socketio.emit("execute", command)
