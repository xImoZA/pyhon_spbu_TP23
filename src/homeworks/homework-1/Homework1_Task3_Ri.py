import sys


def wc(parameter, file):
    with open(file) as open_file:
        if parameter == '-c':
            count_byte = 0
            for line in open_file:
                count_byte += len(line.encode("utf-8"))
            return count_byte

        elif parameter == '-m':
            count_symbols = 0
            for line in open_file:
                count_symbols += len(line)
            return count_symbols

        elif parameter == '-l':
            count_line = 0
            for _ in open_file:
                count_line += 1
            return count_line

        elif parameter == '-w':
            count_word = 0
            for line in open_file:
                count_word += len(line.split())
            return count_word


def head(option, number, file):
    with open(file) as open_file:
        if option == '-n':
            return ''.join([open_file.readline() for i in range(number)])

        output_text = ''
        for line in open_file:
            for symbol in line:
                output_text += symbol
                if len(output_text.encode("utf-8")) == number:
                    return output_text

                elif len(output_text.encode("utf-8")) > number:
                    return output_text


def tail(option, number, file):
    with open(file) as open_file:
        if option == '-n':
            open_file = open_file.readlines()

            return ''.join(open_file[len(open_file) - number: len(open_file)])

        open_file = open_file.read()

        for symbols in range(len(open_file)):
            if len(open_file[len(open_file) - symbols:len(open_file)].encode("utf-8")) == number:
                return open_file[len(open_file) - symbols:len(open_file)]

            elif len(open_file[len(open_file) - symbols:len(open_file)].encode("utf-8")) > number:
                return open_file[len(open_file) - symbols - 1:len(open_file)]


if __name__ == '__main__':
    operation = sys.argv[1]

    if operation == 'wc':
        argument, input_file = sys.argv[2:]
        print(f'{operation} {argument} {input_file}: {wc(argument, input_file)}')

    else:
        argument, x, input_file = sys.argv[2:]

        if operation == 'head':
            print(f'{operation} {argument} {input_file}: \n{head(argument, int(x), input_file)}')

        elif operation == 'tail':
            print(f'{operation} {argument} {input_file}: \n{tail(argument, int(x), input_file)}')
