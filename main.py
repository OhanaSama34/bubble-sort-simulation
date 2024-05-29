from flask import Flask, render_template, request
from sort import *

app = Flask(__name__, template_folder='templates')

@app.route("/about")
def about():
    return render_template('about.html', title='About Our Team')

@app.route('/', methods=['GET', 'POST'])
def index():
    init= None
    steps = None
    if request.method == 'POST':
        array_str = request.form.get('array')
        init = array_str
        array = list(map(int, array_str.split(',')))
        steps = bubble_sort(array)
    return render_template('simulation.html', steps=steps, init=init, title='Home | Simulation')

if __name__ == '__main__':
    app.run(debug=True)