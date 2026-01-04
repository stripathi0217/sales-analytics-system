from Q5.utils.file_handler import read_sales_data
from Q5.utils.data_processor import parse_transactions, validate_and_filter
from Q5.utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data
)
from Q5.utils.report_generator import generate_sales_report

def main():
    # Step 1: Read raw sales data
    raw_lines = read_sales_data("Q5/data/sales_data.txt")

    # Step 2: Parse raw data
    transactions = parse_transactions(raw_lines)

    # Step 3: Validate transactions
    valid_transactions, _, _ = validate_and_filter(transactions)

    # Step 4: Fetch products from API
    api_products = fetch_all_products()
    product_mapping = create_product_mapping(api_products)

    # Step 5: Enrich sales data
    enriched_transactions = enrich_sales_data(valid_transactions, product_mapping)

    # Step 6: Generate report
    generate_sales_report(
        valid_transactions,
        enriched_transactions,
        output_file="Q5/output/sales_report.txt"
    )

if __name__ == "__main__":
    main()
