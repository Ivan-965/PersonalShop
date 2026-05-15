"""Модуль подготовки к запуску проекта"""
from os import getenv
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = getenv('TOKEN')

MANAGER_ID = int(os.getenv('MANAGER_ID', 0))