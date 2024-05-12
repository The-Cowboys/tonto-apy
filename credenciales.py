from dotenv import load_dotenv
import os

load_dotenv()

class Credenciales :
    USUARIO:str = os.getenv("USUARIO")
    PASSWORD:str = os.getenv("PASSWORD")
    HOST:str = os.getenv("HOST")
    POERT:str = os.getenv ("POERT")
    DB_NOMBRE:str = os.getenv("DB_NOMBRE")

    DATABASE_URL = f"postgresql://{USUARIO}:{PASSWORD}@{HOST}:{POERT}/{DB_NOMBRE}"
