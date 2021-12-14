from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturer", __name__)

@manufacturer_blueprint.route('/manufacturers')
def show_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.html', manufacturers=manufacturers)


@manufacturer_blueprint.route('/manufacturer/<int:id>')
def show_details(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturer/show.html', manufacturer=manufacturer)

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