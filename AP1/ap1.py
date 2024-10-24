from tinydb import TinyDB, Query
from flask import Flask, render_template, request, redirect, url_for

#-------------------------------------------------------------
# Classe Aluno

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

#-------------------------------------------------------------
# Banco de Dados

class DAO():
    def __init__(self):
        self.db = TinyDB('bancoDeDados.json')
    
    def inserir(self, nome, matricula):
        self.db.insert({'nome': nome, 'matricula': matricula})
    
    def listar(self):
        return self.db.all()
    
    def atualizar(self, nome, matricula):
        self.db.update({'nome': nome, 'matricula': matricula}, Query().matricula == matricula)
        
    def deletar(self, matricula):
        self.db.remove(Query().matricula == matricula)

#-------------------------------------------------------------
# Flask e inicialização do DAO

app = Flask(__name__)

dao = DAO()

#-------------------------------------------------------------
# Rotas

@app.route('/')
def index():
    return render_template('index.html', alunos=dao.listar())

@app.route('/add')
def novo_aluno():
    return render_template('add.html')

@app.route('/edit', methods=['GET'])
def editar_aluno():
    matricula = request.args.get('id')
    return render_template('edit.html', matri=matricula)

@app.route('/inserir', methods=['POST'])
def inserir_aluno():
    cnome = request.form.get('nome')
    cmatricula = request.form.get('matricula')
    print(cnome, cmatricula)
    dao.inserir(cnome, cmatricula)
    return redirect(url_for('index'))

@app.route('/deletar', methods=['GET'])
def deletar_aluno():
    matricula = request.args.get('matricula')
    dao.deletar(matricula)
    return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def atualizar_aluno():
    matricula = request.args.get('mat')
    novonome = request.form.get('nome')
    print(novonome, matricula)
    dao.atualizar(novonome, matricula)
    return redirect(url_for('index'))