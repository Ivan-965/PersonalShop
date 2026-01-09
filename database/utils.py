from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.base import engine
from database.models import Users, Carts
from sqlalchemy import update, select

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
            query = Carts(user_id = subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False

    except AttributeError:
        return False
