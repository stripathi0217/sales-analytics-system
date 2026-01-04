from utils.file_handler import read_sales_file
from utils.data_processor import clean_sales_data

FILE_PATH = "data/sales_data.txt"

def main():
    raw_records = read_sales_file(FILE_PATH)

    total_records = len(raw_records)

    valid_records, invalid_records = clean_sales_data(raw_records)

    print("Total records parsed:", total_records)
    print("Invalid records removed:", invalid_records)
    print("Valid records after cleaning:", len(valid_records))

if __name__ == "__main__":
    main()
