import requests

BASE_URL = "https://dummyjson.com/products"


def fetch_all_products():
    """
    Fetches all products from DummyJSON API
    Returns: list of product dictionaries
    """
    try:
        response = requests.get(f"{BASE_URL}?limit=100", timeout=10)
        response.raise_for_status()

        data = response.json()
        print("API fetch successful")

        return data.get("products", [])

    except Exception as e:
        print("API fetch failed:", e)
        return []


def create_product_mapping(api_products):
    """
    Creates mapping of product ID to product info
    """
    product_mapping = {}

    for product in api_products:
        product_mapping[product["id"]] = {
            "category": product.get("category"),
            "brand": product.get("brand"),
            "rating": product.get("rating")
        }

    return product_mapping
