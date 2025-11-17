from dao.db_config import get_connection

class TurmaDAO:

    def listar(self):
        """ Lista todas as turmas com dados do curso e professor (JOIN) """
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query SQL com JOIN conforme o slide
        sql = """
            SELECT turma.id, turma.semestre, curso.nome_curso, professor.nome, professor.disciplina
            FROM turma
            JOIN curso ON turma.curso_id = curso.id
            JOIN professor ON turma.professor_id = professor.id 
            ORDER BY turma.id desc
        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso_id, professor_id):
        """ Salva (Insere ou Atualiza) uma turma """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id: # ATUALIZAR (UPDATE)
                cursor.execute(
                    """
                    UPDATE turma 
                    SET semestre = %s, curso_id = %s, professor_id = %s 
                    WHERE id = %s
                    """,
                    (semestre, curso_id, professor_id, id)
                )
            else: # INSERIR (INSERT)
                cursor.execute(
                    """
                    INSERT INTO turma (semestre, curso_id, professor_id) 
                    VALUES (%s, %s, %s)
                    """,
                    (semestre, curso_id, professor_id)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        """ Busca uma turma específica pelo ID """
        conn = get_connection()
        cursor = conn.cursor()
        # Query SQL para buscar a turma com seus IDs de chave estrangeira
        cursor.execute('SELECT id, semestre, curso_id, professor_id FROM turma WHERE id = %s', (id,))
        turma = cursor.fetchone()
        conn.close()
        return turma

    def remover(self, id):
        """ Remove uma turma pelo ID """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM turma WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()