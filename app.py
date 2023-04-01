from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'data analyst',
  'location': 'Delhi, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 1,
  'title': 'data scientist',
  'location': 'remote',
}, {
  'id': 1,
  'title': 'frontend',
  'location': 'bangaluru, India',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 1,
  'title': 'backend',
  'location': 'San Francisco, USA',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
