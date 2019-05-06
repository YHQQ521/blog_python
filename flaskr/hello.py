from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the first page,hello, world!'


@app.route('/hello')
def hello():
    return 'This is a common function,哈哈哈哈'


@app.route('/user/<username>')
def user(username):
    return 'User %s' % username
