from flask import Flask
from flask import render_template
app = Flask (__name__)


@app.route('/')
def hello_world():
    return 'Hello Word'


@app.route('/test/')
def test():
    return render_template('templates.html')


if __name__ == '__main__':
    app.run()