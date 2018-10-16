from flask import Flask
from flask_cache import Cache
from flask import render_template
from flask import request
from config import Config
import os


App = Flask(__name__)
App.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
cache = Cache(App, config={'CACHE_TYPE': 'simple'})

if not os.path.exists(Config.UPLOAD_FOLDER):
    os.mkdir(Config.UPLOAD_FOLDER)
App.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
from app.sanitation import sanitation
from app.report import report
from app.penalty import penalty
from app.profession import profession
from app.public import public
from app.note import note
from app.hairdressing import hairdressing
from app.medical import medical
from app.map import map
from app.out import out
from app.law import law
from app.scan import scan
from app.admin import admin
App.register_blueprint(report, url_prefix='/report')
App.register_blueprint(penalty, url_prefix='/penalty')
App.register_blueprint(profession, url_prefix='/profession')
App.register_blueprint(sanitation, url_prefix='/sanitation')
App.register_blueprint(public, url_prefix='/public')
App.register_blueprint(note, url_prefix='/note')
App.register_blueprint(hairdressing, url_prefix='/hairdressing')
App.register_blueprint(medical, url_prefix='/medical')
App.register_blueprint(map, url_prefix='/map')
App.register_blueprint(out, url_prefix='/out')
App.register_blueprint(law, url_prefix='/law')
App.register_blueprint(scan, url_prefix='/scan')
App.register_blueprint(admin, url_prefix='/admin')


@App.route('/')
def home():
    return render_template('home.html')

@App.route('/MP_verify_9jYKdFS9fxfWUcUI.txt')
def wxtxt():
    return '9jYKdFS9fxfWUcUI'
    #return render_template('MP_verify_9jYKdFS9fxfWUcUI.txt')

@App.route('/home2')
def home2():
    return render_template('home2.html')


def make_cache_key(*args, **kwargs):
    """Dynamic creation the request url."""
    path = request.path
    args = str(hash(frozenset(request.args.items())))
    return (path + args).encode('utf-8')


if __name__ == '__main__':
    #App.run()
    App.run(host='0.0.0.0', port=8080)
