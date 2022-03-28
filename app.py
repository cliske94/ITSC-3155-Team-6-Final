from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html', title="Home")

@app.get("/about")
def about():
    return render_template('about.html', title="About Us")