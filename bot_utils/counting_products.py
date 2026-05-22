from database.utils import db_get_cart_items


def counting_products(chat_id, user_text):

    items = db_get_cart_items(chat_id)
    if not items:
        return None

    text = f"<b>{user_text}</b>\n\n"
    total_products = 0
    total_price = 0
    count = 0
    cart_id = None

    for idx, item in enumerate(items, start=1):
        name = item["product_name"]
        qty = item["quantity"]
        price = float(item["final_price"])

        item_total = price * qty

        total_price += item_total
        total_products += qty
        count += 1
        cart_id = item["product_id"]

        text += f"<b>{idx}. {name}</b>\n"
        text += f"<b>Количество:</b> {qty}\n"
        text += f"<b>Стоимость:</b> {item_total:.2f} руб\n\n"

    text += (
        f"<b>Общее количество продуктов:</b> {total_products}\n"
        f"<b>Общая стоимость корзины:</b> {total_price:.2f} руб"
    )

    return count, text, total_price, cart_id
