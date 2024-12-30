from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Software Developer - I',
    'company': 'ABC Company',
    'location': 'Bangalore, India',
    'experience': '1',
    'Salary': '6.5LPA'
  },
  {
    'id': 2,
    'title': 'Frontend Developer',
    'company': 'Xyz corp.',
    'location': 'Chennai, India',
    'experience': '3',
    'Salary': '10LPA'
  },
  {
    'id': 3,
    'title': 'Backend Developer',
    'company': 'Kekron-Mekron corp.',
    'location': 'Hydrabad, India',
    'experience': '2',
    'Salary': '20LPA'
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'company': 'Rotten Tomatoes',
    'location': 'Bangalore, India',
    'experience': '7',
    'Salary': '50LPA'
  }
  
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs_list = JOBS)

@app.route("/api/jobs")
def api():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8080, debug = True)