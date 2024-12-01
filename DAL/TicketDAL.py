import sqlite3

PATH_DB = 'db/ParkDB.s3db'


def buscar_todos():
    con = sqlite3.connect(PATH_DB)
    cur = con.cursor()
    cur.execute("select ticket_id Ticket, Entrada, coalesce(saida,'') Saida, coalesce(valor,'') Valor, Placa, Carro, Cor, coalesce(tempo,'') Tempo, case when pago = 0 then 'Não' else 'Sim' end Pago from ticket")
    dados = cur.fetchall()
    cur1 = con.cursor()
    cur1.execute(f"PRAGMA table_info(ticket)")
    colunas = [linha[1] for linha in cur1.fetchall()]
    con.close()
    return dados, colunas


def pagar(id, saida, tempo, valor):
    con = sqlite3.connect(PATH_DB)
    cur = con.cursor()
    query = f"""
                update 
                    ticket
                set 
                    saida = {saida},
                    valor = {valor},
                    tempo = {tempo},
                    pago = 1
                where 
                    id = {id}
            """
    cur.execute(query)
    con.commit()
    ret = cur.fetchone()
    con.close()
    return ret