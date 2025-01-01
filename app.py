from flask import Flask, render_template, jsonify
from datetime import date
from database import get_jobData_from_db, get_specificJobData_from_db
app = Flask(__name__)

current_date = date.today()
current_year = current_date.year

@app.route("/")
def home():
  jobs = get_jobData_from_db()
  return render_template('home.html', jobs_list = jobs, year = current_year)

@app.route("/job/<id>")
def get_job(id):
  job = get_specificJobData_from_db(id)
  if not job:
    return render_template('404.html')
  return render_template('jobPage.html', jobDetail = job, year = current_year)

@app.route("/api/jobs")
def api():
  jobs = get_jobData_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080, debug = True)