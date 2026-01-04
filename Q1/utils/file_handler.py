def read_sales_file(file_path):
    records = []

    # encoding='latin-1' handles non-UTF-8 text
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line == "":
                continue
            records.append(line)

    return records
