from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError
from .interpreter import LogoInterpreter
from .parser import LogoParser


def parse_logo_http_response(code: str) -> tuple[dict, int]:
    """Parse logo code and return HTTP response.

    Args:
        code (str): The logo code.

    Returns:
        tuple[dict, int]: A HTTP response.
    """
    try:
        parser = LogoParser()
        interpreter = LogoInterpreter()
        return interpreter.run(parser.run(code)), 200
    except ParserInvalidCommandError as e:
        return {"error": str(e)}, 400
    except ParserUnexpectedTokenError as e:
        return {"error": str(e)}, 400
