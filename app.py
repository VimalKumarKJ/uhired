import os
import requests
from flask import Flask, render_template, jsonify, request
from datetime import date
from database import get_jobData_from_db, get_specificJobData_from_db, store_applicant_data
app = Flask(__name__)

H_CAPTCHA_SECRET_KEY = os.getenv("H_CAPTCHA_SECRET_KEY")

current_date = date.today()
current_year = current_date.year

def verify_hcaptcha(hcaptcha_response):
    data = {
        'secret': H_CAPTCHA_SECRET_KEY,
        'response': hcaptcha_response
    }
    response = requests.post('https://hcaptcha.com/siteverify', data=data)
    result = response.json()
    return result.get('success', False)

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

@app.route("/job/<id>/apply", methods=["POST"])
def apply_job(id):
    data = request.form
    hcaptcha_response = request.form.get('h-captcha-response')
    print(hcaptcha_response)
    if not verify_hcaptcha(hcaptcha_response):
       return render_template('error.html', message="hCaptcha verification failed. Please try again.")
    job = get_specificJobData_from_db(id)
    store_applicant_data(id, data)
    return render_template('applicationSuccess.html', jobDetail=job, user=data)



@app.route("/api/jobs")
def api():
  jobs = get_jobData_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080, debug = True)