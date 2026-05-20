from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("base.html")

@app.route("/jogos/<categoria>")
def jogos(categoria):
    if categoria == "RAWG":
        pass