from flask import Flask, render_template
from datetime import datetime

app = Flask("hello2")

posts = [
    {
        "title": "O meu primeiraço Post",
        "body": "Aqui é o texto do post",
        "author": "Filipe",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu segundo Post",
        "body": "Aqui é o texto do post",
        "author": "Dória",
        "created": datetime(2022,7,26)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
