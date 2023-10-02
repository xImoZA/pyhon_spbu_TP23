import os


def delete_fragment(start, end, dna):
    start_index = dna.find(start)
    end_index = dna.find(end, start_index + len(start)) + len(end)

    return dna[:start_index] + dna[end_index:]


def insert_fragment(start, fragment, dna):
    start_index = dna.find(start) + len(start)

    return dna[:start_index] + fragment + dna[start_index:]


def replace_fragment(template, fragment, dna):
    return dna.replace(template, fragment, 1)


def read_file(read_name, output_name):
    with open(read_name, "r") as src_file, open(output_name, "w") as dst_file:
        m = int(src_file.readline())
        genotype = src_file.readline()

        n = int(src_file.readline())
        for experiment in range(1, n + 1):
            operation, parameter_1, parameter_2 = src_file.readline().split()

            if operation == "DELETE":
                genotype = delete_fragment(parameter_1, parameter_2, genotype)

            elif operation == "INSERT":
                genotype = insert_fragment(parameter_1, parameter_2, genotype)

            elif operation == "REPLACE":
                genotype = replace_fragment(parameter_1, parameter_2, genotype)

            dst_file.write(f"After {experiment} experiment: {genotype}")


if __name__ == "__main__":
    name_scr_file = input("Enter the name of the file to read: ")
    while os.path.exists(name_scr_file) is False:
        name_scr_file = input("There is no such file in the directory. Try again: ")

    name_dst_file = input("Enter the name of the file to output the result: ")
    if os.path.exists(name_dst_file) is False:
        check_name = input(
            "There is no such file in the directory. Do you want to create a new file? (Y/N): "
        )

        if check_name == "N":
            while os.path.exists(name_dst_file) is False:
                name_dst_file = input(
                    "Enter the name of the file to output the result: "
                )

    read_file(name_scr_file, name_dst_file)
    print(f"The results of the experiments are derived in {name_dst_file}")
