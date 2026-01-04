def read_sales_data(filename):
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()

                cleaned_lines = []

                for line in lines:
                    line = line.strip()

                    if line == "":
                        continue

                    if line.startswith("TransactionID"):
                        continue

                    cleaned_lines.append(line)

                return cleaned_lines

        except UnicodeDecodeError:
            continue

        except FileNotFoundError:
            print("File not found:", filename)
            return []

    print("Unable to read file")
    return []
