#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A To Do List"""
#Author - Erica Liz

from flask import Flask, render_template
from flask import request, redirect
import re
app = Flask(__name__)

to_do = []

class MyTask:
    todo = None
    emails = None
    priority_level = None
    
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['todo']
    emails = request.form['emails']
    priority_level = request.form['priority_level']
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", emails):
        print "Email does not match. Enter again!"
        return render_template('/')
    else:            
        todo = MyTask()
        todo.todo = task
        todo.emails = emails
        todo.priority_level = priority_level
        to_do.append(todo)
    return render_template('index.html', to_do=to_do)
    
@app.route('/clear')
def clear():
    while len(to_do) > 0:
        for item in to_do:
            to_do.pop()
    return redirect('/')

if __name__ == "__main__":
    app.run()
