def calculate_total_revenue(transactions):
    total = 0.0
    for tx in transactions:
        total += tx['Quantity'] * tx['UnitPrice']
    return total

def region_wise_sales(transactions):
    region_data = {}
    total_revenue = calculate_total_revenue(transactions)

    for tx in transactions:
        region = tx['Region']
        revenue = tx['Quantity'] * tx['UnitPrice']

        if region not in region_data:
            region_data[region] = {
                'total_sales': 0.0,
                'transaction_count': 0
            }

        region_data[region]['total_sales'] += revenue
        region_data[region]['transaction_count'] += 1

    for region in region_data:
        region_data[region]['percentage'] = round(
            (region_data[region]['total_sales'] / total_revenue) * 100, 2
        )

    return dict(sorted(
        region_data.items(),
        key=lambda x: x[1]['total_sales'],
        reverse=True
    ))

def top_selling_products(transactions, n=5):
    product_data = {}

    for tx in transactions:
        product = tx['ProductName']
        quantity = tx['Quantity']
        revenue = quantity * tx['UnitPrice']

        if product not in product_data:
            product_data[product] = [0, 0.0]

        product_data[product][0] += quantity
        product_data[product][1] += revenue

    product_list = [
        (product, data[0], data[1])
        for product, data in product_data.items()
    ]

    product_list.sort(key=lambda x: x[1], reverse=True)
    return product_list[:n]
def customer_analysis(transactions):
    customers = {}

    for tx in transactions:
        cust = tx['CustomerID']
        revenue = tx['Quantity'] * tx['UnitPrice']

        if cust not in customers:
            customers[cust] = {
                'total_spent': 0.0,
                'purchase_count': 0,
                'products': set()
            }

        customers[cust]['total_spent'] += revenue
        customers[cust]['purchase_count'] += 1
        customers[cust]['products'].add(tx['ProductName'])

    for cust in customers:
        customers[cust]['avg_order_value'] = round(
            customers[cust]['total_spent'] / customers[cust]['purchase_count'], 2
        )
        customers[cust]['products_bought'] = list(customers[cust]['products'])
        del customers[cust]['products']

    return dict(sorted(
        customers.items(),
        key=lambda x: x[1]['total_spent'],
        reverse=True
    ))

def daily_sales_trend(transactions):
    daily = {}

    for tx in transactions:
        date = tx['Date']
        revenue = tx['Quantity'] * tx['UnitPrice']

        if date not in daily:
            daily[date] = {
                'revenue': 0.0,
                'transaction_count': 0,
                'customers': set()
            }

        daily[date]['revenue'] += revenue
        daily[date]['transaction_count'] += 1
        daily[date]['customers'].add(tx['CustomerID'])

    for date in daily:
        daily[date]['unique_customers'] = len(daily[date]['customers'])
        del daily[date]['customers']

    return dict(sorted(daily.items()))

def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)

    peak_day = None
    max_revenue = 0

    for date, data in daily.items():
        if data['revenue'] > max_revenue:
            max_revenue = data['revenue']
            peak_day = date
            count = data['transaction_count']

    return (peak_day, max_revenue, count)

def low_performing_products(transactions, threshold=10):
    product_data = {}

    for tx in transactions:
        product = tx['ProductName']
        quantity = tx['Quantity']
        revenue = quantity * tx['UnitPrice']

        if product not in product_data:
            product_data[product] = [0, 0.0]

        product_data[product][0] += quantity
        product_data[product][1] += revenue

    low_products = [
        (product, data[0], data[1])
        for product, data in product_data.items()
        if data[0] < threshold
    ]

    low_products.sort(key=lambda x: x[1])
    return low_products
