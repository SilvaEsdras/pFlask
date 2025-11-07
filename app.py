from flask import Flask, render_template, request # Verificar se 'request' já foi importado
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO


app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista_alunos=lista)

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista_professores=lista)

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista_cursos=lista)

@app.route('/sobre')
def sobre_sistema():
    return render_template('sobre.html')

@app.route('/ajuda')
def ajuda_sistema():
    return render_template('ajuda.html')

# --- INÍCIO DA SOLUÇÃO DO EXERCÍCIO ---
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
# --- FIM DA SOLUÇÃO DO EXERCÍCIO ---


# --- INÍCIO DA SOLUÇÃO DO DESAFIO [cite: 118] ---

# Rota para EXIBIR o formulário de cadastro
@app.route('/desafio')
def desafio_formulario():
    return render_template('desafio/formulario.html')

# Rota para RECEBER os dados do formulário via POST
@app.route('/desafio/enviar', methods=['POST'])
def desafio_enviar():
    # Coleta todos os dados do formulário [cite: 119-123]
    dados = {
        "nome": request.form['nome'],
        "data_nascimento": request.form['data_nascimento'],
        "cpf": request.form['cpf'],
        "nome_mae": request.form['nome_mae']
    }
    # Envia os dados coletados para o template de resultado [cite: 124]
    return render_template('desafio/resultado.html', dados=dados)

# --- FIM DA SOLUÇÃO DO DESAFIO ---


if __name__ == '__main__':
    app.run(debug=True)