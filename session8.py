def func_check_docs(fn: "function") -> "Boolean":
    """
    Closure to check if an input function has atleast 50 chars
    in it's docstring.
    """
    char_limit = 50

    def doc_char_checker():
        if len(fn.__doc__) >= char_limit:
            return True
        else:
            return False

        return is_fifty_chars

    return doc_char_checker


def func_next_fib(seq_len: "int") -> "next fib number":
    """
    Closure to output the next fib number after it is generated
    based on the input.
    """
    curr_fib_idx = -1
    fib_list = []

    def create_fib_seq(n):
        a = 0
        b = 1

        nonlocal fib_list
        fib_list = [0, 1]

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            fib_list.append(c)

    create_fib_seq(seq_len)

    def update_fib():
        nonlocal curr_fib_idx
        if curr_fib_idx == len(fib_list) - 1:
            return "End of Sequence"
        curr_fib_idx += 1

        return fib_list[curr_fib_idx]

    return update_fib


def func_add(a: int, b: int) -> int:
    """
    Function to add 2 numbers.
    """
    return a + b


def func_mul(a: int, b: int) -> int:
    """
    Function to multiple 2 numbers.
    """
    return a * b


def func_div(a: int, b: int) -> float:
    """
    Function to divide 2 numbers.
    """
    return a / b


global_fn_count = {"func_add": 0, "func_mul": 0, "func_div": 0}


def func_counter(fn: "function") -> "number of times called":
    """
    Function counter. Counts the number of times a function has been called. 
    The count is updated in the global dictionary.
    """

    def update_count(*args, **kwargs):
        global global_fn_count
        global_fn_count[fn.__name__] += 1

        return fn(*args, **kwargs)

    return update_count


def func_counter_user(fn: "function", dct: "dict") -> "number of times called":
    """
    Function counter per user. Counts the number of times a function has been called. 
    The count is updated in the global dictionary which is passed to the function..
    """

    def update_count(*args, **kwargs):
        nonlocal dct
        dct[fn.__name__] += 1

        return fn(*args, **kwargs)

    return update_count


aks_dict = {"func_add": 0, "func_mul": 0, "func_div": 0}

a = func_counter_user(func_add, aks_dict)
m = func_counter_user(func_mul, aks_dict)
d = func_counter_user(func_div, aks_dict)

print(a(1, 2))

print(m(1, 2))
print(m(5, 2))

print(d(1, 2))
print(d(5, 2))
print(d(10, 2))


print(global_fn_count)
print(aks_dict)
