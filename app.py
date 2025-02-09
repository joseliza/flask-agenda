from flask import Flask, render_template, request
from contactos import contactos

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/listar")
def listar():
    return render_template("listar.html", contactos=contactos)

@app.route("/buscar", methods=["GET"])
def buscar():
    nombre = request.args.get("nombre")
    resultado = None

    if nombre:
        if nombre in contactos:
            resultado = (nombre, contactos[nombre])
        else:
            resultado = {}

    return render_template("buscar.html", resultado=resultado)

@app.route("/insertar", methods=["GET", "POST"])
def insertar():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]

        if nombre in contactos:
            mensaje = "Ese contacto ya existe."
        else:
            contactos[nombre] = telefono
            mensaje = f"Contacto {nombre} agregado."

    return render_template("insertar.html", mensaje=mensaje)

@app.route("/borrar", methods=["GET", "POST"])
def borrar():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form["nombre"]

        if nombre in contactos:
            del contactos[nombre]
            mensaje = f"Contacto {nombre} eliminado."
        else:
            mensaje = "Contacto no encontrado."

    return render_template("borrar.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
