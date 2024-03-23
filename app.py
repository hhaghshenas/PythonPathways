from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Toronto, Canada",
    "salary": "CAD $100,000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Toronto, Canada",
    "salary": "CAD $130,000"
  },
  {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Toronto, Canada",
    "salary": "CAD $110,000"
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "Toronto, Canada",
    "salary": "CAD $120,000"
  },
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

  
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
