from flask import Flask, render_template
from restaurantes import restaurantes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", restaurantes=restaurantes)

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/restaurante/<int:id>")
def ver_restaurante(id):
    restaurante = restaurantes[id]
    return render_template("restaurante.html", restaurante=restaurante)