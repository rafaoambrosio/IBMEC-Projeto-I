from tinydb import TinyDB, Query

class DAO:
    def __init__(self) -> None:
        self.db = TinyDB('dao.json')
        self.estudantes = self.db.table('estudantes')
        self.cursos = self.db.table('cursos')
        self.professores = self.db.table('professores')
        self.query = Query()

    def listar(self, tb):
        if tb == "e":
            return self.estudantes.all()
        elif tb == "c":
            return self.cursos.all()
        elif tb == "p":
            return self.professores.all()
        else:
            return self.db.all()
        
    def inserir(self, tb, colunas, valores):
        dictInserir = {}
        if tb == "e":
            for i in range(len(colunas)):
                dictInserir[colunas[i]] = valores[i]
            self.estudantes.insert(dictInserir)
        elif tb == "c":
            for i in range(len(colunas)):
                dictInserir[colunas[i]] = valores[i]
            self.cursos.insert(dictInserir)
        elif tb == "p":
            for i in range(len(colunas)):
                dictInserir[colunas[i]] = valores[i]
            self.professores.insert(dictInserir)
        else:
            for i in range(len(colunas)):
                dictInserir[colunas[i]] = valores[i]
            self.db.insert(dictInserir)
    
    def buscar(self, tb, coluna, valor):
        if tb == "e":
            return self.estudantes.search(self.query[coluna] == valor)
        elif tb == "c":
            return self.cursos.search(self.query[coluna] == valor)
        elif tb == "p":
            return self.professores.search(self.query[coluna] == valor)
        else:
            return self.db.search(self.query[coluna] == valor)
    
    def atualizar(self, tb, colunabusca, valorbusca, colunamod, valormod):
        if tb == "e":
            self.estudantes.update({colunamod: valormod}, self.query[colunabusca] == valorbusca)
        elif tb == "c":
            self.cursos.update({colunamod: valormod}, self.query[colunabusca] == valorbusca)
        elif tb == "p":
            self.professores.update({colunamod: valormod}, self.query[colunabusca] == valorbusca)
        else:
            self.db.update({colunamod: valormod}, self.query[colunabusca] == valorbusca)
    
    def deletar(self, tb, coluna, valor):
        if tb == "e":
            self.estudantes.remove(self.query[coluna] == valor)
        elif tb == "c":
            self.cursos.remove(self.query[coluna] == valor)
        elif tb == "p":
            self.professores.remove(self.query[coluna] == valor)
        else:
            pass