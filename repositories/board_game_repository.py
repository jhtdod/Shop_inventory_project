from db.run_sql import run_sql

from models.board_game import BoardGame

def select_all():
    board_games = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        board_game = BoardGame(row['name'], row['description'], row['quantity'], row['buying_cost'], row['selling_price'], row['manufacturer'], row['id'])
        board_games.append(board_game)
    return board_games