from lab_02.exercise import example_function


def test_example_function_1():

    assert example_function(2, 3) == 6
    assert example_function(4, 2) == 8
