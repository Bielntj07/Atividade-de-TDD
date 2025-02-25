dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ], 
        "professores":[]}

class AlunoNaoEncontrado(Exception):
    pass

class AlunoJaRegistrado(Exception):
    pass

class AlunoSemNome(Exception):
    pass

class ProfessorNaoEncontrado(Exception):
    pass

class ProfessorJaRegistrado(Exception):
    pass

class ProfessorSemNome(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def deleta_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            dados['alunos'].remove(dicionario)
            return 'ok'
    raise AlunoNaoEncontrado

def edita_por_id(novoNome,id_aluno):
    dic_aluno = aluno_por_id(id_aluno)
    if len(novoNome) <= 0:
        raise AlunoSemNome
    dados['alunos'].append(dict)
    dic_aluno['nome'] = novoNome['nome']
    return 'editado'

def adiciona_aluno(dict):
    lista_alunos = dados['alunos']
    for i in lista_alunos:
        if i['id'] == dict['id']:
            raise AlunoJaRegistrado
    if 'nome' not in dict.keys() or len(dict['nome']) <= 0:
        raise AlunoSemNome
    dados['alunos'].append(dict)
    

def lista_alunos():
    return dados["alunos"]

def apaga_tudo():
    dados['alunos'] = []
    dados['professores'] = []

def lista_professores():
    return dados["professores"]

def adiciona_professor(dict):
    lista_professores = dados['professores']
    for i in lista_professores:
        if i['id'] == dict['id']:
            raise ProfessorJaRegistrado
    if 'nome' not in dict.keys() or len(dict['nome']) <= 0:
        raise ProfessorSemNome
    dados['professores'].append(dict)

def professor_por_id(id_professor):
    lista_professores = dados['professores']
    for dicionario in lista_professores:
        if dicionario['id'] == id_professor:
            return dicionario
    raise ProfessorNaoEncontrado

def edita_por_id_professor(novoNome,id_professor):
    dic_professor = professor_por_id(id_professor)
    if len(novoNome) <= 0:
        raise ProfessorSemNome
    dados['professores'].append(dict)
    dic_professor['nome'] = novoNome['nome']
    return 'editado'

def deleta_por_id_professores(id_prof):
    lista_professores = dados['professores']
    for dicionario in lista_professores:
        if dicionario['id'] == id_prof:
            dados['professores'].remove(dicionario)
            return 'ok'
    raise ProfessorNaoEncontrado