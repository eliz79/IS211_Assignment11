#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)

to_do = []
emails = []
priority_level = []

@app.route('/')
def hello_world():
    return render_template('index.html',
                           to_do=to_do,
                           emails=emails,
                           priority_level=priority_level)

@app.route('/submit', methods = ['POST'])
def submit():
    todos = request.form['todos']
    to_do.append(todos)
    email = request.form['email']
    emails.append(email)
    p_level = request.form['p_level']
    priority_level.append(p_level)
    return redirect('/')

if __name__ == "__main__":
    app.run()
