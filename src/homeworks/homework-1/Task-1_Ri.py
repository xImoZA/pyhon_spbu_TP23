def polynomial(x):
    square_of_x = x * x
    return (square_of_x + 1) * (square_of_x + x) + 1


if __name__ == "__main__":
    input_x = int(input("Calculating x^4+x^3+x^2+x+1, enter x:"))
    print(f"{input_x}^4+{input_x}^3+{input_x}^2+{input_x}+1={polynomial(input_x)}")
