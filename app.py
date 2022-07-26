from flask import Flask, render_template

app = Flask("hello2")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/meucontato")
def meuContato():
    return render_template("index.html")