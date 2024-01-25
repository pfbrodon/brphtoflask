from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/destacados")
def destacados():
    return render_template('destacados.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000

