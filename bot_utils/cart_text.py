def generate_cart_text(cart_items):
    """Генерация о содержимом корзины"""

    if not cart_items:
        return "Коризна пуста🗑️"

    text = "Содержимое корзины🗑️\n"
    total = 0.0

    for item in cart_items:
        name = item.get("product_name", "Товар не найден")
        quantity = item.get("quantity", 0)
        final_price = item.get("final_price", 0)

        total += float(final_price)

        text += f"{name}: {quantity}, {final_price}₽\n"

    text += f"\nИтого: {total} руб."
    return text