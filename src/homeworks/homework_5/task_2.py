def encode(dna: str) -> str:
    if dna == "":
        raise ValueError("You entered an empty string")

    elif not dna.isalpha():
        raise ValueError("DNA must contain only letters")

    encode_dna = ""
    counter = 1
    for i in range(1, len(dna)):
        last_nucleotide = dna[i - 1]
        nucleotide = dna[i]

        if last_nucleotide == nucleotide:
            counter += 1

        else:
            encode_dna += f"{last_nucleotide}{counter}"
            counter = 1

    encode_dna += f"{dna[-1]}{counter}"

    return encode_dna


def decode(dna: str) -> str:
    if is_input_correct(dna):
        nucleotides_list = []
        nucleotide = dna[0]

        for i in range(1, len(dna)):
            element = dna[i]

            if element.isdigit():
                nucleotide += element

            else:
                nucleotides_list.append(nucleotide)
                nucleotide = element

        nucleotides_list.append(nucleotide)

        return "".join(map(lambda gen: gen[0] * int(gen[1:]), nucleotides_list))


def is_input_correct(dna: str) -> bool:
    if dna == "":
        raise ValueError("You entered an empty string")

    if dna.isalpha() or dna.isdigit() or not dna.isalnum():
        raise ValueError("Encode DNA should consist only of letters and numbers")

    elif dna[-1].isalpha():
        raise ValueError("Encode DNA can't end with a letter")

    elif dna[0].isdigit():
        raise ValueError("Encode DNA can't start with a digit")

    for i in range(1, len(dna)):
        if dna[i - 1].isalpha() and dna[i].isalpha():
            raise ValueError("Encode DNA can't have several letters successively")

    return True


def main() -> None:
    dna = input("Enter DNA: ").lower()
    function = input("Enter function:\n 1) Encode\n 2) Decode\nSelected function: ")
    if function == "1":
        try:
            print(f"Encode DNA: {encode(dna)}")
        except ValueError as error:
            print(error)
    elif function == "2":
        try:
            print(f"Decode DNA: {decode(dna)}")
        except ValueError as error:
            print(error)
    else:
        print("Incorrect input. It can only be 1 or 2")


if __name__ == "__main__":
    main()
