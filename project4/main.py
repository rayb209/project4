"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
from flask import render_template
import urllib2
import json
import random
import uuid
from google.appengine.api import users
from google.appengine.api import channel
from utilities import funnames
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
  


@app.route('/cards')
def cat(name=None):
  """ Return me template at application /me URL."""
  return render_template('cards.html', name=name)    



@app.route('/cards2')
def mad(name=None):
  """ Return me template at application /me URL."""
  return render_template('cards2.html', name=name) 

@app.route('/')
def index():
    """Setup a the game"""
    roomid = generate_id()
    template_values = {
                       "roomid":roomid
                                     }
    return render_template("index.html",values=template_values)

@app.route('/<roomid>/<name>')
def chatroom_and_name(roomid,name):
    """Return a the game page"""
    token = channel.create_channel(name + roomid) 
    template_values = {
                       "roomid":roomid,
                        "token": channel.create_channel(name + roomid),
                        "yourname": name
                       }
    return render_template("cards3.html",values=template_values)

@app.route('/<roomid>')
def chatroom(roomid):
    
    
    template_values = {
                       "roomid":roomid,
                       }
    return render_template("getname.html",values=template_values)

  

@app.route('/sendmessage/<user>/<roomid>', methods=['GET', 'POST'])
def sendmessage(user,roomid):
    """sends a message that is useless"""
    message=request.form['message']

    channel.send_message(user+roomid,message)
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, the game is not available.', 404

def generate_id():
    """Return a game id"""
    return "%s-%s" % (str(uuid.uuid4())[:4],random.choice(funnames).lower())
