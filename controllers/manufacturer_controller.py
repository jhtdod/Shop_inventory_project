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

@manufacturer_blueprint.route('/manufacturer/add')
def show_add_form():
    board_games = board_game_repository.select_all()
    return render_template('manufacturer/new.html', board_games=board_games)

@manufacturer_blueprint.route('/manufacturer/add', methods=['POST'])
def add_manufacturer():
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    new_manufacturer = Manufacturer(name, contact_details)
    manufacturer_repository.save(new_manufacturer)
    return redirect('/manufacturer')

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