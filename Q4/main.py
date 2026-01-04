from Q4.utils.file_handler import read_sales_data, save_enriched_data
from Q4.utils.api_handler import fetch_all_products, create_product_mapping


from Q2.utils.data_processor import parse_transactions, validate_and_filter


def enrich_sales_data(transactions, product_mapping):
    enriched = []

    for tx in transactions:
        enriched_tx = tx.copy()

        # Extract numeric product ID (P101 -> 101)
        try:
            product_id_num = int(tx["ProductID"][1:])
        except:
            product_id_num = None

        if product_id_num in product_mapping:
            api_data = product_mapping[product_id_num]
            enriched_tx["API_Category"] = api_data["category"]
            enriched_tx["API_Brand"] = api_data["brand"]
            enriched_tx["API_Rating"] = api_data["rating"]
            enriched_tx["API_Match"] = True
        else:
            enriched_tx["API_Category"] = None
            enriched_tx["API_Brand"] = None
            enriched_tx["API_Rating"] = None
            enriched_tx["API_Match"] = False

        enriched.append(enriched_tx)

    return enriched


# ---------------- RUN EVERYTHING ----------------

raw = read_sales_data("Q4/data/sales_data.txt")

parsed = parse_transactions(raw)
valid, _, _ = validate_and_filter(parsed)

api_products = fetch_all_products()
product_mapping = create_product_mapping(api_products)

enriched_transactions = enrich_sales_data(valid, product_mapping)

save_enriched_data(enriched_transactions)
