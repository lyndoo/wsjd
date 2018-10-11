from flask import render_template
from . import medical
from config import Config
import os
import xlrd
from app.jsonResult import JsonResult
from flask import request
import json
from main import cache

PAGE_INDEX = 30

def getTitleAndFileName(p):
    if p == 1:
        EXCEL_NAME = '1、检验机构信息.xls'
        titleName = '检验机构'
    elif p == 2:
        EXCEL_NAME = '2、门诊部信息.xls'
        titleName = '门诊部'
    elif p == 3:
        EXCEL_NAME = '3、社区卫生服务机构信息.xls'
        titleName = '社区卫生服务机构'
    elif p == 4:
        EXCEL_NAME = '4、卫生院信息.xls'
        titleName = '卫生院'
    elif p == 5:
        EXCEL_NAME = '5、医院类机构信息.xls'
        titleName = '医院'
    else:
        EXCEL_NAME = '6、诊所信息.xls'
        titleName = '诊所'

    return (EXCEL_NAME,titleName)


@medical.route('/')
def index():
    return render_template('medical/index.html')


@cache.memoize(86400)
def loadInfo(p, name=None):
    titleAndFile = getTitleAndFileName(p)
    EXCEL_FILE = os.path.join(Config.APP_STATIC_DATA + os.sep + '医疗机构', titleAndFile[0])  # 文件地址
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


@medical.route('/list/<int:p>', methods=['GET'])
def listPage(p):
    tf = getTitleAndFileName(p)
    return render_template('medical/list.html', p=p, titleName=tf[1])


@medical.route('/list/<int:p>', methods=['POST'])
def list(p):
    name = request.form.get('name')
    pageNo = int(request.form.get('pageNo'))
    #print(pageNo)
    datas = loadInfo(p, name)
    code = 0 if len(datas) <= (pageNo-1) * PAGE_INDEX + PAGE_INDEX else 1
    datas = datas[(pageNo-1) * PAGE_INDEX:(pageNo-1) * PAGE_INDEX + PAGE_INDEX]
    m = JsonResult(code, datas)
    return json.dumps(m, default=lambda obj: obj.__dict__, ensure_ascii=False)


@medical.route('/<int:p>/<string:name>')
def detail(p, name):
    datas = loadInfo(p)
    for i in datas:
        if i['name'] == name:
            info = i
            break

    return render_template('medical/detail.html', info=info)

