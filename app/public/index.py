from flask import render_template
from . import public
from config import Config
from flask import request
import os
import xlrd
from main import cache
from app.jsonResult import JsonResult
import json


PAGE_INDEX = 30

def getTitleAndFileName(p):
    if p == 1:
        EXCEL_NAME = '1、理发店.xls'
        titleName = '理发店'
    elif p == 2:
        EXCEL_NAME = '2、宾馆.xls'
        titleName = '宾馆'
    elif p == 3:
        EXCEL_NAME = '3、公共浴室.xls'
        titleName = '公共浴室'
    elif p == 7:
        EXCEL_NAME = '7、旅店.xls'
        titleName = '旅店'
    elif p == 8:
        EXCEL_NAME = '8、美容店.xls'
        titleName = '美容院'
    elif p == 9:
        EXCEL_NAME = '9、商场（店）.xls'
        titleName = '商场（店）'
    elif p == 13:
        EXCEL_NAME = '13、音乐厅.xls'
        titleName = '音乐厅'
    elif p == 14:
        EXCEL_NAME = '14、影剧院.xls'
        titleName = '影剧院'
    elif p == 15:
        EXCEL_NAME = '15、游艺厅（室）.xls'
        titleName = '游艺厅（室）'
    elif p == 17:
        EXCEL_NAME = '17、招待所.xls'
        titleName = '招待所'
    else:
        EXCEL_NAME = '18、游泳场（馆）.xls'
        titleName = '游泳场（馆）'
    return EXCEL_NAME, titleName,


@cache.memoize(86400)
def loadInfo(p, name=None):
    titleAndFile = getTitleAndFileName(p)
    EXCEL_FILE = os.path.join(Config.APP_STATIC_DATA + os.sep + '公共卫生', titleAndFile[0])  # 文件地址
    workbook = xlrd.open_workbook(EXCEL_FILE)

    listName = ['name', 'address', 'no', 'lasttime', 'register', 'level', 'remark']
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


@public.route('/')
def index():
    return render_template('public/index.html')


@public.route('/list/<int:p>', methods=['POST'])
def list(p):
    name = request.form.get('name')
    pageNo = int(request.form.get('pageNo'))
    #print(pageNo)
    datas = loadInfo(p, name)
    code = 0 if len(datas) <= (pageNo-1) * PAGE_INDEX + PAGE_INDEX else 1
    datas = datas[(pageNo-1) * PAGE_INDEX:(pageNo-1) * PAGE_INDEX + PAGE_INDEX]
    m = JsonResult(code, datas)
    return json.dumps(m, default=lambda obj: obj.__dict__, ensure_ascii=False)


@public.route('/list/<int:p>', methods=['Get'])
def listPage(p):
    tf = getTitleAndFileName(p)
    return render_template('public/list.html', p=p, titleName=tf[1])


@public.route('/<int:p>/<string:name>')
def detail(p, name):
    for i in loadInfo(p):
        if i['name'] == name:
            info = i
            break
    return render_template('public/detail.html', info=info)

