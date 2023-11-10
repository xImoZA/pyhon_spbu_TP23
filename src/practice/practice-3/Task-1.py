from math import gcd


def get_fractions(max_denominator):
    dict_output_fractions = {}
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                dict_output_fractions[
                    numerator / denominator
                ] = f"{numerator}/{denominator}"
    return [
        dict_output_fractions[fractions]
        for fractions in sorted(dict_output_fractions.keys())
    ]


if __name__ == "__main__":
    n = int(input("To output all irreducible fractions, enter n: "))
    print(f'Fractions: {" ".join(get_fractions(n))}')
