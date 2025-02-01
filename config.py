import os

import dotenv


dotenv.load_dotenv(".env")


PROJECT_ROOT_PATH = os.path.dirname(__file__)

FLASK_SECRET = os.getenv("FLASK_SECRET")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{PROJECT_ROOT_PATH}/database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

HOST = "0.0.0.0"
PORT = 5000
DEBUG_MODE = False

SUPER_USERS = {
    -1: "Admin"
}
