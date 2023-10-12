def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["Apple", "Banana", "Apple", "Orange", "Apple", "Grapes"]
target = "Apple"
result = linear_search_product(products, target)
print(f"Indices of '{target}': {result}")