# Em: dao/curso_dao.py

from dao.db_config import get_connection

class CursoDAO:
    # 1. CORREÇÃO: Selecione apenas as colunas que existem
    sqlSelect = 'SELECT id, nome_curso, duracao FROM curso'
    
    # 2. CORREÇÃO: O form envia 'nome' e 'duracao_meses', 
    # mas o DB espera 'nome_curso' e 'duracao'
    def salvar(self, id, nome, duracao): 
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id: # UPDATE
                cursor.execute(
                    # Use 'nome_curso' e 'duracao'
                    'UPDATE curso SET nome_curso = %s, duracao = %s WHERE id = %s',
                    (nome, duracao, id)
                )
            else: # INSERT
                cursor.execute(
                    # Use 'nome_curso' e 'duracao'
                    'INSERT INTO curso (nome_curso, duracao) VALUES (%s, %s)',
                    (nome, duracao)
                )
            
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    # 3. CORREÇÃO: Ajuste o buscar_por_id
    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        # Selecione apenas as colunas que existem
        cursor.execute('SELECT id, nome_curso, duracao FROM curso WHERE id = %s', (id,)) 
        registro = cursor.fetchone() 
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM curso WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()