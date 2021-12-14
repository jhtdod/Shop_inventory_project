from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.board_game import BoardGame
from models.manufacturer import Manufacturer
import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

board_game_blueprint = Blueprint("board_game", __name__)

@board_game_blueprint.route('/')
def split_view():
    board_games = board_game_repository.select_all()
    return render_template('index.html', board_games=board_games)

@board_game_blueprint.route('/inventory')
def show_inventory():
    board_games = board_game_repository.select_all()
    return render_template('board_games/index.html', board_games=board_games)

@board_game_blueprint.route('/inventory/<int:id>')
def show_details(id):
    board_game = board_game_repository.select(id)
    return render_template('board_games/show.html', board_game=board_game)

@board_game_blueprint.route('/inventory/add')
def show_add_form():
    manufacturers = manufacturer_repository.select_all()
    return render_template('board_games/new.html', manufacturers=manufacturers)

@board_game_blueprint.route('/inventory/add', methods=['POST'])
def add_game():
    name = request.form["name"]
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer'])
    new_game = BoardGame(name, description, quantity, buying_cost, selling_price, manufacturer)
    board_game_repository.save(new_game)
    return redirect('/inventory')

@board_game_blueprint.route('/inventory/edit/<int:id>')
def show_edit(id):
    board_game = board_game_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('/board_games/edit.html', board_game=board_game, manufacturers=manufacturers)

@board_game_blueprint.route('/inventory/edit/<int:id>', methods=['POST'])
def edit_game(id):
    name = request.form["name"]
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer'])
    updated_game = BoardGame(name, description, quantity, buying_cost, selling_price, manufacturer, id)
    board_game_repository.update(updated_game)
    return redirect('/inventory')

@board_game_blueprint.route('/inventory/delete/<int:id>')
def delete_game(id):
    board_game_repository.delete(id)
    return redirect('/inventory')