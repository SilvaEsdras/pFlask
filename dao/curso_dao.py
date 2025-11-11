from dao.db_config import get_connection

class CursoDAO:
    # Assumindo que o SELECT * retorna (id, nome, duracao_meses, coordenador)
    sqlSelect = 'SELECT * FROM curso'
    
    # Método Salvar (Inserir) para Curso
    def salvar(self, id, nome_curso, duracao_meses, coordenador):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id is None:
                cursor.execute(
                    'INSERT INTO curso (nome_curso, duracao_meses, coordenador) VALUES (%s, %s, %s)',
                    (nome_curso, duracao_meses, coordenador)
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