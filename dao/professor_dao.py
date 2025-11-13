# Em: dao/professor_dao.py

from dao.db_config import get_connection

class ProfessorDAO:
    # 1. CORREÇÃO: Remova 'cidade' do SELECT
    sqlSelect = 'SELECT id, nome, disciplina FROM professor'

    # 2. CORREÇÃO: Remova 'cidade' dos parâmetros e das queries
    def salvar(self, id, nome, disciplina): # Removido 'cidade' daqui
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id: # UPDATE
                cursor.execute(
                    # Removido 'cidade = %s'
                    'UPDATE professor SET nome = %s, disciplina = %s WHERE id = %s',
                    (nome, disciplina, id) # Removido 'cidade' daqui
                )
            else: # INSERT
                cursor.execute(
                    # Removido 'cidade' (a query original já estava correta)
                    'INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', 
                    (nome, disciplina)
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

    # 3. CORREÇÃO: Remova 'cidade' do buscar_por_id
    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        # Removida 'cidade' do SELECT
        cursor.execute('SELECT id, nome, disciplina FROM professor WHERE id = %s', (id,)) 
        registro = cursor.fetchone() 
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM professor WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()