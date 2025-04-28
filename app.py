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
    ruta_imagenes = os.path.join(app.static_folder, 'images/galeria1/')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_1.html', imagenes=imagenes)

@app.route('/galeria_2')
def galeria_2():
    # Ruta de la carpeta de imágenes
    ruta_imagenes = os.path.join(app.static_folder, 'images/galeria2')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_2.html', imagenes=imagenes)

@app.route('/galeria_3')
def galeria_3():
    # Ruta de la carpeta de imágenes
    ruta_imagenes = os.path.join(app.static_folder, 'images/galeria3')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_3.html', imagenes=imagenes)

@app.route('/galeria_4')
def galeria_4():
    # Ruta de la carpeta de imágenes
    ruta_imagenes = os.path.join(app.static_folder, 'images/galeria4')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_4.html', imagenes=imagenes)

@app.route('/galeria_5')
def galeria_5():
    # Ruta de la carpeta de imágenes
    ruta_imagenes = os.path.join(app.static_folder, 'images/galeria5')

    # Obtener la lista de nombres de archivo de imágenes
    imagenes = [imagen for imagen in os.listdir(ruta_imagenes) if imagen.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    print(imagenes)
    # Renderizar la plantilla con la lista de imágenes
    return render_template('galeria_5.html', imagenes=imagenes)




if __name__=='__main__':  
    app.run(host="0.0.0.0", debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000, host="0.0.0.0"<-- para acceder desde cualquier IP, debug=True para ver errores en la consola
