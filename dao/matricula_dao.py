from dao.db_config import get_connection

class MatriculaDAO:
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        # Query atualizada para buscar Professor e Disciplina através da Turma
        sql = """
            SELECT 
                m.id, 
                t.semestre, 
                a.nome, 
                c.nome_curso, 
                p.nome, 
                p.disciplina 
            FROM matricula m
            JOIN aluno a ON m.aluno_id = a.id
            JOIN turma t ON m.turma_id = t.id
            JOIN curso c ON m.curso_id = c.id
            JOIN professor p ON t.professor_id = p.id
            ORDER BY m.id DESC
        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Busca o curso_id associado à turma selecionada
            cursor.execute("SELECT curso_id FROM turma WHERE id = %s", (turma_id,))
            turma_row = cursor.fetchone()
            
            if not turma_row:
                return {"status": "erro", "mensagem": "Turma selecionada não encontrada."}
            
            curso_id = turma_row[0]

            if id: # Atualizar
                cursor.execute(
                    "UPDATE matricula SET aluno_id=%s, turma_id=%s, curso_id=%s WHERE id=%s", 
                    (aluno_id, turma_id, curso_id, id)
                )
            else: # Inserir
                cursor.execute(
                    "INSERT INTO matricula (aluno_id, turma_id, curso_id) VALUES (%s, %s, %s)", 
                    (aluno_id, turma_id, curso_id)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, aluno_id, turma_id FROM matricula WHERE id=%s", (id,))
        item = cursor.fetchone()
        conn.close()
        return item

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM matricula WHERE id=%s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()