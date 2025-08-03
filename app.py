from flask import Flask, render_template, jsonify
from flask_cors import CORS


JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 9,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Mumbai, India',
        'salary' : 'Rs. 14,00,000'
    },
    {
        'id' : 3,
        'title' : 'Frontend Engineer',
        'location' : 'Remote',
        'salary' : 'Rs. 7,00,000'
    },
    {
        'id' : 4,
        'title' : 'Backend Engineer',
        'location' : 'San Francisco, USA',
        'salary' : '$100,000'
    },

]

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)