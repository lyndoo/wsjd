from flask import render_template,request,session
from . import admin
from config import Config
from dal.reportdal import Report
from dal.attach_dal import Attach
import math
from app.jsonResult import JsonResult


@admin.route('/')
def index():
    if session_check():
        return render_template('admin/index.html')
    else:
        return '<h2>请先登录!<a href="/admin/login">登陆</a></h2>'


@admin.route('/logout')
def logout():
    '''退出'''
    session.pop('account')
    return render_template('admin/login.html')


@admin.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        account = request.form['username']
        pwd = request.form['password']
        print(account,pwd)
        if check_account(account,pwd):
            session['account'] = account
            return render_template('admin/index.html')
        else:
            return render_template('admin/login.html',msg='账号密码错误!')




@admin.route('/lreport_<int:index>')
def lreport(index):
    '''举报投诉列表页'''
    if session_check():
        r = Report()
        if not index:
            index = 0
        count,result = r.list_report(index * Config.PAGE_SIZE,Config.PAGE_SIZE)
        totalPage = int(math.ceil(float(count['count']) / Config.PAGE_SIZE))
        prevPage = 0 if index - 1<=0 else index-1
        nextPage = index + 1 if index+1 < totalPage else totalPage -1
        return render_template('admin/lreport.html',result=result,currentPage=index+1,totalPage=totalPage,prevPage=prevPage,nextPage=nextPage)
    else:
        return '<h2>请先登录!<a href="/admin/login">登陆</a></h2>'

@admin.route('/vreport_<int:ser>')
def vreport(ser):
    '''举报投诉查看页'''
    result = Report().get_report(ser)
    if result:
        attachs = None
        if result['Attach']:
            sers = result['Attach'].split(',')
            attachs = Attach().list_attachs(tuple(map(int,sers)))
        return render_template('admin/vreport.html',result=result,attachs=attachs)
    else:
        return '<h2>未找到此举报信息,<a href="javascript:history.go(-1);">返回</a></h2>'

@admin.route('/rreport_<int:ser>')
def rreport(ser):
    '''确认回复举报投诉'''
    result = Report().reply_report(ser)
    return '确认回复成功!' if result>0 else '确认回复失败'


def check_account(account,pwd):
    """验证账户"""
    return account == 'admin' and pwd == Config.ADMIN_PWD

def session_check():
    return 'account' in session





