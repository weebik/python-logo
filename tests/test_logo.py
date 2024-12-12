from python_logo import run


def test_showturtle():
    showturtle_input = "showturtle"
    showturtle_alias_input = "st"
    showturtle_response = [{"name": "showturtle"}]
    assert list(run(showturtle_input)) == showturtle_response
    assert list(run(showturtle_alias_input)) == showturtle_response


def test_hideturtle():
    hideturtle_input = "hideturtle"
    hideturtle_alias_input = "ht"
    hideturtle_response = [{"name": "hideturtle"}]
    assert list(run(hideturtle_input)) == hideturtle_response
    assert list(run(hideturtle_alias_input)) == hideturtle_response


def test_penup():
    penup_input = "penup"
    penup_alias_input = "pu"
    penup_response = [{"name": "penup"}]
    assert list(run(penup_input)) == penup_response
    assert list(run(penup_alias_input)) == penup_response


def test_pendown():
    pendown_input = "pendown"
    pendown_alias_input = "pd"
    pendown_response = [{"name": "pendown"}]
    assert list(run(pendown_input)) == pendown_response
    assert list(run(pendown_alias_input)) == pendown_response


def test_forward():
    forward_input = "forward 100"
    forward_alias_input = "fd 100"
    forward_response = [{"name": "forward", "value": 100.0}]
    assert list(run(forward_input)) == forward_response
    assert list(run(forward_alias_input)) == forward_response


def test_backward():
    backward_input = "backward 100"
    backward_alias_input = "bk 100"
    backward_response = [{"name": "backward", "value": 100.0}]
    assert list(run(backward_input)) == backward_response
    assert list(run(backward_alias_input)) == backward_response


def test_left():
    left_input = "left 90"
    left_alias_input = "lt 90"
    left_response = [{"name": "left", "value": 90.0}]
    assert list(run(left_input)) == left_response
    assert list(run(left_alias_input)) == left_response


def test_right():
    right_input = "right 90"
    right_alias_input = "rt 90"
    right_response = [{"name": "right", "value": 90.0}]
    assert list(run(right_input)) == right_response
    assert list(run(right_alias_input)) == right_response


def test_repeat():
    repeat_input = "repeat 4 [forward 100 right 90]"
    repeat_response = [
        {"name": "forward", "value": 100.0},
        {"name": "right", "value": 90.0},
        {"name": "forward", "value": 100.0},
        {"name": "right", "value": 90.0},
        {"name": "forward", "value": 100.0},
        {"name": "right", "value": 90.0},
        {"name": "forward", "value": 100.0},
        {"name": "right", "value": 90.0},
    ]
    assert list(run(repeat_input)) == repeat_response


def test_if():
    if_true_input = "if true [forward 100]"
    if_true_response = [{"name": "forward", "value": 100.0}]
    if_false_input = "if false [forward 100]"
    if_false_response = []
    assert list(run(if_true_input)) == if_true_response
    assert list(run(if_false_input)) == if_false_response


def test_else():
    else_input = "if false [forward 100] else [right 90]"
    else_response = [{"name": "right", "value": 90.0}]
    assert list(run(else_input)) == else_response


def test_make():
    variables_input = "make test-var 100 forward :test-var"
    variables_response = [{"name": "forward", "value": 100.0}]
    assert list(run(variables_input)) == variables_response


def test_expr():
    expr_input = """
    forward 20 + 20 + 20
    forward 20 * 20 + 20
    forward 20 * (20 + 20)
    forward 20 * (20 + 20) / 2
    forward 20 * (20 + 20) / 2 - 100
    forward 10 / 4
    make test_var -2 ^ (3 + 2)
    forward :test_var
    repeat 2.3 [forward 100.5]
    """
    expr_response = [
        {"name": "forward", "value": 60.0},
        {"name": "forward", "value": 420.0},
        {"name": "forward", "value": 800.0},
        {"name": "forward", "value": 400.0},
        {"name": "forward", "value": 300.0},
        {"name": "forward", "value": 2.5},
        {"name": "forward", "value": -32.0},
        {"name": "forward", "value": 100.5},
        {"name": "forward", "value": 100.5},
    ]
    assert list(run(expr_input)) == expr_response
