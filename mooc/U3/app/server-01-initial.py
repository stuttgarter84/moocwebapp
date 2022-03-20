# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/home')
def home():
    return app.send_static_file('home.html')

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route('/signup')
def signup():
    return app.send_static_file('signup.html')





# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)