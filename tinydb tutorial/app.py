from flask import Flask, render_template, request, redirect, url_for
from tinyDB_tutorial import DAO

app = Flask(__name__)

@app.route('/app-school')
@app.route('/app-school/')
@app.route('/app-school/index')
@app.route('/app-school/index.html')
def index():
    return render_template('index.html')

@app.route('/app-school/full-stack/listar')
def listar():
    return render_template('listar.html')

@app.route('/app-school/full-stack/inserir')
def inserir():
    DAO().inserir()
    return redirect(url_for('listar'))