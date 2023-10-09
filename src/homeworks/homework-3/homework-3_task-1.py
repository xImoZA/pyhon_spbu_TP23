def curry_explicit(function, arity):
    if arity < 0:
        print("Uncorrected arity")
        return False

    elif arity == 0:
        return function

    def get_args(args):
        if len(args) == arity:
            return function(*args)

        def get_one_arg(arg):
            return get_args([*args, arg])

        return get_one_arg

    return get_args([])


def uncurry_explicit(function, arity):
    if arity < 0:
        print("Uncorrected arity")
        return False

    elif arity == 0:
        return function

    def get_args(*args):
        if len(args) != arity:
            print("Error: The number of arguments does not correspond to arity")
            return False

    # у меня совершенно нет идей, помогите пожалуйста
    # я не понимаю как аргументы поместить в скобки и эти скобки подряд в функцию(

    return get_args


if __name__ == "__main__":
    f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    # g2 = uncurry_explicit(f2, 3)
    print(f2(123)(456)(562)(123))  # <123,456,562>
    # print(g2(123, 456, 562))  # <123,456,562>
