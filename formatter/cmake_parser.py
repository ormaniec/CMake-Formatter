def read_next_command(file_path):
    empty_read = True
    concat_val = []
    result = []
    file = open(file_path)
    for line in file:
        if "(" in line and empty_read:
            empty_read = False
            if concat_val:
                result.append(concat_val)
                concat_val = []

        line.splitlines()
        concat_val.append(line)

        if ")" in line:
            result.append(concat_val)
            concat_val = []
            empty_read = True

    print(result)
