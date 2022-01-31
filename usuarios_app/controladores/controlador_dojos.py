from flask import render_template, request, redirect, session, url_for, flash
from usuarios_app import app
from usuarios_app.modelos.modelo_dojos import Dojos
from datetime import datetime

@app.route( '/', methods=['GET'] )
def paginaInicio():
    return render_template( "index.html")

@app.route( '/result/<idDojo>', methods=["GET"] )
def despliegaDojo(idDojo):
    if 'name' in session:
        nuevoDojo = {
            "id" : idDojo
        }
        dojo = Dojos.obtenerDojo( nuevoDojo )
        print("hehehe quiero ver:",dojo[0]["name"],"frfr")
        print("hehehe quiero ver:",dojo[0]["location"],"frfr")
        print("hehehe quiero ver:",dojo[0]["languaje"],"frfr")
        if dojo == False:
            flash("Información corrupta recibida")
        if dojo[0]["name"] == "  ":
            flash("No ingresó un nombre válido")
        if dojo[0]["location"] == " ":
            flash("No seleccionó la ubicación")
        if dojo[0]["languaje"] == False:
            flash("No seleccionó el lenguaje")
        return render_template( "result.html", dojo=dojo )
    else:
        return redirect( '/' )


@app.route( '/process', methods=["POST"] )
def registrarFormulario():
    nuevoDojo = {
        "id" : None,
        "name" : request.form["name"],
        "location" : request.form["location"],
        "languaje" : request.form["languaje"],
        "comment" : request.form["comment"],
        "created_at" : datetime.today(),
        "update_at" : datetime.today()
    }
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["languaje"] = request.form["languaje"]
    session["comment"] = request.form["comment"]
    session["created_at"] = datetime.today()
    session["update_at"] = datetime.today()
    idDojo = Dojos.agregaDojo( nuevoDojo )
    return redirect(url_for( 'despliegaDojo', idDojo=idDojo ))

@app.route( '/destroy_session', methods=["POST"] )
def borrarSession():
    session.clear()
    return redirect( '/' )

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"