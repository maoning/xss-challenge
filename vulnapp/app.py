from flask import Flask, render_template, redirect, request, url_for
import requests
from os import path

app = Flask(__name__)
app._static_folder = path.abspath('static/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitted')
def submission_result():
    message = request.args.get('message')
    return render_template('submitted.html', message=message)

@app.route('/message', methods=['POST'])
def message():
    message = request.form.get('message')
    return redirect(url_for('submission_result', message=message))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
