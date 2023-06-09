import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение переменных окружения
BMP_API_URL = os.getenv("BMP_API_URL")
PG_URL = os.getenv("PG_URL")
SBERMOCK_API_URL = os.environ.get("SBERMOCK_API_URL")

BMP_API_TOKEN = os.getenv("BMP_API_TOKEN")
BMP_API_TOKEN_ADMIN = os.getenv("BMP_API_TOKEN_ADMIN")


PG_DB_HOST = os.getenv("PG_DB_HOST")
PG_DB_PORT = os.getenv("PG_DB_PORT")
PG_DB_NAME = os.getenv("PG_DB_NAME")
PG_DB_USER = os.getenv("PG_DB_USER")
PG_DB_PASSWORD = os.getenv("PG_DB_PASSWORD")