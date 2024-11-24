from python_logo.interpreter import LogoInterpreter
from python_logo.parser import LogoParser


class ParserTests:
    """Test suite for validating the functionality of
    the LogoParser and LogoInterpreter.
    """

    def __init__(self):
        """Initializes the ParserTests instance."""
        self.parser = LogoParser()
        self.interpreter = LogoInterpreter()

    def test_forward(self):
        forward_input = "forward 100"
        forward_alias_input = "fd 100"
        forward_response = {"commands": [{"name": "forward", "value": 100}]}
        assert self.interpreter.run(self.parser.run(forward_input)) == forward_response
        assert (
            self.interpreter.run(self.parser.run(forward_alias_input))
            == forward_response
        )

    def test_backward(self):
        backward_input = "backward 100"
        backward_alias_input = "bk 100"
        backward_response = {"commands": [{"name": "backward", "value": 100}]}
        assert (
            self.interpreter.run(self.parser.run(backward_input)) == backward_response
        )
        assert (
            self.interpreter.run(self.parser.run(backward_alias_input))
            == backward_response
        )

    def test_left(self):
        left_input = "left 90"
        left_alias_input = "lt 90"
        left_response = {"commands": [{"name": "left", "value": 90}]}
        assert self.interpreter.run(self.parser.run(left_input)) == left_response
        assert self.interpreter.run(self.parser.run(left_alias_input)) == left_response

    def test_right(self):
        right_input = "right 90"
        right_alias_input = "rt 90"
        right_response = {"commands": [{"name": "right", "value": 90}]}
        assert self.interpreter.run(self.parser.run(right_input)) == right_response
        assert (
            self.interpreter.run(self.parser.run(right_alias_input)) == right_response
        )

    def test_showturtle(self):
        showturtle_input = "showturtle"
        showturtle_alias_input = "st"
        showturtle_response = {"commands": [{"name": "showturtle"}]}
        assert (
            self.interpreter.run(self.parser.run(showturtle_input))
            == showturtle_response
        )
        assert (
            self.interpreter.run(self.parser.run(showturtle_alias_input))
            == showturtle_response
        )

    def test_hideturtle(self):
        hideturtle_input = "hideturtle"
        hideturtle_alias_input = "ht"
        hideturtle_response = {"commands": [{"name": "hideturtle"}]}
        assert (
            self.interpreter.run(self.parser.run(hideturtle_input))
            == hideturtle_response
        )
        assert (
            self.interpreter.run(self.parser.run(hideturtle_alias_input))
            == hideturtle_response
        )

    def test_penup(self):
        penup_input = "penup"
        penup_alias_input = "pu"
        penup_response = {"commands": [{"name": "penup"}]}
        assert self.interpreter.run(self.parser.run(penup_input)) == penup_response
        assert (
            self.interpreter.run(self.parser.run(penup_alias_input)) == penup_response
        )

    def test_pendown(self):
        pendown_input = "pendown"
        pendown_alias_input = "pd"
        pendown_response = {"commands": [{"name": "pendown"}]}
        assert self.interpreter.run(self.parser.run(pendown_input)) == pendown_response
        assert (
            self.interpreter.run(self.parser.run(pendown_alias_input))
            == pendown_response
        )

    def test_all(self):
        logo_input = """
            forward 20
            fd 30
            backward 40
            bk 50
            left 60
            lt 70
            right 80
            rt 90
            hideturtle
            ht
            showturtle
            st
            penup
            pu
            pendown
            pd
        """
        logo_response = {
            "commands": [
                {"name": "forward", "value": 20},
                {"name": "forward", "value": 30},
                {"name": "backward", "value": 40},
                {"name": "backward", "value": 50},
                {"name": "left", "value": 60},
                {"name": "left", "value": 70},
                {"name": "right", "value": 80},
                {"name": "right", "value": 90},
                {"name": "hideturtle"},
                {"name": "hideturtle"},
                {"name": "showturtle"},
                {"name": "showturtle"},
                {"name": "penup"},
                {"name": "penup"},
                {"name": "pendown"},
                {"name": "pendown"},
            ]
        }
        assert self.interpreter.run(self.parser.run(logo_input)) == logo_response
