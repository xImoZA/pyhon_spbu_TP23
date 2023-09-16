import csv


def count_word(file):
    dict_with_count_words = {}

    with open(file, 'r') as src_file:
        for line in src_file:
            for word in list(map(str, line.split())):
                dict_with_count_words[word.lower()] = dict_with_count_words.get(word.lower(), 0) + 1

    return dict_with_count_words


def write_word(file, dict_words):
    list_with_word = [[key, dict_words[key]] for key in dict_words.keys()]
    with open(file, 'w') as dst_file:
        word_writer = csv.writer(dst_file)
        word_writer.writerow(['Word', 'Count'])
        word_writer.writerows(list_with_word)


if __name__ == '__main__':
    scr_file = input('To analyze the text, enter the name of the text file: ')
    dst_file = input('Enter the name of the file to save the result: ')

    write_word(dst_file, count_word(scr_file))

    print(f'The result is written to a file {dst_file}')
