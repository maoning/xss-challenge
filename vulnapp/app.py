from flask import Flask, abort, render_template, redirect, request, url_for
import requests
from os import path, environ


app = Flask(__name__)
app._static_folder = path.abspath('static/')

@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html'), 403

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
    try:
        url = 'http://' + environ.get('XSSBOT_HOST') + ':5555'
        app.logger.info('make request to %s', url)
        requests.get(url, params = {'message': message})
    except Exception as e:
        app.logger.info(e)
    finally:
        return redirect(url_for('submission_result', message=message))

@app.route('/admin', methods=['GET'])
def admin():
    secret = request.cookies.get(environ.get('COOKIE_NAME'))
    if secret == environ.get('COOKIE_VALUE'):
        return render_template('admin.html', flag = environ.get('FLAG'))
    else:
        abort(403, description='Only admin can see this page')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
