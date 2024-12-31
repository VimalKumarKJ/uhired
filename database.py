from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)

def get_jobData_from_db():
  with engine.connect() as connect:
    result = connect.execute(text("SELECT * FROM jobs"))
    jobs= []
    for row in result.all():
        jobs.append(dict(row._mapping))
    return jobs