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