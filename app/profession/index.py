from flask import render_template
from . import profession


@profession.route('/')
def index():
    return render_template('profession/index.html')

