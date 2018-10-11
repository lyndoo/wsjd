from flask import render_template
from . import hairdressing
from config import Config
from main import cache
import os
import xlrd
import json
from flask import request
from app.jsonResult import JsonResult

EXCEL_FILE = os.path.join(Config.APP_STATIC_DATA, '医疗美容.xls')  # 文件地址
PAGE_INDEX = 30


@cache.memoize(86400)
def loadInfo(name=None):
    workbook = xlrd.open_workbook(EXCEL_FILE)
    listName = ['name', 'no', 'address', 'lasttime', 'register', 'type', 'km', 'remark']
    convert_list = []
    sh = workbook.sheet_by_index(0)
    for rownum in range(2, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = dict()
        if name is None:
            for colnum in range(0, sh.ncols):
                single[listName[colnum]] = rowvalue[colnum]
            convert_list.append(single)
        else:
            if name in rowvalue[0]:
                for colnum in range(0, sh.ncols):
                    single[listName[colnum]] = rowvalue[colnum]
                convert_list.append(single)
    return convert_list


@hairdressing.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def index():
    return render_template('hairdressing/index.html')


@hairdressing.route('/', methods=['POST'])
def list():
    name = request.form.get('name')
    pageNo = int(request.form.get('pageNo'))
    #print(pageNo)
    datas = loadInfo(name)
    code = 0 if len(datas) <= (pageNo-1) * PAGE_INDEX + PAGE_INDEX else 1
    datas = datas[(pageNo-1) * PAGE_INDEX:(pageNo-1) * PAGE_INDEX + PAGE_INDEX]
    m = JsonResult(code, datas)
    return json.dumps(m, default=lambda obj: obj.__dict__, ensure_ascii=False)


@hairdressing.route('/detail/<string:name>')
def detail(name):
    datas = loadInfo()
    for i in datas:
        if i['name'] == name:
            info = i
            break
    #print(info)
    return render_template('hairdressing/detail.html', info=info)

