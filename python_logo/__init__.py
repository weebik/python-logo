from flask import Flask
from flask_socketio import SocketIO

from .events import register_events
from .interpreter import Interpreter
from .parser import parse
from .routes import main
from .utils import run

__all__ = ["Interpreter", "create_app", "parse", "run"]

socketio = SocketIO()


def create_app() -> Flask:
    """Creates and configures the Flask application with socketio.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(main)
    register_events(socketio)
    socketio.init_app(app)
    return app
