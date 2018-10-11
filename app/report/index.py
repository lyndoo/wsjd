from flask import render_template
from . import report
from main import cache
import os
from config import Config
import xlrd
import time

@report.route('/')
@cache.cached(timeout=86400)
def index():
    excelFile = os.path.join(Config.APP_STATIC_DATA, '一键举报.xlsx')#文件地址
    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 获取最后修改时间
    workbook = xlrd.open_workbook(excelFile)
    sheet2 = workbook.sheet_by_index(0)
    names = []
    for i in range(1, sheet2.nrows):
        names.append(sheet2.row_values(i))
    return render_template('report/index.html', names=names, ctime=mtime)

