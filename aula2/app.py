from flask import Flask, render_template, request, redirect, url_for
from newDAO import DAO

app = Flask(__name__)

dao = DAO()

@app.route('/app-school')
@app.route('/app-school/')
@app.route('/app-school/index')
@app.route('/app-school/index.html')
def index():
    return render_template('index.html')

#######
# CURSO
#######

@app.route('/app-school/curso/listar')
def listar_curso():
    return render_template('/curso/listar.html', cursos=dao.listar('c'))

@app.route('/app-school/curso/novo')
def novo_curso():
    return render_template('/curso/inserir.html')

@app.route('/app-school/curso/inserir', methods=['POST'])
def inserir_curso():
    cnome = request.form.get('nome')
    descricao = request.form['descricao']
    print(cnome, descricao)
    dao.inserir('c', ['nome', 'descricao'],[cnome, descricao])
    return redirect(url_for('listar_curso'))

@app.route('/app-school/curso/cadastrar')
def cadastrar_curso():
    return render_template('/curso/form.html')

@app.route('/app-school/curso/remover')
def remover_curso():
    return render_template('/curso/remover.html')

@app.route('/app-school/curso/deletar', methods=['POST'])
def deletar_curso():
    cctodel = []
    cvtodel = []
    cnome = request.form.get('nome')
    if cnome != "":
        cctodel = ('nome')
        cvtodel = (cnome)
    descricao = request.form['descricao']
    if descricao != "":
        cctodel = 'descricao'
        cvtodel = descricao
    dao.deletar('c', cctodel, cvtodel)
    return redirect(url_for('listar_curso'))

###########
# ESTUDANTE
###########

@app.route('/app-school/estudante/listar')
def listar_estudante():
    return render_template('/estudante/listar.html', estudantes=dao.listar('e'))

@app.route('/app-school/estudante/novo')
def novo_estudante():
    return render_template('/estudante/inserir.html')

@app.route('/app-school/estudante/inserir', methods=['POST'])
def inserir_estudante():
    enome = request.form.get('nome')
    email = request.form['email']
    idade = request.form['idade']
    print(enome, email, idade)
    dao.inserir('e', ['nome', 'email', 'idade'],[enome, email, idade])
    return redirect(url_for('listar_estudante'))

@app.route('/app-school/estudante/cadastrar')
def cadastrar_estudante():
    return render_template('/estudante/form.html')

@app.route('/app-school/estudante/remover')
def remover_estudante():
    return render_template('/estudante/remover.html')

@app.route('/app-school/estudante/deletar', methods=['POST'])
def deletar_estudante():
    ectodel = []
    evtodel = []
    enome = request.form.get('nome')
    if enome != '':
        ectodel = 'nome'
        evtodel = enome
    email = request.form['email']
    if email != '':
        ectodel = 'email'
        evtodel = email
    idade = request.form['idade']
    if idade != '':
        ectodel = 'idade'
        evtodel = idade
    dao.deletar('e', ectodel, evtodel)
    return redirect(url_for('listar_estudante'))

###########
# PROFESSOR
###########

@app.route('/app-school/professor/listar')
def listar_professor():
    return render_template('/professor/listar.html', professores=dao.listar('p'))

@app.route('/app-school/professor/novo')
def novo_professor():
    return render_template('/professor/inserir.html')

@app.route('/app-school/professor/inserir', methods=['POST'])
def inserir_professor():
    pnome = request.form.get('nome')
    curso = request.form['curso']
    cpf = request.form['cpf']
    print(pnome, curso, cpf)
    dao.inserir('p', ['nome', 'curso', 'cpf'],[pnome, curso, cpf])
    return redirect(url_for('listar_professor'))

@app.route('/app-school/professor/cadastrar')
def cadastrar_professor():
    return render_template('/professor/form.html')

@app.route('/app-school/professor/remover')
def remover_professor():
    return render_template('/professor/remover.html')

@app.route('/app-school/professor/deletar', methods=['POST'])
def deletar_professor():
    pctodel = []
    pvtodel = []
    pnome = request.form.get('nome')
    if pnome != "":
        pctodel = 'nome'
        pvtodel = pnome
    curso = request.form['curso']
    if curso != "":
        pctodel = 'curso'
        pvtodel = curso
    cpf = request.form['cpf']
    if cpf != "":
        pctodel = 'cpf'
        pvtodel = cpf
    dao.deletar('p', pctodel, pvtodel)
    return redirect(url_for('listar_professor'))