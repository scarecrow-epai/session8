import re
import os
import pytest
import inspect
import session8

README_CONTENT_CHECK_FOR = [
    "func_check_docs",
    "func_next_fib",
    "func_add",
    "func_mul",
    "func_div",
    "func_counter",
    "func_counter_user",
]


def test_readme_exists():
    """                                                                                                                                                                      
    Test funtion to check if README exists.                                                                                                                                  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """                                                                                                                                                                      
    Test if README contains atleast 200 words.                                                                                                                               
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session8)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_func_check_docs():
    """
    Test function for Q1. Closure to check if a function has atleast 50 
    characters in its doc strings.
    """

    def test_func1():
        """
        Less than 50 chars.
        """

        return 1

    def test_func2():
        """
        This is more than 50 chars. It is pointless. 
        This docstring serves no purpose other than to 
        exceed 50 characters for this test to work properly.
        """

        return 1

    assert (
        session8.func_check_docs(test_func1)() is False
        and session8.func_check_docs(test_func2)() is True
    )


def test_next_fib():
    """
    Test for question 2. Checks if the next fib number is correct or not.
    """

    fib_list = [0, 1, 1, 2, 3]
    temp = []

    fib_func = session8.func_next_fib(10)
    for i in range(len(fib_list)):
        temp.append(fib_func())

    assert temp == fib_list


def test_end_next_fib():
    """
    Test for question 2. Check if the last number is handled properly by function.
    Next fibonacci number cannot be called for n+1 step if there exist n fibonacci 
    numbers.
    """

    fib_list = [0, 1, 1, 2, 3]

    fib_func = session8.func_next_fib(5)
    for i in range(len(fib_list)):
        fib_func()

    assert fib_func() == "End of Sequence"


def test_func_count():
    """
    Function to count the number of times a function is called.
    """

    global_fn_count = {"func_add": 0, "func_mul": 0, "func_div": 0}

    a = session8.func_counter(session8.func_add)
    m = session8.func_counter(session8.func_mul)
    d = session8.func_counter(session8.func_div)

    a(1, 2)
    m(1, 2)
    m(5, 2)
    d(1, 2)
    d(5, 2)
    d(10, 2)

    assert global_fn_count == {"func_add": 0, "func_mul": 0, "func_div": 0}


def test_func_count_user():
    """
    Function to count the number of times a function is called. A dictionary 
    is passed in. 
    """
    abc_dict = {"func_add": 0, "func_mul": 0, "func_div": 0}
    def_dict = {"func_add": 0, "func_mul": 0, "func_div": 0}

    a_abc = session8.func_counter_user(session8.func_add, abc_dict)
    m_abc = session8.func_counter_user(session8.func_mul, abc_dict)
    d_abc = session8.func_counter_user(session8.func_div, abc_dict)

    a_def = session8.func_counter_user(session8.func_add, def_dict)
    m_def = session8.func_counter_user(session8.func_mul, def_dict)
    d_def = session8.func_counter_user(session8.func_div, def_dict)

    a_abc(1, 2)
    m_abc(1, 2)
    m_def(5, 2)
    d_abc(1, 2)
    d_abc(5, 2)
    d_def(10, 2)

    assert abc_dict == {"func_add": 1, "func_mul": 1, "func_div": 2} and def_dict == {
        "func_add": 0,
        "func_mul": 1,
        "func_div": 1,
    }
