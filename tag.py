import os, flask, smtplib, shelve, math, random, json, logging, datetime
from   os  import environ
from flask import Flask, session, request, redirect, url_for, escape


app = Flask('I School Tag')
app.debug = True
app.secret_key = '\xfai\x17^\xc1\x84U\x13\x1c\xaeU\xb1\xd5d\xe8:\x08\xf91\x19w\x843\xee'
db    = shelve.open("db/shorten")

def createUserID():
	#app.logger.debug("createUID " + str(username))
	username = (int) (random.random() * 1000000);
	return username

def updateTagged(newTagged):
	db['tagged'] = newTagged;
	print "tagged [" + newTagged + "]"
	srv = connectEmailServer()
	for usr in usrDB.keys():
		print "email user[" + usr + "] = " + str(usrDB[usr])
		email(srv, usr, newTagged)
	srv.quit()


def connectEmailServer():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login('littlestbear1873@gmail.com', 'South Hall')
	return server

def email(srv, usr, tagged):
	rc = srv.sendmail('littlestbear1873@gmail.com', str(usrDB[usr]), str(tagged) + " is now IT")
	print "emailing " + str(usrDB[usr]) + " = " + str(rc)



@app.errorhandler(404)
def pageNotFound(error):
    return "Four-Oh-Four.\n<p>Sadly, this page does not exist</p>", 404


@app.route('/')
def index():
	taggedName = request.args.get("name", "default_name")
	#updateTagged(tagged)
	#resp = Flask.make_response(flask.Flask.render_template('index.html', title=" ", name=tagged))
    #resp.set_cookie('uid', uid);	
	resp = flask.make_response(flask.render_template('index.html', title='I School Tag', name=taggedName))
	return resp; #"Hello World, bitches! " + taggedName;


