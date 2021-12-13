from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.board_game import BoardGame
import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

board_game_blueprint = Blueprint("board_game", __name__)