from tinydb import TinyDB, Query

class DAO:
    def __init__(self) -> None:
        self.db = TinyDB('db.json')
        self.query = Query()
    
    def listar(self):
        return self.db.all()

    def inserir(self, nome = "", email = "", idade = 0):
        if nome == "" or email == "" or idade == 0:
            self.db.insert({'nome':'Margrit', 'email': 'margrit@outlook.com', 'idade': 16})
            self.db.insert({'nome':'Guilherme', 'email': 'guilherme@yahoo.com', 'idade': 29})
            self.db.insert({'nome':'Ricardo', 'email': 'rick@mack.com.br', 'idade': 26})
            self.db.insert({'nome':'Veronica', 'email': 'v@gmail.com', 'idade': 28})
            self.db.insert({'nome':'Caroline', 'email': 'carol@egg.com', 'idade': 32})
            self.db.insert({'nome':'Tagliaferro', 'email': 'tagliaferro@yes.com', 'idade': 22})
        else:
            self.db.insert({'nome': nome, 'email': email, 'idade': idade})
            return "Dados inseridos com sucesso"

    def buscar(self, busca = ""):
        if busca == "":
            results = self.db.search(self.query.email == 'tagliaferro@yes.com')
        elif busca.isdigit():
            results = self.db.search(self.query.idade == int(busca))
        elif '@' in busca:
            results = self.db.search(self.query.email == busca)
        else:
            results = self.db.search(self.query.nome == busca)
        print(results, "\n")
        return results

    def atualizar(self, valor = "", busca = "", modobusca= "", modovalor = ""):
        if modovalor == "":
            self.db.update({'email': '@', 'idade': 78}, self.query.nome == 'Margrit')
        elif modovalor == "i":
            if modobusca== "":
                self.db.update({'idade': 78}, self.query.idade == busca)
            elif modobusca== "i":
                self.db.update({'idade': int(valor)}, self.query.idade == busca)
            elif modobusca== "e":
                self.db.update({'idade': int(valor)}, self.query.email == busca)
            elif modobusca== "n":
                self.db.update({'idade': int(valor)}, self.query.nome == busca)
        elif modovalor == "e":
            if modobusca== "":
                self.db.update({'email': '@'}, self.query.email == busca)
            elif modobusca== "i":
                self.db.update({'email': valor}, self.query.idade == busca)
            elif modobusca== "e":
                self.db.update({'email': valor}, self.query.email == busca)
            elif modobusca== "n":
                self.db.update({'email': valor}, self.query.nome == busca)
        elif modovalor == "n":
            if modobusca== "":
                self.db.update({'nome': 'Paulo'}, self.query.nome == busca)
            elif modobusca== "i":
                self.db.update({'nome': valor}, self.query.idade == busca)
            elif modobusca== "e":
                self.db.update({'nome': valor}, self.query.email == busca)
            elif modobusca== "n":
                self.db.update({'nome': valor}, self.query.nome == busca)
        else:
            self.db.update({'nome': valor}, self.query.nome == busca)
        

    def remover(self, modo="", valor="", operador=""):
        if modo == "":
            self.db.remove(self.query.idade < 18)
            self.db.remove(self.query.nome == 'Guilherme')
        elif modo == "i":
            if operador == "":
                self.db.remove(self.query.idade == valor)
            elif operador == "=":
                self.db.remove(self.query.idade == valor)
            elif operador == ">":
                self.db.remove(self.query.idade > valor)
            elif operador == "<":
                self.db.remove(self.query.idade < valor)
            elif operador == ">=":
                self.db.remove(self.query.idade >= valor)
            elif operador == "<=":
                self.db.remove(self.query.idade <= valor)
        elif modo == "e":
            self.db.remove(self.query.email == valor)
        elif modo == "n":
            self.db.remove(self.query.nome == valor)
        
            


#db.truncate()#remove todos os elementos do dicionário
#inserir()
#atualizar()
#buscar()
#remover()
#print(db.all())
