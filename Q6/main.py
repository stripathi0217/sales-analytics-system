from Q6.utils.file_handler import read_sales_data, save_enriched_data
from Q6.utils.data_processor import (
    parse_transactions,
    validate_and_filter,
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products
)
from Q6.utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data
)
from Q6.utils.report_generator import generate_sales_report


def main():
    print("=" * 40)
    print("       SALES ANALYTICS SYSTEM")
    print("=" * 40)

    try:
        # 1. Read data
        print("\n[1/10] Reading sales data...")
        raw_lines = read_sales_data("Q6/data/sales_data.txt")
        print(f"✓ Successfully read {len(raw_lines)} transactions")

        # 2. Parse data
        print("\n[2/10] Parsing and cleaning data...")
        transactions = parse_transactions(raw_lines)
        print(f"✓ Parsed {len(transactions)} records")

        # 3. Show filter options
        print("\n[3/10] Filter Options Available:")
        regions = sorted(set(tx['Region'] for tx in transactions))
        amounts = [tx['Quantity'] * tx['UnitPrice'] for tx in transactions]

        print("Regions:", ", ".join(regions))
        print(f"Amount Range: ₹{min(amounts)} - ₹{max(amounts)}")

        choice = input("Do you want to filter data? (y/n): ").lower()

        filter_region = None
        min_amount = None
        max_amount = None

        if choice == "y":
            filter_region = input("Enter region (or press Enter to skip): ").strip() or None

            min_val = input("Enter minimum amount (or press Enter to skip): ").strip()
            max_val = input("Enter maximum amount (or press Enter to skip): ").strip()

            min_amount = float(min_val) if min_val else None
            max_amount = float(max_val) if max_val else None

        # 4. Validate & filter
        print("\n[4/10] Validating transactions...")
        valid_transactions, invalid_count, _ = validate_and_filter(
            transactions,
            region=filter_region,
            min_amount=min_amount,
            max_amount=max_amount
        )
        print(f"✓ Valid: {len(valid_transactions)} | Invalid: {invalid_count}")

        # 🛑 IMPORTANT SAFETY CHECK
        if not valid_transactions:
            print("\n⚠️ No transactions match the selected filters.")
            print("Please try again with different filter values.")
            print("\nProcess stopped safely.")
            return


        # 5. Analysis
        print("\n[5/10] Analyzing sales data...")
        total_revenue = calculate_total_revenue(valid_transactions)
        region_sales = region_wise_sales(valid_transactions)
        top_products = top_selling_products(valid_transactions)
        customers = customer_analysis(valid_transactions)
        daily_trend = daily_sales_trend(valid_transactions)
        peak_day = find_peak_sales_day(valid_transactions)
        low_products = low_performing_products(valid_transactions)
        print("✓ Analysis complete")

        # 6. API fetch
        print("\n[6/10] Fetching product data from API...")
        api_products = fetch_all_products()
        product_mapping = create_product_mapping(api_products)
        print(f"✓ Fetched {len(api_products)} products")

        # 7. Enrich data
        print("\n[7/10] Enriching sales data...")
        enriched_transactions = enrich_sales_data(valid_transactions, product_mapping)

        enriched_count = sum(1 for tx in enriched_transactions if tx["API_Match"])
        print(f"✓ Enriched {enriched_count}/{len(valid_transactions)} transactions")

        # 8. Save enriched data
        print("\n[8/10] Saving enriched data...")
        save_enriched_data(enriched_transactions, "Q6/data/enriched_sales_data.txt")
        print("✓ Saved to: Q6/data/enriched_sales_data.txt")

        # 9. Generate report
        print("\n[9/10] Generating report...")
        generate_sales_report(
            valid_transactions,
            enriched_transactions,
            output_file="Q6/output/sales_report.txt"
        )
        print("✓ Report saved to: Q6/output/sales_report.txt")

        # 10. Done
        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        print("Message:", e)
        print("Please check input files and try again.")


if __name__ == "__main__":
    main()
