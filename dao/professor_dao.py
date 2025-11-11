from dao.db_config import get_connection

class ProfessorDAO:
    # Assumindo que o SELECT * retorna (id, nome, disciplina, cidade)
    sqlSelect = 'SELECT * FROM professor'

    # Método Salvar (Inserir) para Professor
    def salvar(self, id, nome, disciplina, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id is None:
                cursor.execute(
                    'INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', (nome, disciplina)
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