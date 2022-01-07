from os import path, environ
from dotenv import load_dotenv

load_dotenv()

path = path.abspath(path.dirname(__file__))

class ConfigBase:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")

class Development(ConfigBase):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{path}/application/database/database.db"

class Production(ConfigBase):
    Debug = False
    if(environ.get("DATABASE_URL") != None):
        SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL").replace('postgres://', 'postgresql://')

app_config = {
    "development": Development(),
    "testing": None,
    "production": Production()
}

app_env = environ.get("FLASK_ENV")

if app_env is None:
    app_env = "development"
    environ["FLASK_ENV"] = "development" 
