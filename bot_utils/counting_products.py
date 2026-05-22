from database.utils import db_get_cart_items


def counting_products(chat_id, user_text):
    """Подсчёт продуктов из корзины и формирование текста менеджеру"""
    items = db_get_cart_items(chat_id)
    print("ITEMS", items)
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

        item_total = qty * price
        total_price += item_total
        count += 1
        cart_id = item["product_id"]

        text += f"<b>{idx}. {name}</b>\n"
        text += f"<b>{qty}</b>\n"
        text += f"<b>Стоимость - {item_total:.2f}₽</b>\n"

    text += (
        f"Общее кол-во товаров: {total_products}\n"
        f"Стоимость корзины: {total_price}₽\n"
    )
    return count, text, total_price, cart_id