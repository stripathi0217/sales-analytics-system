from datetime import datetime
from collections import defaultdict

def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive formatted text sales report
    """

    # -----------------------------
    # BASIC CALCULATIONS
    # -----------------------------
    total_transactions = len(transactions)
    total_revenue = sum(tx['Quantity'] * tx['UnitPrice'] for tx in transactions)
    avg_order_value = total_revenue / total_transactions if total_transactions else 0

    dates = sorted(tx['Date'] for tx in transactions)
    start_date = dates[0]
    end_date = dates[-1]

    # -----------------------------
    # REGION-WISE PERFORMANCE
    # -----------------------------
    region_data = defaultdict(lambda: {'sales': 0, 'count': 0})

    for tx in transactions:
        amount = tx['Quantity'] * tx['UnitPrice']
        region_data[tx['Region']]['sales'] += amount
        region_data[tx['Region']]['count'] += 1

    region_summary = []
    for region, data in region_data.items():
        percent = (data['sales'] / total_revenue) * 100
        region_summary.append((region, data['sales'], percent, data['count']))

    region_summary.sort(key=lambda x: x[1], reverse=True)

    # -----------------------------
    # TOP PRODUCTS
    # -----------------------------
    product_data = defaultdict(lambda: {'qty': 0, 'revenue': 0})

    for tx in transactions:
        product_data[tx['ProductName']]['qty'] += tx['Quantity']
        product_data[tx['ProductName']]['revenue'] += tx['Quantity'] * tx['UnitPrice']

    top_products = sorted(
        product_data.items(),
        key=lambda x: x[1]['qty'],
        reverse=True
    )[:5]

    # -----------------------------
    # TOP CUSTOMERS
    # -----------------------------
    customer_data = defaultdict(lambda: {'spent': 0, 'orders': 0})

    for tx in transactions:
        amount = tx['Quantity'] * tx['UnitPrice']
        customer_data[tx['CustomerID']]['spent'] += amount
        customer_data[tx['CustomerID']]['orders'] += 1

    top_customers = sorted(
        customer_data.items(),
        key=lambda x: x[1]['spent'],
        reverse=True
    )[:5]

    # -----------------------------
    # DAILY SALES TREND
    # -----------------------------
    daily_data = defaultdict(lambda: {'revenue': 0, 'count': 0, 'customers': set()})

    for tx in transactions:
        amount = tx['Quantity'] * tx['UnitPrice']
        daily_data[tx['Date']]['revenue'] += amount
        daily_data[tx['Date']]['count'] += 1
        daily_data[tx['Date']]['customers'].add(tx['CustomerID'])

    # -----------------------------
    # API ENRICHMENT SUMMARY
    # -----------------------------
    enriched_count = sum(1 for tx in enriched_transactions if tx.get('API_Match'))
    enrichment_rate = (enriched_count / len(enriched_transactions)) * 100 if enriched_transactions else 0

    failed_products = list({
        tx['ProductName'] for tx in enriched_transactions if not tx.get('API_Match')
    })

    # -----------------------------
    # WRITE REPORT
    # -----------------------------
    with open(output_file, 'w', encoding='utf-8') as file:

        file.write("=" * 50 + "\n")
        file.write("        SALES ANALYTICS REPORT\n")
        file.write(f"Generated: {datetime.now()}\n")
        file.write(f"Records Processed: {total_transactions}\n")
        file.write("=" * 50 + "\n\n")

        file.write("OVERALL SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Revenue:        ₹{total_revenue:,.2f}\n")
        file.write(f"Total Transactions:   {total_transactions}\n")
        file.write(f"Average Order Value:  ₹{avg_order_value:,.2f}\n")
        file.write(f"Date Range:           {start_date} to {end_date}\n\n")

        file.write("REGION-WISE PERFORMANCE\n")
        file.write("-" * 50 + "\n")
        file.write("Region     Sales        % Total   Transactions\n")
        for r, sales, pct, cnt in region_summary:
            file.write(f"{r:<10} ₹{sales:,.0f}   {pct:6.2f}%      {cnt}\n")

        file.write("\nTOP 5 PRODUCTS\n")
        file.write("-" * 50 + "\n")
        for i, (name, data) in enumerate(top_products, 1):
            file.write(f"{i}. {name} | Qty: {data['qty']} | Revenue: ₹{data['revenue']:,.2f}\n")

        file.write("\nTOP 5 CUSTOMERS\n")
        file.write("-" * 50 + "\n")
        for i, (cid, data) in enumerate(top_customers, 1):
            file.write(f"{i}. {cid} | Spent: ₹{data['spent']:,.2f} | Orders: {data['orders']}\n")

        file.write("\nDAILY SALES TREND\n")
        file.write("-" * 50 + "\n")
        for date, data in sorted(daily_data.items()):
            file.write(
                f"{date} | Revenue: ₹{data['revenue']:,.2f} | "
                f"Txns: {data['count']} | "
                f"Customers: {len(data['customers'])}\n"
            )

        file.write("\nAPI ENRICHMENT SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(f"Products Enriched: {enriched_count}\n")
        file.write(f"Success Rate: {enrichment_rate:.2f}%\n")
        file.write("Products Not Enriched:\n")
        for p in failed_products:
            file.write(f"- {p}\n")

    print("Sales report generated successfully.")
