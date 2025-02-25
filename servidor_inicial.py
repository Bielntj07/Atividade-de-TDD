
from flask import Flask, request

import model_aluno_professor as model

app = Flask(__name__) 

from flask_cors import CORS
CORS(app)

		
@app.route("/") 
def hello():
        print("rodei mesmo") 
        return "Hello World!"

'''Rode esse arquivo .py para que o programa
disponiblize as URLs abaixo'''


'''atende em /alunos, verbo GET
pode acessar http://localhost:5002/alunos
no navegador'''
@app.route("/alunos", methods=["GET"])
def alunos():
    print("lista de todos os alunos")
    return model.lista_alunos()
'''
Quando o usuário acessa a URL, o flask roda
a função correspondente e devolve o return 
para o usuário. O usuário baixa o return como
um arquivo txt especial, um json
'''


'''
pode acessar http://localhost:5002/alunos/15
             http://localhost:5002/alunos/29
no navegador
'''
@app.route("/alunos/<int:nAluno>", methods=["GET"]) 
def alunoPorId(nAluno):
    try:
        return model.aluno_por_id(nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)
# 1) /alunos/<int:nAluno>  e passa nAluno no def  
# para pegar o nro na URL    
# 2)  methods=["GET"] para definir o verbo
# 3)  return ({'erro':'aluno nao encontrado'},400) 
#     diz qual o arquivo retornado (o dicionario)
#     e tb o codigo de status (400)
# 4)  Se vc nao disser o cod status, vai "200 OK" por padrao, como em         
#     return model.aluno_por_id(nAluno)

# COD STATUS??
# É um código de 3 digitos que diz se a conexao deu certo
# 404 é o mais clássico, significa que a página que você
# está procurando não foi encontrada
# 200 significa que tudo deu certo.

# Pra ver o cód status, pode ser útil baixar o insomnia
# https://insomnia.rest/download
# (não precisa criar conta no aplicativo!)
# instruções adicionais sobre o imsomnia:
# https://docs.google.com/document/d/1IOcJJq4eSdM1IhM3ji95mu2FF1xjz-hXbX1730WWtMk/edit?usp=sharing


'''atende em /alunos, verbo POST'''
@app.route("/alunos", methods=["POST"])
def cria_aluno():
    dict = request.json
    try:
        dict['id'] = int (dict['id'])
        model.adiciona_aluno(dict)
        return model.lista_alunos()
    except model.AlunoJaRegistrado:
        return ({"erro":'id ja utilizada'}, 400)
    except model.AlunoSemNome:
        return ({"erro":'aluno sem nome'}, 400)
# para criar um aluno, precisamos enviar um dicionário
# (talvez vc queria ver instruções sobre o imsomnia)
# https://docs.google.com/document/d/1IOcJJq4eSdM1IhM3ji95mu2FF1xjz-hXbX1730WWtMk/edit?usp=sharing


#Na URL /reseta, apagaremos a lista de alunos e professores 
# (essa URL atende o verbo POST e o DELETE).
@app.route("/reseta", methods=["POST","DELETE"])
def reseta():
    model.apaga_tudo()
    return "resetado" #poderia ser return dados
    #tive que retornar ALGUMA COISA, pro usuario receber algo
    #o flask nao deixa uma funcao de URL nao ter retorno

@app.route("/alunos/<int:nAluno>", methods=["DELETE"])
def deletaPorId(nAluno):
    try:
        return model.deleta_por_id(nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)

@app.route("/alunos/<int:nAluno>", methods=["PUT"])
def editaPorId(nAluno):
    dict = request.json
    if 'nome' not in dict:
        return ({"erro":'aluno sem nome'}, 400)
    try:
        return model.edita_por_id(dict ,nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)
    except model.AlunoSemNome:
        return ({"erro":'aluno sem nome'}, 400)
# blza, agora vamos ver os testes
# no arquivo runtests. Se não baixou, baixe ele

# Ah, se quiser um material extra de flask, tem aqui
# https://docs.google.com/presentation/d/1kjwCVi9Y0MIh9UNziGnql7CoJh7TdYZNH9EKFCWS9rE/edit#slide=id.p1

@app.route("/professores", methods=["GET"])
def professores():
    print("lista de todos os professores")
    return model.lista_professores()

@app.route("/professores", methods=["POST"])
def cria_professor():
    dict = request.json
    try:
        dict['id'] = int (dict['id'])
        model.adiciona_professor(dict)
        return model.lista_professores()
    except model.ProfessorJaRegistrado:
        return ({"erro":'id ja utilizada'}, 400)
    except model.ProfessorSemNome:
        return ({"erro":'professor sem nome'}, 400)

@app.route("/professores/<int:nProf>", methods=["GET"]) 
def professorPorId(nProf):
    try:
        return model.professor_por_id(nProf)
    except model.ProfessorNaoEncontrado:
        return ( {"erro":'professor nao encontrado'}, 400)

@app.route("/professores/<int:nProf>", methods=["PUT"])
def editaPorIdProfessor(nProf):
    dict = request.json
    if 'nome' not in dict:
        return ({"erro":'professor sem nome'}, 400)
    try:
        return model.edita_por_id_professor(dict,nProf)
    except model.ProfessorNaoEncontrado:
        return ( {"erro":'professor nao encontrado'}, 400)
    except model.ProfessorSemNome:
        return ({"erro":'professor sem nome'}, 400)

@app.route("/professores/<int:nProf>", methods=["DELETE"])
def deletaPorIdProf(nProf):
    try:
        return model.deleta_por_id_professores(nProf)
    except model.ProfessorNaoEncontrado:
        return ( {"erro":'professor nao encontrado'}, 400)

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)