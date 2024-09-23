from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    codigo, nombre, apellido, actividad, horainicio, horafinal = data["codigo"], data["nombre"], data["apellido"], data["actividad"], data["horainicio"], data["horafinal"]
    insert(codigo, nombre, apellido, actividad, horainicio, horafinal)
    return "User added"

     
if _name_ == "_main_":    
    host = "127.0.0.1",
    port =8000,
    app.run(host, port, True)