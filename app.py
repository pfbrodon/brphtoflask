from flask import Flask, render_template
import os

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

@app.route('/galeria_1')
def galeria_1():
    # Ruta de la carpeta de imágenes
    ruta_imagenes = os.path.join(app.static_folder, 'images')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_1.html', imagenes=imagenes)


if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000

