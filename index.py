from flask import Flask, render_template

app = Flask(__name__)

matters = [
    'ethen_ethane',
    'propane'
]


@app.route('/')
def index():
    return render_template('index.html', matters=matters)


@app.route('/matter/<int:matter_id>')
def show_matter(matter_id):
    return render_template('index.html', id=matter_id, matters=matters)
