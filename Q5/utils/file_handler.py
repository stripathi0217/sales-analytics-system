import os


def read_sales_data(filename):
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as file:
                lines = file.readlines()

                cleaned = []
                for line in lines:
                    line = line.strip()
                    if line == "" or line.startswith("TransactionID"):
                        continue
                    cleaned.append(line)

                return cleaned

        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print("File not found:", filename)
            return []

    print("Unable to read file")
    return []


def save_enriched_data(enriched_transactions,
                       filename="Q4/data/enriched_sales_data.txt"):
    """
    Saves enriched transactions to file
    """

    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    header = (
        "TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|"
        "CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match\n"
    )

    with open(filename, "w", encoding="utf-8") as file:
        file.write(header)

        for tx in enriched_transactions:
            row = (
                f"{tx['TransactionID']}|{tx['Date']}|{tx['ProductID']}|"
                f"{tx['ProductName']}|{tx['Quantity']}|{tx['UnitPrice']}|"
                f"{tx['CustomerID']}|{tx['Region']}|"
                f"{tx['API_Category']}|{tx['API_Brand']}|"
                f"{tx['API_Rating']}|{tx['API_Match']}\n"
            )
            file.write(row)

    print("Enriched data saved successfully")
