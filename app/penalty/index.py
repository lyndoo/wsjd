from flask import render_template;
from . import penalty
from main import cache
import os
from config import Config
import xlrd
import time

EXCEL_FILE = os.path.join(Config.APP_STATIC_DATA, '行政处罚.xls')  # 文件地址


@cache.memoize(86400)
def loadExcel(p):
    workbook = xlrd.open_workbook(EXCEL_FILE)
    sheet2 = workbook.sheet_by_index(p)
    lists = []
    for i in range(2, sheet2.nrows):
        lists.append(sheet2.row_values(i))
    return lists


@penalty.route('/')
def index():
    return render_template('penalty/index.html')


@penalty.route('/list_<int:p>')
def penaltyList(p):
    myTitle = '法人' if p == 0 else '自然人'
    lasttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(EXCEL_FILE)))#获取最后修改时间
    return render_template('penalty/list.html', p=p, lists=loadExcel(p), myTitle=myTitle, lasttime=lasttime)


@penalty.route('/<int:p>/detail/<int:id>')
def detail(p,id):
    datas = loadExcel(p)
    for i in datas:
        if i[0] == id:
            info = i
            break

    return render_template('penalty/detail.html', info=info)

