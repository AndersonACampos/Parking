import sqlite3

path_db = 'db/ParkDB.s3db'


def buscar_todos():
    db = sqlite3.connect(path_db)
    cur = db.cursor()
    cur.execute("select ticket_id Ticket, Entrada, coalesce(saida, '') Saida, coalesce(valor,'') Valor, Placa, Carro, Cor, coalesce(tempo,'') Tempo, case when pago = 0 then 'Não' else 'Sim' end Pago from ticket")
    dados = cur.fetchall()
    cur1 = db.cursor()
    cur1.execute(f"PRAGMA table_info(ticket)")
    colunas = [linha[1] for linha in cur1.fetchall()]
    db.close()
    return dados, colunas