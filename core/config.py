from dotenv import load_dotenv
import os
import sys


if getattr(sys, "frozen", False):

    BASE_DIR = os.path.dirname(sys.executable)

else:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))


load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:

    API_BASE_URL = os.getenv("API_BASE_URL")

    SQL_SERVER = os.getenv("SQL_SERVER")

    DATABASE = os.getenv("DATABASE")

    DRIVER = os.getenv("DRIVER")
