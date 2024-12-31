from flask import Flask, render_template, jsonify
from sqlalchemy import text
from datetime import date
from database import engine
app = Flask(__name__)

current_date = date.today()
current_year = current_date.year

def get_jobData_from_db():
  with engine.connect() as connect:
    result = connect.execute(text("SELECT * FROM jobs"))
    jobs= []
    for row in result.all():
        jobs.append(dict(row._mapping))
    return jobs
  



@app.route("/")
def home():
  jobs = get_jobData_from_db()
  return render_template('home.html', jobs_list = jobs, year = current_year)

@app.route("/api/jobs")
def api():
  jobs = get_jobData_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080, debug = True)