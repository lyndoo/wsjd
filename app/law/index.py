from flask import render_template
from . import law

@law.route('/')
def index():
    return render_template('law/index.html')