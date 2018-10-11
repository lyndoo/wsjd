from flask import render_template
from . import map

@map.route('/<string:key>')
def index(key):
    return render_template('/mapindex.html', mkey=key)