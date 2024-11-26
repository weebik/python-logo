from python_logo import Interpreter, parse


def test_forward():
    forward_input = "forward 100"
    forward_alias_input = "fd 100"
    forward_response = {"commands": [{"name": "forward", "value": 100}]}
    assert Interpreter(parse(forward_input)).interpret_all() == forward_response
    assert Interpreter(parse(forward_alias_input)).interpret_all() == forward_response


def test_backward():
    backward_input = "backward 100"
    backward_alias_input = "bk 100"
    backward_response = {"commands": [{"name": "backward", "value": 100}]}
    assert Interpreter(parse(backward_input)).interpret_all() == backward_response
    assert Interpreter(parse(backward_alias_input)).interpret_all() == backward_response


def test_left():
    left_input = "left 90"
    left_alias_input = "lt 90"
    left_response = {"commands": [{"name": "left", "value": 90}]}
    assert Interpreter(parse(left_input)).interpret_all() == left_response
    assert Interpreter(parse(left_alias_input)).interpret_all() == left_response


def test_right():
    right_input = "right 90"
    right_alias_input = "rt 90"
    right_response = {"commands": [{"name": "right", "value": 90}]}
    assert Interpreter(parse(right_input)).interpret_all() == right_response
    assert Interpreter(parse(right_alias_input)).interpret_all() == right_response


def test_showturtle():
    showturtle_input = "showturtle"
    showturtle_alias_input = "st"
    showturtle_response = {"commands": [{"name": "showturtle"}]}
    assert Interpreter(parse(showturtle_input)).interpret_all() == showturtle_response
    assert (
        Interpreter(parse(showturtle_alias_input)).interpret_all()
        == showturtle_response
    )


def test_hideturtle():
    hideturtle_input = "hideturtle"
    hideturtle_alias_input = "ht"
    hideturtle_response = {"commands": [{"name": "hideturtle"}]}
    assert Interpreter(parse(hideturtle_input)).interpret_all() == hideturtle_response
    assert (
        Interpreter(parse(hideturtle_alias_input)).interpret_all()
        == hideturtle_response
    )


def test_penup():
    penup_input = "penup"
    penup_alias_input = "pu"
    penup_response = {"commands": [{"name": "penup"}]}
    assert Interpreter(parse(penup_input)).interpret_all() == penup_response
    assert Interpreter(parse(penup_alias_input)).interpret_all() == penup_response


def test_pendown():
    pendown_input = "pendown"
    pendown_alias_input = "pd"
    pendown_response = {"commands": [{"name": "pendown"}]}
    assert Interpreter(parse(pendown_input)).interpret_all() == pendown_response
    assert Interpreter(parse(pendown_alias_input)).interpret_all() == pendown_response


def test_repeat():
    repeat_input = "repeat 4 [forward 100 right 90]"
    repeat_response = {
        "commands": [
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
        ]
    }
    assert Interpreter(parse(repeat_input)).interpret_all() == repeat_response


def test_if():
    if_true_input = "if true [forward 100]"
    if_true_response = {
        "commands": [
            {"name": "forward", "value": 100},
        ]
    }
    if_false_input = "if false [forward 100]"
    if_false_response = {"commands": []}
    assert Interpreter(parse(if_true_input)).interpret_all() == if_true_response
    assert Interpreter(parse(if_false_input)).interpret_all() == if_false_response


def test_all():
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
        repeat 4 [forward 100 right 90]
        if true [forward 100]
        if false [forward 100]
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
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
            {"name": "right", "value": 90},
            {"name": "forward", "value": 100},
        ]
    }
    assert Interpreter(parse(logo_input)).interpret_all() == logo_response
