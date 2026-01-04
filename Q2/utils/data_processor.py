def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """

    transactions = []

    for line in raw_lines:
        parts = line.split('|')

        # Skip rows with incorrect number of fields
        if len(parts) != 8:
            continue

        transaction_id, date, product_id, product_name, quantity, unit_price, customer_id, region = parts

        # Clean product name
        product_name = product_name.replace(',', '')

        # Clean numeric fields
        quantity = quantity.replace(',', '')
        unit_price = unit_price.replace(',', '')

        try:
            quantity = int(quantity)
            unit_price = float(unit_price)
        except ValueError:
            continue

        transaction = {
            'TransactionID': transaction_id,
            'Date': date,
            'ProductID': product_id,
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'CustomerID': customer_id,
            'Region': region.strip()
        }

        transactions.append(transaction)

    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters
    """

    valid_transactions = []
    invalid_count = 0

    total_input = len(transactions)

    # STEP 1: VALIDATE TRANSACTIONS
    for tx in transactions:
        if tx['Quantity'] <= 0 or tx['UnitPrice'] <= 0:
            invalid_count += 1
            continue

        if not tx['TransactionID'].startswith('T'):
            invalid_count += 1
            continue

        if not tx['ProductID'].startswith('P'):
            invalid_count += 1
            continue

        if not tx['CustomerID'].startswith('C'):
            invalid_count += 1
            continue

        if tx['Region'] == "":
            invalid_count += 1
            continue

        valid_transactions.append(tx)

    # STEP 2: DISPLAY AVAILABLE OPTIONS (ONLY VALID DATA)
    regions = sorted(set(tx['Region'] for tx in valid_transactions))
    print("Available regions:", regions)

    amounts = [tx['Quantity'] * tx['UnitPrice'] for tx in valid_transactions]
    print("Transaction amount range:", min(amounts), "to", max(amounts))

    # STEP 3: APPLY OPTIONAL FILTERS
    if region:
        valid_transactions = [
            tx for tx in valid_transactions
            if tx['Region'] == region
        ]

    if min_amount is not None:
        valid_transactions = [
            tx for tx in valid_transactions
            if tx['Quantity'] * tx['UnitPrice'] >= min_amount
        ]

    if max_amount is not None:
        valid_transactions = [
            tx for tx in valid_transactions
            if tx['Quantity'] * tx['UnitPrice'] <= max_amount
        ]

    # STEP 4: SUMMARY
    summary = {
        'total_input': total_input,
        'invalid': invalid_count,
        'final_count': len(valid_transactions)
    }

    return valid_transactions, invalid_count, summary
