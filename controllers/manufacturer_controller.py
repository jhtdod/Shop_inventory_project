from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturer", __name__)