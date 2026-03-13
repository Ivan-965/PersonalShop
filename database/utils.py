from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.base import engine
from database.models import Users, Carts, Categories, FinallyCarts, Orders, Products
from sqlalchemy import update, select, func, join, DECIMAL

"""Модуль c функциями для работы с данными в базе данных."""


def get_session():
    return Session(engine)


def db_register_user(full_name, chat_id):
    """Register a new user in the database."""

    try:
        with get_session() as session:
            query = Users(name=full_name, telegram=chat_id)
            session.add(query)
            session.commit()
        return False
    except IntegrityError:
        return True


def db_update_user(chat_id, phone):
    """Добавления телефона пользователя в базу данных."""
    with get_session() as session:
        query = update(Users).where(Users.telegram == chat_id).values(phone=phone)
        session.execute(query)
        session.commit()


def db_create_user_cart(chat_id):
    """Создание корзины пользователя в базе данных."""
    try:
        with get_session() as session:
            subquery = session.scalar(select(Users).where(Users.telegram == chat_id))
            query = Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False

    except AttributeError:
        return False


def db_get_all_category():
    """Получение всех категорий из базы данных."""
    with get_session() as session:
        query = select(Categories)
        return session.scalars(query).all()


def db_get_finally_price(chat_id):
    """Получение итоговой цены"""

    with get_session() as session:
        query = select(func.sum(FinallyCarts.final_price)).select_from(
            join(Carts, FinallyCarts, Carts.id == FinallyCarts.cart_id)).join(Users, Users.id == Carts.user_id).where(
            Users.telegram == chat_id)
        return session.execute(query).fetchone()[0]


def db_get_last_orders(chat_id, limit=5):
    """Получение последних 5 заказов."""

    with get_session() as session:
        query = (
            select(Orders).
            join(Carts, Orders.cart_id == Carts.id).
            join(Users, Carts.user_id == Users.id).
            where(Users.telegram == chat_id).
            order_by(Orders.id.desc()).limit(limit)
        )
        return session.scalars(query).all()


def db_get_products(category_id):
    """получение продуктов по ID категории."""

    with get_session() as session:
        query = select(Products).where(Products.category_id == category_id)
        return session.scalars(query).all()


def db_get_product_by_id(product_id):
    """Возвращает информацию о товаре по его ID."""
    with get_session() as session:
        query = select(Products).where(Products.id == product_id)
        return session.scalar(query)


def db_get_user_cart(chat_id):
    """Получение корзины пользователя по ID корзины"""

    with get_session() as session:
        query = select(Carts).join(Users, Carts.user_id == Users.id).where(Users.telegram == chat_id)
        return session.scalar(query)


def db_add_or_update_item(
        cart_id: int,
        product_id: int,
        product_name: str,
        product_price: DECIMAL,
        increment: int = 0
):

    try:
        with get_session() as session:
            item = (
                session.query(FinallyCarts)
                .filter_by(cart_id=cart_id, product_id=product_id)
                .first()
            )

            if item:
                if increment != 0:
                    item.quantity = max(1, item.quantity + increment)
            else:
                qty = 1 if increment <= 0 else increment
                item = FinallyCarts(
                    cart_id=cart_id,
                    product_id=product_id,
                    product_name=product_name,
                    quantity=qty,
                    final_price=0
                )
                session.add(item)

            item.final_price = item.quantity * product_price

            products_sum, total_products = session.query(
                func.coalesce(func.sum(FinallyCarts.final_price), 0),
                func.coalesce(func.sum(FinallyCarts.quantity), 0)
            ).filter(
                FinallyCarts.cart_id == cart_id
            ).one()

            session.query(Carts).filter(
                Carts.id == cart_id
            ).update({
                Carts.total_price: products_sum,
                Carts.total_products: total_products
            })

            session.commit()

            return {
                "status": "ok",
                "total_price": float(products_sum),
                "total_products": int(total_products),
                "product_quantity": item.quantity
            }

    except Exception as e:
        return {"status": "error", "message": str(e)}
