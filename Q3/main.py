# Q3/main.py

from Q3.utils.file_handler import read_sales_data
from Q3.utils.data_processor import (
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products
)

from Q2.utils.data_processor import (
    parse_transactions,
    validate_and_filter
)

# -----------------------------
# MAIN FLOW
# -----------------------------
raw = read_sales_data("Q3/data/sales_data.txt")
parsed = parse_transactions(raw)
valid, _, _ = validate_and_filter(parsed)

print("Total Revenue:", calculate_total_revenue(valid))
print("Region-wise Sales:", region_wise_sales(valid))
print("Top Products:", top_selling_products(valid))
print("Customer Analysis:", customer_analysis(valid))
print("Daily Sales Trend:", daily_sales_trend(valid))
print("Peak Sales Day:", find_peak_sales_day(valid))
print("Low Performing Products:", low_performing_products(valid))
