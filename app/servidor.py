from flask import Flask
from database import *

app = Flask(__name__)


@app.route("/")
def home():
    return "Home!"

@app.route("/lista")
def listar_sabores():
    sabores = {}
    sabores["sabores"] = lista_sabores_ativos()
    return sabores


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)
#     app.run()
