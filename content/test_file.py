
import pytest
from functions_file import add_numbers, multiply_numbers
""" 
def test_add_numbers():
    # Use test values directly inside the test
    a = 1
    b = 2
    print(f"Testing with a = {a}, b = {b}")  # This will be shown with pytest -s
    result = add_numbers(a, b)
    assert result == a + b
 """
# shift + option + a to comment out multiple lines

# You can add an assertion message to help understand the test failure
""" 
def test_add_numbers():
    a, b, expected = 3, 2, 4  # This will fail because 1 + 2 is not 4
    result = add_numbers(a, b)
    assert result == expected, f"Expected {expected} but got {result} for inputs {a} and {b}"

 """

# You can create test casess as a list of tuples
""" 
def test_add_numbers():
    # A list of test cases (a, b, expected_result)
    test_cases = [
        (1, 2, 3),
        (5, 5, 10),
        (10, -10, 0),
        (100, 200, 400)
    ]
    
    for a, b, expected in test_cases:
        result = add_numbers(a, b)
        print(f"Testing four cases with a = {a}, b = {b}, expected = {expected}, result = {result}")  # For debugging purposes
        assert result == expected 
 """

# Or you can create a fixture to provide test cases to be used in multiple tests

""" 
@pytest.fixture
def number_test_cases():
    # A list of tuples with test cases (a, b, expected_result)
    return [
        (1, 2, 3, 2),
        (5, 5, 10, 25),
        (10, -10, 0, -100),
        (100, 200, 300, 20000)
    ]

# Use the fixture in the test function
def test_add_numbers(number_test_cases):
    # Loop through test cases provided by the fixture
    for a, b, add_expected, not_used in number_test_cases:
        result = add_numbers(a, b)
        print(f"Testing with a = {a}, b = {b}, expected = {add_expected}, result = {result}")
        assert result == add_expected

def test_multiply_numbers(number_test_cases):
    # Loop through test cases provided by the fixture
    for a, b, expected, mult_expected in number_test_cases:
        result = multiply_numbers(a, b)
        print(f"Testing with a = {a}, b = {b}, multiplied expected = {mult_expected}, result = {result}")
        assert result == mult_expected

 """
# Or you can paramertize it rather than creating a function
""" 
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -10, 0),
    (100, 200, 300)
])

def test_add_numbers(a, b, expected):
    result = add_numbers(a, b)
    assert result == expected
 """

# If you don't like commenting out, you can skip too

@pytest.mark.skip(reason="Skipping for some useful reason like not connected to API")
def test_add_external_dependency():
    # This test will be skipped
    assert 1 + 1 == 2



