from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions, validate_and_filter

def main():
    raw_lines = read_sales_data("data/sales_data.txt")
    transactions = parse_transactions(raw_lines)

    valid_transactions, invalid_count, summary = validate_and_filter(transactions)

    print("Total input records:", summary['total_input'])
    print("Invalid records:", summary['invalid'])
    print("Final valid records:", summary['final_count'])

if __name__ == "__main__":
    main()
