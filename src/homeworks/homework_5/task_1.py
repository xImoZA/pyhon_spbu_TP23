def get_unicode(sign):
    unicode = hex(ord(sign))[2:].upper()
    return f"U+{unicode.rjust(4, '0')}"


def get_utf16(sign):
    unicode_number = ord(sign)

    if unicode_number < 65535:
        binary_char = bin(unicode_number)[2:].rjust(16, "0")
        return [binary_char[:8], binary_char[8:]]

    unicode_number -= 65536
    binary_char = bin(unicode_number)[2:].rjust(20, "0")

    higher_bits = bin(int(binary_char[:10], 2) + 55296)[2:]
    lower_bits = bin(int(binary_char[10:], 2) + 56320)[2:]

    return [higher_bits[:8], higher_bits[8:], lower_bits[:8], lower_bits[8:]]


def main():
    string = input("Enter a string: ")
    print("UTF-16 encoding:")
    for symbol in string:
        unicode = get_unicode(symbol)
        utf16 = get_utf16(symbol)

        print(f"{symbol} \t {unicode} \t {' '.join(utf16)}", end="\n")


if __name__ == "__main__":
    main()
