from dao.db_config import get_connection

class AlunoDAO:
    sqlSelect = 'SELECT id, nome, idade, cidade FROM aluno'
    
    def salvar(self, id, nome, idade, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id: # Se o ID existe, ATUALIZA (UPDATE)
                cursor.execute(
                    'UPDATE aluno SET nome = %s, idade = %s, cidade = %s WHERE id = %s',
                    (nome, idade, cidade, id)
                )
            else: # Se o ID é None, INSERE (INSERT)
                cursor.execute(
                    'INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)',
                    (nome, idade, cidade)
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

    # Novo método para BUSCAR POR ID
    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        # Usamos (id,) para passar a tupla corretamente
        cursor.execute('SELECT id, nome, idade, cidade FROM aluno WHERE id = %s', (id,)) 
        registro = cursor.fetchone() # Retorna um único registro
        conn.close()
        return registro

    # Novo método para REMOVER
    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM aluno WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()