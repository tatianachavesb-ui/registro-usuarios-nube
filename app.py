"""Ejemplo: registro y listado de la tabla 'usuario' con Flask + MySQL (PyMySQL)."""
from flask import Flask, render_template, request, redirect, url_for, flash
from db import obtener_conexion

app = Flask(__name__)
app.secret_key = "cambia-esta-clave"


@app.route("/")
def index():
    return redirect(url_for("listar"))


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        cedula = request.form.get("cedula", "").strip()
        nombre = request.form.get("nombre", "").strip()
        if not cedula.isdigit() or not nombre:
            flash("La cédula debe ser numérica y el nombre es obligatorio.", "error")
            return render_template("registrar.html", cedula=cedula, nombre=nombre)
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                # Consulta parametrizada: evita inyección SQL
                cursor.execute("INSERT INTO usuario (cedula, nombre) VALUES (%s, %s)", (cedula, nombre))
            conexion.commit()
            flash("Usuario registrado correctamente.", "ok")
            return redirect(url_for("listar"))
        except Exception as e:
            conexion.rollback()
            if "Duplicate" in str(e) or "1062" in str(e):
                flash("Ya existe un usuario con esa cédula.", "error")
            else:
                flash(f"Error al registrar: {e}", "error")
            return render_template("registrar.html", cedula=cedula, nombre=nombre)
        finally:
            conexion.close()
    return render_template("registrar.html")


@app.route("/usuarios")
def listar():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT cedula, nombre FROM usuario ORDER BY nombre")
            usuarios = cursor.fetchall()
    finally:
        conexion.close()
    return render_template("listar.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
