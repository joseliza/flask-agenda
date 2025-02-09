from flask import Flask, render_template, request
from agenda import agenda

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/listar")
def listar():
    return render_template("listar.html", agenda=agenda)

@app.route("/buscar", methods=["GET"])
def buscar():
    nombre = request.args.get("nombre")
    resultado = None

    if nombre:
        if nombre in agenda:
            resultado = (nombre, agenda[nombre])
        else:
            resultado = {}

    return render_template("buscar.html", resultado=resultado)

@app.route("/insertar", methods=["GET", "POST"])
def insertar():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]

        if nombre in agenda:
            mensaje = "Ese contacto ya existe."
        else:
            agenda[nombre] = telefono
            mensaje = f"Contacto {nombre} agregado."

    return render_template("insertar.html", mensaje=mensaje)

@app.route("/borrar", methods=["GET", "POST"])
def borrar():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form["nombre"]

        if nombre in agenda:
            del agenda[nombre]
            mensaje = f"Contacto {nombre} eliminado."
        else:
            mensaje = "Contacto no encontrado."

    return render_template("borrar.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
