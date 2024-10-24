from tinydb import TinyDB, Query
from flask import Flask, render_template, request, redirect, url_for

class Produto:
    def __init__(self, tipo:str, titulo:str, localizacao:str, resumo:str, descricao:str, incluso:str, dicas:str, observacoes:str, precos:str, midias:str, numero_diarias:int, hospedagem:str, roteiro:str, disponivel:str, data_de_saida:str, limite_vagas:int):
        self.tipo = tipo
        self.titulo = titulo
        self.localizacao = localizacao
        self.resumo = resumo
        self.descricao = descricao
        self.rawincluso = incluso
        self.incluso = incluso.split(splitter)
        self.rawdicas = dicas
        self.dicas = dicas.split(splitter)
        self.rawobservacoes = observacoes
        self.observacoes = observacoes.split(splitter)
        self.rawprecos = precos
        self.precos = [x.split(splitter2) for x in precos.split(splitter)]
        self.rawmidias = midias
        self.midias = midias.split(splitter)
        self.numero_diarias = numero_diarias
        self.hospedagem = hospedagem
        self.roteiro = roteiro
        self.disponivel = disponivel
        self.data_de_saida = data_de_saida
        self.limite_vagas = limite_vagas

class DAO():
    def __init__(self):
        self.db = TinyDB('bancoDeDados.json')
    
    def inserir(self, produto):
        self.db.insert({'tipo': produto.tipo, 'titulo': produto.titulo, 'localizacao': produto.localizacao, 'resumo': produto.resumo, 'descricao': produto.descricao, 'incluso': produto.incluso, 'dicas': produto.dicas, 'observacoes': produto.observacoes, 'precos': produto.precos, 'midias': produto.midias, 'numero_diarias': produto.numero_diarias, 'hospedagem': produto.hospedagem, 'roteiro': produto.roteiro, 'disponivel': produto.disponivel, 'data_de_saida': produto.data_de_saida, 'limite_vagas': produto.limite_vagas, 'rawincluso': produto.rawincluso, 'rawdicas': produto.rawdicas, 'rawobservacoes': produto.rawobservacoes, 'rawprecos': produto.rawprecos, 'rawmidias': produto.rawmidias})
    
    def listar(self):
        return self.db.all()
    
    def listar_por_tipo(self, tipo):
        return self.db.search(Query().tipo == tipo)
    
    def atualizar(self, titulo, localizacao, resumo, descricao, incluso, dicas, observacoes, precos, midias, numero_diarias, hospedagem, roteiro, disponivel, data_de_saida, limite_vagas):
        self.db.update({'localizacao': localizacao, 'resumo': resumo, 'descricao': descricao, 'incluso': incluso.split(splitter), 'dicas': dicas.split(splitter), 'observacoes': observacoes.split(splitter), 'precos': [x.split(splitter2) for x in precos.split(splitter)], 'midias': midias.split(splitter), 'numero_diarias': numero_diarias, 'hospedagem': hospedagem, 'roteiro': roteiro, 'disponivel': disponivel, 'data_de_saida': data_de_saida, 'limite_vagas': limite_vagas, 'rawincluso': incluso, 'rawdicas': dicas, 'rawobservacoes': observacoes, 'rawprecos': precos, 'rawmidias': midias}, Query().titulo == titulo)
        
    def deletar(self, titulo):
        self.db.remove(Query().titulo == titulo)
    
    def buscar(self, titulo):
        return self.db.search(Query().titulo == titulo)
       
#-------------------------------------------------------------

app = Flask(__name__)

dao = DAO()

senha = '1234'

splitter = '/./'
splitter2 = '/;/'

#-------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    titulo = request.args.get('titulo')
    produtos = dao.buscar(titulo)
    return render_template('buscar.html', produtos=produtos)

@app.route('/passeios')
def passeios():
    produtos = dao.listar_por_tipo('passeio')
    return render_template('passeios.html', produtos=produtos)

@app.route('/pacotes')
def pacotes():
    produtos = dao.listar_por_tipo('pacote')
    return render_template('pacotes.html', produtos=produtos)

@app.route('/insert', methods=['POST'])
def inserir_produto():
    tipo = str(request.form.get('tipo'))
    titulo = request.form.get('titulo')
    localizacao = request.form.get('localizacao')
    resumo = request.form.get('resumo')
    descricao = request.form.get('descricao')
    incluso = request.form.get('incluso')
    dicas = request.form.get('dicas')
    observacoes = request.form.get('observacoes')
    precos = request.form.get('precos')
    midias = request.form.get('midias')
    numero_diarias = int(request.form.get('numero_diarias'))
    hospedagem = request.form.get('hospedagem')
    roteiro = request.form.get('roteiro')
    disponivel = request.form.get('disponivel')
    data_de_saida = request.form.get('data_de_saida')
    limite_vagas = int(request.form.get('limite_vagas'))
    dao.inserir(Produto(tipo, titulo, localizacao, resumo, descricao, incluso, dicas, observacoes, precos, midias, numero_diarias, hospedagem, roteiro, disponivel, data_de_saida, limite_vagas))
    return redirect(url_for('index'))

@app.route('/edit', methods=['GET'])
def editar_produto():
    auth = request.args.get('auth')
    if auth == senha:
        titulo = request.args.get('titulo')
        produto = dao.buscar(titulo)
        if len(produto) > 0:
            return render_template('edit.html', produto=produto[0])
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/update', methods=['GET', 'POST'])
def update():
    titulo = request.args.get('titulo')
    tipo = request.form.get('tipo')
    localizacao = request.form.get('localizacao')
    resumo = request.form.get('resumo')
    descricao = request.form.get('descricao')
    incluso = request.form.get('incluso')
    dicas = request.form.get('dicas')
    observacoes = request.form.get('observacoes')
    precos = request.form.get('precos')
    midias = request.form.get('midias')
    numero_diarias = int(request.form.get('numero_diarias'))
    hospedagem = request.form.get('hospedagem')
    roteiro = request.form.get('roteiro')
    disponivel = request.form.get('disponivel')
    data_de_saida = request.form.get('data_de_saida')
    limite_vagas = int(request.form.get('limite_vagas'))
    dao.deletar(titulo)
    dao.inserir(Produto(tipo, titulo, localizacao, resumo, descricao, incluso, dicas, observacoes, precos, midias, numero_diarias, hospedagem, roteiro, disponivel, data_de_saida, limite_vagas))
    return redirect(url_for('index'))

@app.route('/delete', methods=['GET'])
def deletar_produto():
    titulo = request.args.get('titulo')
    dao.deletar(titulo)
    return redirect(url_for('index'))

@app.route('/show', methods=['GET'])
def show():
    titulo = request.args.get('titulo')
    produto =  dao.buscar(titulo)
    if len(produto) > 0:
        return render_template('show.html', produto=produto[0])
    else:
        return render_template('index.html')
    
@app.route('/adm', methods=['GET'])
def adm():
    auth = request.args.get('auth')
    if auth == senha:
        return render_template('adm.html', produtos=dao.listar(), senha=auth)
    else:
        return redirect(url_for('index'))