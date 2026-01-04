def clean_sales_data(raw_records):
    valid_records = []
    invalid_count = 0

    for record in raw_records:
        parts = record.split('|')

        # Skip header
        if parts[0] == "TransactionID":
            continue

        # Wrong number of columns
        if len(parts) != 8:
            invalid_count += 1
            continue

        transaction_id, date, product_id, product_name, quantity, price, customer_id, region = parts

        # Validation rules
        if not transaction_id.startswith('T'):
            invalid_count += 1
            continue

        if customer_id.strip() == "" or region.strip() == "":
            invalid_count += 1
            continue

        # Remove commas
        product_name = product_name.replace(',', '')
        quantity = quantity.replace(',', '')
        price = price.replace(',', '')

        try:
            quantity = int(quantity)
            price = float(price)
        except:
            invalid_count += 1
            continue

        if quantity <= 0 or price <= 0:
            invalid_count += 1
            continue

        valid_records.append({
            "transaction_id": transaction_id,
            "date": date,
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": price,
            "customer_id": customer_id,
            "region": region
        })

    return valid_records, invalid_count
