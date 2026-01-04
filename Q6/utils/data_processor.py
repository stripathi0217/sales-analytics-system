from collections import defaultdict


# -------------------------------------------------
# PARSE TRANSACTIONS
# -------------------------------------------------
def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines:
        parts = line.split('|')
        if len(parts) != 8:
            continue

        tid, date, pid, pname, qty, price, cid, region = parts

        pname = pname.replace(',', '')
        qty = qty.replace(',', '')
        price = price.replace(',', '')

        try:
            qty = int(qty)
            price = float(price)
        except ValueError:
            continue

        transactions.append({
            'TransactionID': tid,
            'Date': date,
            'ProductID': pid,
            'ProductName': pname,
            'Quantity': qty,
            'UnitPrice': price,
            'CustomerID': cid,
            'Region': region
        })

    return transactions


# -------------------------------------------------
# VALIDATE & FILTER
# -------------------------------------------------
def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0

    for tx in transactions:
        if (
            tx['Quantity'] <= 0 or
            tx['UnitPrice'] <= 0 or
            not tx['TransactionID'].startswith('T') or
            not tx['ProductID'].startswith('P') or
            not tx['CustomerID'].startswith('C')
        ):
            invalid += 1
            continue

        valid.append(tx)

    if region:
        valid = [tx for tx in valid if tx['Region'] == region]

    if min_amount is not None:
        valid = [tx for tx in valid if tx['Quantity'] * tx['UnitPrice'] >= min_amount]

    if max_amount is not None:
        valid = [tx for tx in valid if tx['Quantity'] * tx['UnitPrice'] <= max_amount]

    return valid, invalid, {}


# -------------------------------------------------
# PART 2 – ANALYTICS FUNCTIONS
# -------------------------------------------------
def calculate_total_revenue(transactions):
    return sum(tx['Quantity'] * tx['UnitPrice'] for tx in transactions)


def region_wise_sales(transactions):
    data = defaultdict(lambda: {'total_sales': 0, 'transaction_count': 0})
    total = calculate_total_revenue(transactions)

    for tx in transactions:
        amt = tx['Quantity'] * tx['UnitPrice']
        data[tx['Region']]['total_sales'] += amt
        data[tx['Region']]['transaction_count'] += 1

    for region in data:
        data[region]['percentage'] = round(
            (data[region]['total_sales'] / total) * 100, 2
        )

    return dict(data)


def top_selling_products(transactions, n=5):
    data = defaultdict(lambda: {'qty': 0, 'revenue': 0})

    for tx in transactions:
        data[tx['ProductName']]['qty'] += tx['Quantity']
        data[tx['ProductName']]['revenue'] += tx['Quantity'] * tx['UnitPrice']

    result = sorted(
        [(k, v['qty'], v['revenue']) for k, v in data.items()],
        key=lambda x: x[1],
        reverse=True
    )

    return result[:n]


def customer_analysis(transactions):
    data = defaultdict(lambda: {
        'total_spent': 0,
        'purchase_count': 0,
        'products_bought': set()
    })

    for tx in transactions:
        amt = tx['Quantity'] * tx['UnitPrice']
        cid = tx['CustomerID']
        data[cid]['total_spent'] += amt
        data[cid]['purchase_count'] += 1
        data[cid]['products_bought'].add(tx['ProductName'])

    result = {}
    for cid, info in data.items():
        result[cid] = {
            'total_spent': info['total_spent'],
            'purchase_count': info['purchase_count'],
            'avg_order_value': round(info['total_spent'] / info['purchase_count'], 2),
            'products_bought': list(info['products_bought'])
        }

    return dict(result)


def daily_sales_trend(transactions):
    data = defaultdict(lambda: {
        'revenue': 0,
        'transaction_count': 0,
        'unique_customers': set()
    })

    for tx in transactions:
        amt = tx['Quantity'] * tx['UnitPrice']
        date = tx['Date']
        data[date]['revenue'] += amt
        data[date]['transaction_count'] += 1
        data[date]['unique_customers'].add(tx['CustomerID'])

    result = {}
    for date in sorted(data):
        result[date] = {
            'revenue': data[date]['revenue'],
            'transaction_count': data[date]['transaction_count'],
            'unique_customers': len(data[date]['unique_customers'])
        }

    return result


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)

    peak_date = max(daily, key=lambda d: daily[d]['revenue'])
    peak = daily[peak_date]

    return peak_date, peak['revenue'], peak['transaction_count']


def low_performing_products(transactions, threshold=10):
    data = defaultdict(lambda: {'qty': 0, 'revenue': 0})

    for tx in transactions:
        data[tx['ProductName']]['qty'] += tx['Quantity']
        data[tx['ProductName']]['revenue'] += tx['Quantity'] * tx['UnitPrice']

    result = [
        (k, v['qty'], v['revenue'])
        for k, v in data.items()
        if v['qty'] < threshold
    ]

    return sorted(result, key=lambda x: x[1])
