from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.board_game import BoardGame
import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

board_game_blueprint = Blueprint("board_game", __name__)

# @board_game_blueprint.route('/')
# def reroute():
#     return redirect('/inventory')

@board_game_blueprint.route('/inventory')
def show_inventory():
    board_games = board_game_repository.select_all()
    return render_template('board_games/index.html', board_games=board_games)

@board_game_blueprint.route('/inventory/<int:id>')
def show_details(id):
    board_game = board_game_repository.select(id)
    return render_template('board_games/show.html', board_game=board_game)