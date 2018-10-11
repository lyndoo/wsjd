from flask import Blueprint

hairdressing = Blueprint('hairdressing', __name__)

from . import index