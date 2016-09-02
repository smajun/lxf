#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
# from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' % user_agent
    # return '<h1>Bad Request</h1>', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
    # return redirect('http://m.hanxinbank.com')


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

def load_user(id):
    if id == '1':
        return 'duoduo'


@app.route('/user/<id>')
def get_user(id):
    # def load_user(id):
    #     if id == 1:
    #         return 'duoduo'
    # user = 'duoduo'
    user = load_user(id)
    if not user:
        abort(404)
        # return '<h1>Error, %s!</h1>' % user
    return '<h1>Hello, %s!</h1>' % user


if __name__ == '__main__':
    app.run(debug=True)
