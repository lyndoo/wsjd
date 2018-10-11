from flask import render_template
from . import sanitation


@sanitation.route('/')
def index():
    return render_template('sanitation/index.html')


@sanitation.route('/sn/')
def listsn():
    return render_template('sanitation/sn.html')


@sanitation.route('/sw/')
def listsw():
    return render_template('sanitation/sw.html')

