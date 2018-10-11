from flask import render_template
from . import note


@note.route('/')
def index():
    return render_template('note/index.html')