from dao.db_config import get_connection

class AlunoDAO: 
    sqlSelect = 'SELECT id, nome, idade, cidade FROM aluno'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista