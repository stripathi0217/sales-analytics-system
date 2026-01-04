import requests

# -----------------------------------
# TASK 3.1: FETCH ALL PRODUCTS
# -----------------------------------
def fetch_all_products():
    """
    Fetches all products from DummyJSON API
    """
    url = "https://dummyjson.com/products?limit=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("API fetch successful")
        return response.json().get("products", [])
    except Exception as e:
        print("API fetch failed:", e)
        return []


# -----------------------------------
# TASK 3.1 (b): CREATE PRODUCT MAPPING
# -----------------------------------
def create_product_mapping(api_products):
    """
    Creates mapping of product ID to product details
    """
    mapping = {}
    for product in api_products:
        mapping[product["id"]] = {
            "title": product.get("title"),
            "category": product.get("category"),
            "brand": product.get("brand"),
            "rating": product.get("rating"),
        }
    return mapping


# -----------------------------------
# TASK 3.2: ENRICH SALES DATA
# -----------------------------------
def enrich_sales_data(transactions, product_mapping):
    """
    Enriches transactions with API product info
    """
    enriched = []

    for tx in transactions:
        new_tx = tx.copy()

        # Extract numeric product ID (P101 -> 101)
        try:
            product_id_num = int(tx["ProductID"][1:])
        except:
            product_id_num = None

        if product_id_num and product_id_num in product_mapping:
            api_product = product_mapping[product_id_num]
            new_tx["API_Category"] = api_product["category"]
            new_tx["API_Brand"] = api_product["brand"]
            new_tx["API_Rating"] = api_product["rating"]
            new_tx["API_Match"] = True
        else:
            new_tx["API_Category"] = None
            new_tx["API_Brand"] = None
            new_tx["API_Rating"] = None
            new_tx["API_Match"] = False

        enriched.append(new_tx)

    return enriched
