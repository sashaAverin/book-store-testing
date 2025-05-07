import os
from dotenv import load_dotenv
load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    REG_EMAIL = os.getenv("REG_EMAIL")
    PASSWORD = os.getenv("PASSWORD")