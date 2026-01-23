import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

"""Запуск бызы данных"""

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


def clean(s: str):
    if not s:
        return ""
    return "".join(c for c in s if c.isprintable()).strip()


DB_USER = clean(os.getenv("DB_USER"))
DB_PASSWORD = clean(os.getenv("DB_PASSWORD"))
DB_NAME = clean(os.getenv("DB_NAME"))
DB_HOST = clean(os.getenv("DB_HOST"))
DB_PORT = clean(os.getenv("DB_PORT"))

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print("DATABASE_URL =", repr(DATABASE_URL))

engine = create_engine(DATABASE_URL, echo=True, future=True)


class Base(DeclarativeBase):
    pass
