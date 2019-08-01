from project import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anouk'}
    return render_template('index.html', title='Draagmuur15', user=user)