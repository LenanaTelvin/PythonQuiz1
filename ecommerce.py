def add_product(product_name: str, price: float, quantity: int) -> dict:
    product = {
        'product_name': product_name,
        'price': price,
        'quantity': quantity
    }
    return product


def update_price(product: dict, new_price: float) -> dict:
    product['price'] = new_price
    return product


def update_quantity(product: dict, quantity_change: int) -> dict:
    product['quantity'] += quantity_change
    return product

if __name__ == "__main__":
    product = add_product("Laptop", 45000.00, 10)
    print("Original product:", product)

    product = update_price(product, 38000.00)
    print("After price update:", product)

    product = update_quantity(product, 5)
    print("After increasing quantity:", product)

    product = update_quantity(product, -3)  
    print("After decreasing quantity:", product)
