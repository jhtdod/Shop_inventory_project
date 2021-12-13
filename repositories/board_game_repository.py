from db.run_sql import run_sql
from models.board_game import BoardGame
import repositories.manufacturer_repository as manufacturer_repository 

def save(board_game):
    sql = "INSERT INTO board_games (name, description, quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [board_game.name, board_game.description, board_game.quantity, board_game.buying_cost, board_game.selling_price, board_game.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie.id = id

def select_all():
    board_games = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)
    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        board_game = BoardGame(row['name'], row['description'], row['quantity'], row['buying_cost'], row['selling_price'], manufacturer, row['id'])
        board_games.append(board_game)
    return board_games

def select(id):
    board_game = None
    sql = "SELECT * FROM board_games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        board_game = BoardGame(row['name'], row['description'], row['quantity'], row['buying_cost'], row['selling_price'], manufacturer, row['id'])
    return board_game

def delete_all():
    sql = "DELETE FROM board_games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM board_games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(board_game):
    sql = "UPDATE board_games SET (name, description, quantity, buying_cost, selling_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [board_game.name, board_game.description, board_game.quantity, board_game.buying_cost, board_game.selling_price, board_game.manufacturer.id, board_game.id]
    run_sql(sql, values)
