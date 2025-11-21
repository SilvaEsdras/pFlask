# 1. Importar request, redirect e flash
from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO

app = Flask(__name__)

# 2. Adicionar a chave secreta para usar o 'flash'
app.secret_key = "uma_chave_muito_secreta_e_unica" 

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista_alunos=lista)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)

@app.route('/aluno/salvar/', methods=['POST'])
@app.route('/aluno/salvar/<int:id>', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade)
    if result["status"] == "ok":
        flash(f"Aluno '{nome}' salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/aluno')

@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista_professores=lista)

@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=None)

@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form.html', professor=professor)

@app.route('/professor/salvar/', methods=['POST'])
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina) 
    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/professor')

@app.route("/professor/remover/<int:id>")
def remover_professor(id):
    dao = ProfessorDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/professor')


@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista_cursos=lista)

@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)

@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = CursoDAO()
    curso = dao.buscar_por_id(id)
    return render_template('curso/form.html', curso=curso)

@app.route('/curso/salvar/', methods=['POST'])
@app.route('/curso/salvar/<int:id>', methods=['POST'])
def salvar_curso(id=None):
    nome = request.form['nome']
    duracao = request.form['duracao_meses'] 
    dao = CursoDAO()
    result = dao.salvar(id, nome, duracao) 
    if result["status"] == "ok":
        flash(f"Curso '{nome}' salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/curso')

@app.route("/curso/remover/<int:id>")
def remover_curso(id):
    dao = CursoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/curso')


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista_turmas = dao.listar()
    return render_template('turma/lista.html', lista_turmas=lista_turmas)

@app.route('/turma/form')
def form_turma():
    # Buscamos as listas para popular os <select>
    lista_professores = ProfessorDAO().listar()
    lista_cursos = CursoDAO().listar()
    return render_template('turma/form.html',
                           turma=None,
                           lista_professores=lista_professores,
                           lista_cursos=lista_cursos)

@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    # Buscamos as listas para os <select>
    lista_professores = ProfessorDAO().listar()
    lista_cursos = CursoDAO().listar()
    
    # Buscamos os dados da turma específica
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    
    return render_template('turma/form.html',
                           turma=turma,
                           lista_professores=lista_professores,
                           lista_cursos=lista_cursos)

@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):
    # Coletamos os dados do formulário
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']
    
    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso_id, professor_id)
    
    if resultado["status"] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
        
    return redirect('/turma')

@app.route("/turma/remover/<int:id>")
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')


@app.route('/matricula')
def listar_matricula():
    dao = MatriculaDAO()
    lista_matriculas = dao.listar()
    return render_template('matricula/lista.html', lista_matriculas=lista_matriculas)

@app.route('/matricula/form')
def form_matricula():
    # Buscar listas para os selects
    lista_alunos = AlunoDAO().listar()
    # A listagem de turmas do TurmaDAO já traz informações ricas (curso, prof)
    lista_turmas = TurmaDAO().listar() 
    
    return render_template('matricula/form.html', 
                           matricula=None,
                           lista_alunos=lista_alunos,
                           lista_turmas=lista_turmas)

@app.route('/matricula/editar/<int:id>')
def editar_matricula(id):
    lista_alunos = AlunoDAO().listar()
    lista_turmas = TurmaDAO().listar()
    
    dao = MatriculaDAO()
    matricula = dao.buscar_por_id(id)
    
    return render_template('matricula/form.html', 
                           matricula=matricula,
                           lista_alunos=lista_alunos,
                           lista_turmas=lista_turmas)

@app.route('/matricula/salvar/', methods=['POST'])
@app.route('/matricula/salvar/<int:id>', methods=['POST'])
def salvar_matricula(id=None):
    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    
    dao = MatriculaDAO()
    resultado = dao.salvar(id, aluno_id, turma_id)
    
    if resultado["status"] == "ok":
        flash("Matrícula salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
        
    return redirect('/matricula')

@app.route("/matricula/remover/<int:id>")
def remover_matricula(id):
    dao = MatriculaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Matrícula removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/matricula')


@app.route('/sobre')
def sobre_sistema():
    return render_template('sobre.html')

@app.route('/ajuda')
def ajuda_sistema():
    return render_template('ajuda.html')

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio')
def desafio_formulario():
    return render_template('desafio/formulario.html')

@app.route('/desafio/enviar', methods=['POST'])
def desafio_enviar():
    dados = {
        "nome": request.form['nome'],
        "data_nascimento": request.form['data_nascimento'],
        "cpf": request.form['cpf'],
        "nome_mae": request.form['nome_mae']
    }
    return render_template('desafio/resultado.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)