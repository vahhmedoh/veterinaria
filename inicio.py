from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/vulpix')
def vulpix():
    return render_template("vulpix.html")

@app.route('/magikarp')
def magikarp():
    return render_template("magikarp.html")

@app.route('/jolteon')
def jolteon():
    return render_template("jolteon.html")

