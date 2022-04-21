from flask import Flask, render_template, redirect, url_for, request
from src import astro, analysis


app = Flask(__name__)

result = ''
name1, name2 = '', ''


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/checker', methods=['GET'])
def checker():
    return render_template('checker.html', result=result, name1=name1, name2=name2)


@app.route('/get_statistics', methods=['GET'])
def stat():
    top = analysis.make_top()
    return render_template('stat.html', top=top)


@app.route('/enter_names', methods=['POST'])
def enter_names():
    global name1, name2
    name1 = request.form['name1']
    name2 = request.form['name2']

    global result
    result = astro.calculate_compatibility(name1, name2)

    if name1 and name2:
        with open("server/database/name_frequency.txt", 'a') as data:
            data.write(name1 + '\n')
            data.write(name2 + '\n')

    return redirect(url_for('checker'))


if __name__ == "__main__":
    app.run()