import tool.test_module as tm

def test_answer():
    assert tm.test_function_sum(1,2) == 3, f"function passed the test"