# 1. Importar request, redirect e flash
from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

# 2. Adicionar a chave secreta para usar o 'flash'
app.secret_key = "uma_chave_muito_secreta_e_unica" # [cite: 194]

@app.route('/')
def home():
    return render_template('index.html') 

# --- ROTAS DE ALUNO ---

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista_alunos=lista)

# 3. Rota para exibir o formulário de aluno [cite: 151]
@app.route('/aluno/form')
def form_aluno():
    # Passamos 'aluno=None' para o template usar o mesmo formulário para cadastro
    return render_template('aluno/form.html', aluno=None)

# 4. Rota para salvar um novo aluno (via POST) [cite: 181]
@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno(id=None):
    # Coleta os dados do formulário
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    
    dao = AlunoDAO()
    # Chama o método salvar do DAO
    result = dao.salvar(id, nome, idade, cidade)

    # Verifica o resultado e envia uma mensagem flash
    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success") # [cite: 181]
    else:
        flash(result["mensagem"], "danger") # [cite: 181]

    # Redireciona de volta para a lista de alunos
    return redirect('/aluno') # [cite: 181]

# --- ROTAS DE PROFESSOR (Exercício) ---

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista_professores=lista)

# 5. Rota para exibir o formulário de professor
@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=None)

# 6. Rota para salvar um novo professor
@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor(id=None):
    # Coleta os dados do formulário (Nome, Disciplina, Cidade)
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    cidade = request.form['cidade']
    
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina, cidade)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')

# --- ROTAS DE CURSO (Exercício) ---

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista_cursos=lista)

# 7. Rota para exibir o formulário de curso
@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)

# 8. Rota para salvar um novo curso
@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso(id=None):
    # Coleta os dados (Nome, Duracao, Coordenador)
    nome = request.form['nome']
    duracao_meses = request.form['duracao_meses']
    coordenador = request.form['coordenador']
    
    dao = CursoDAO()
    result = dao.salvar(id, nome, duracao_meses, coordenador)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

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