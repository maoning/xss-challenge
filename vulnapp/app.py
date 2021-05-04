from flask import Flask, abort, render_template, redirect, request, url_for
import requests
from os import path, environ

DEADLINE = 6

app = Flask(__name__)
app._static_folder = path.abspath('static/')

@app.errorhandler(403)
def forbbiden(e):
    return render_template('error.html', error=str(e)), 403

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', error=str(e)), 500

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
        response = requests.get(url, params = {'message': message}, timeout=DEADLINE)
        if (response.status_code < 400):
            return redirect(url_for('submission_result', message=message))
        else:
            abort(500, description=response.text)
    except requests.exceptions.Timeout:
        app.logger.info('xssbot failed to return a response in %ds', DEADLINE)
        abort(500, description='It took admin too long to read the message, admin gave up :(')
    except Exception as e:
        app.logger.error('unexpected exception encountered when calling xssbot')
        abort(500, description='Unexpected expected exception encountered')


@app.route('/admin', methods=['GET'])
def admin():
    secret = request.cookies.get(environ.get('COOKIE_NAME'))
    if secret == environ.get('COOKIE_VALUE'):
        return render_template('admin.html', flag = environ.get('FLAG'))
    else:
        abort(403, description='Only admin can see this page')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
