import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение переменных окружения
BMP_API_URL = os.getenv("BMP_API_URL")
PG_URL = os.getenv("PG_URL")
SBERMOCK_API_URL = os.environ.get("SBERMOCK_API_URL")

BMP_API_TOKEN = os.getenv("BMP_API_TOKEN")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")