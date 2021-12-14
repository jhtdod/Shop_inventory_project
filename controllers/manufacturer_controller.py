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

@manufacturer_blueprint.route('/manufacturer/edit/<int:id>')
def show_edit(id):
    manufacturer = manufacturer_repository.select(id)
    board_games = board_game_repository.select_all()
    return render_template('/manufacturer/edit.html', board_games=board_games, manufacturer=manufacturer)

@manufacturer_blueprint.route('/manufacturer/edit/<int:id>', methods=['POST'])
def edit_game(id):
    name = request.form["name"]
    contact_details = request.form['contact_details']
    updated_manufacturer = Manufacturer(name, contact_details, id)
    manufacturer_repository.update(updated_manufacturer)
    return redirect('/manufacturer')

@board_game_blueprint.route('/inventory/delete/<int:id>')
def delete_game(id):
    board_game_repository.delete(id)
    return redirect('/inventory')