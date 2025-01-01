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
        result = connect.execute(text("SELECT * FROM jobs ORDER BY id"))
        jobs = []
        for row in result:
            jobs.append(dict(row._mapping))
        return jobs

def get_specificJobData_from_db(id):
    with engine.connect() as connect:
        result = connect.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        row = result.all()
        if len(row) == 0:
            return None
        else:
            return dict(row[0]._mapping)
        
def store_applicant_data(id, userData):
    with engine.connect() as connect:
        query = text("""
            INSERT INTO applicantsdata(
                job_id, fname, lname, email, phone, expt_salary, start_date, experience, resume
            ) 
            VALUES(
                :jobId, :fname, :lname, :email, :phone, :exptSalary, :startDate, :experience, :resumeLink
            )
        """)
        connect.execute(query, {
            'jobId': id,
            'fname': userData['fname'],
            'lname': userData['lname'],
            'email': userData['email'],
            'phone': userData['phone'],
            'exptSalary': userData['salary'],
            'startDate': userData['availability'],
            'experience': userData['experience'],
            'resumeLink': userData['resume']
        })
        connect.commit()