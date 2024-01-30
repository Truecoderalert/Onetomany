from flask_app import app
from flask import Flask, request, render_template, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja


@app.route('/')
def home():
    alldojos = Dojo.get_all()
    
    return render_template('show_dojos.html' , alldojos = alldojos)

@app.route('/redirecttoinfo',methods=['post'])
def turntoresult():
    Dojo.create(request.form)
    return redirect('/')






if __name__=='__main__':
    app.run(debug=True)