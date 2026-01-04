def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues

    Returns: list of raw lines (strings)
    """

    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()

                cleaned_lines = []

                for line in lines:
                    line = line.strip()

                    # Skip empty lines
                    if line == "":
                        continue

                    # Skip header row
                    if line.startswith("TransactionID"):
                        continue

                    cleaned_lines.append(line)

                return cleaned_lines

        except UnicodeDecodeError:
            continue

        except FileNotFoundError:
            print("Error: File not found:", filename)
            return []

    print("Error: Unable to read file with supported encodings")
    return []
