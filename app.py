# 1. Importar request, redirect e flash
from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

# 2. Adicionar a chave secreta para usar o 'flash'
app.secret_key = "uma_chave_muito_secreta_e_unica" 

@app.route('/')
def home():
    return render_template('index.html') 

# --- ROTAS DE ALUNO ---

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista_alunos=lista)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

# Rota de EDIÇÃO de Aluno
@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id) # Busca o aluno no DB
    return render_template('aluno/form.html', aluno=aluno) # Envia para o form

# Rotas de SALVAR (INSERT e UPDATE)
@app.route('/aluno/salvar/', methods=['POST']) # Rota para INSERIR (id=None)
@app.route('/aluno/salvar/<int:id>', methods=['POST']) # Rota para ATUALIZAR (id informado)
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

# Rota de REMOVER Aluno
@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')

# --- ROTAS DE PROFESSOR (Exercício) ---

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

# 6. Rota para salvar um novo professor
@app.route('/professor/salvar/', methods=['POST'])
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    # Coleta os dados do formulário (Nome, Disciplina)
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    # 1. CORREÇÃO: Remova a linha abaixo
    # cidade = request.form['cidade'] 
    
    dao = ProfessorDAO()
    # 2. CORREÇÃO: Remova 'cidade' da chamada do método
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

# --- ROTAS DE CURSO (Exercício) ---

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
    # Coleta os dados (Nome, Duracao)
    nome = request.form['nome']
    # 1. CORREÇÃO: O form envia 'duracao_meses', o DB espera 'duracao'
    duracao = request.form['duracao_meses'] 
    
    # 2. CORREÇÃO: Remova a linha abaixo, pois a coluna 'coordenador' não existe
    # coordenador = request.form['coordenador'] 
    
    dao = CursoDAO()
    # 3. CORREÇÃO: Passe 'duracao', e não 'coordenador'
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

# --- Rotas dos exercícios anteriores ---

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