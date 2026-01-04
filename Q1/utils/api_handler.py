def get_product_info(product_id):
    fake_api_data = {
        "P101": "Laptop",
        "P102": "Mouse",
        "P103": "Keyboard"
    }

    return fake_api_data.get(product_id, "Unknown Product")
