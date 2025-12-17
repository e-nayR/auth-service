import os
from dotenv import load_dotenv
load_dotenv()

secret_key = os.getenv("SECRET_KEY")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")

db_url = f"postgresql+psycopg2://{user}:{password}@pg-svc:5432/{db}"