import os
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker
from database.base import Base
from database.models import Users, Carts, FinallyCarts, Categories, Products, Orders
from dotenv import load_dotenv

"""Скрипт для инициализации базы данных"""

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def _create_database():
    """Создаёт базу данных, если она не существует"""
    default_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"
    default_engine = create_engine(default_url, echo=False)

    with default_engine.connect() as conn:
        conn.execute(text("COMMIT"))
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
            {"dbname": DB_NAME}
        ).scalar()

        if not result:
            print(f"создаём базу данных '{DB_NAME}'...")
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
            print(f"База данных '{DB_NAME}' создана")
        else:
            print(f"База данных '{DB_NAME}' уже существует")


def init_db():
    _create_database()

    print("создаём таблицы...")
    Base.metadata.create_all(engine)
    print('Таблицы gotovu')

    with SessionLocal() as session:

        categories = ["Торты", "Сыр", "Печенье"]
        category_map = {}

        for name in categories:
            category = session.scalar(select(Categories).filter_by(category_name=name))
            if not category:
                category = Categories(category_name=name)
                session.add(category)
                session.flush()
            category_map[name] = category.id
        products = [
            ("Торты", "Медовик", 45, "мёд, мука, сахар, яйца, масло", "media/honey_cake.jpg"),
            ("Торты", "Прага", 100, "бисквит, крем, пропитка, глазурь", "media/praga_cake.jpg"),
            ("Торты", "Рождественское полено", 80, "мука, яйца, сахар, масло, соль", "media/poleno_cake.jpg"),
            ("Сыр", "Российский", 280, "мягкий сливочный вкус, натуральное производство", "media/russian_cheese.jpg"),
            ("Сыр", "Голландский Гауда", 350, "классический голландский сыр, насыщенный аромат",
             "media/gouda_cheese.jpg"),
            ("Сыр", "Фета", 320, "соленый, рассыпчатый греческий сыр", "media/feta_cheese.jpg"),
            ("Печенье", "Овсяное", 120, "нежное овсяное печенье с кусочками шоколада", "media/oatmeal_cookie.jpg"),
            ("Печенье", "Сахарное", 100, "хрустящее традиционное песочное печенье", "media/sugar_cookie.jpg"),
            ("Печенье", "Имбирное", 150, "специальное пряное имбирное печенье с ароматом корицы",
             "media/gingerbread_cookie.jpg")]

        for category_name, name, price, desc, image in products:
            product_exists = session.scalar(select(Products).filter_by(product_name=name))
            if not product_exists:
                product = Products(
                    category_id=category_map[category_name],
                    product_name=name,
                    price=price,
                    description=desc,
                    image=image
                )
                session.add(product)

        session.commit()
        print("Первичные данные категорий ")


if __name__ == "__main__":
    init_db()
