def curry_explicit(function, arity):
    if arity < 0:
        exit("Uncorrected arity")

    elif arity == 0:
        return function()

    def get_args(args):
        if len(args) > arity:
            exit(
                "Uncorrected input: The number of arguments does not correspond to arity"
            )

        if len(args) == arity:
            return function(*args)

        def get_one_arg(*new_arg):
            return get_args([*args, *new_arg])

        return get_one_arg

    return get_args([])


def uncurry_explicit(function, arity):
    if arity < 0:
        exit("Uncorrected arity")

    elif arity == 0:
        return function()

    def get_args(*args):
        if len(args) != arity:
            exit(
                "Uncorrected input: The number of arguments does not correspond to arity"
            )

        output_function = function(args[0])

        for i in range(1, len(args)):
            output_function = output_function(args[i])

        return output_function

    return get_args


def main():
    f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    g2 = uncurry_explicit(f2, 3)
    print(f2(123)(456)(562))  # <123,456,562>
    print(g2(123, 456, 562))  # <123,456,562>


if __name__ == "__main__":
    main()
