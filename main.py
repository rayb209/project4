"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import os
import sys
from flask import Flask
from flask import render_template
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
@app.route('/<name>')
def hello(name=None):
  """ Return me template at application /me URL."""
  return render_template('main.html',name=name)  

@app.route('/catwalk')
def cat(name=None):
  """ Return me template at application /me URL."""
  return render_template('catwalk.html', name=name)    

@app.route('/madlibs')
def mad(name=None):
  """ Return me template at application /me URL."""
  return render_template('madlibs.html', name=name)    


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404