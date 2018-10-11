from flask import Blueprint

medical = Blueprint('medical', __name__)

from . import index