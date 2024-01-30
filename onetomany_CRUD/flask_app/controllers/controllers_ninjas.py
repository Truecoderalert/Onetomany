from flask_app import app
from flask import Flask, request, render_template, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_ninja import Ninja
from flask_app.models.models_dojo import Dojo



@app.route('/newninja')
def createnewninja():
    dojos = Dojo.get_all()
    return render_template('addninja.html' , dojos = dojos)

@app.route('/addninja', methods=['post'])
def showallninjas():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.addninja(data)
    return redirect('/')
    
@app.route('/master')
def showall():
    master = Ninja.allninjas()
    return render_template ('showone.html', master = master)
    
    
    