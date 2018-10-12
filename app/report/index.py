from flask import render_template,request
from . import report
from main import cache,App
import pymysql.cursors
import os,base64,uuid
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

@report.route('/onlinefrist')
@cache.cached(timeout=86400)
def ofirst():
    return render_template('report/onlineFirst.html')



@report.route('/online',methods=['POST','GET'])
def onlinereport():
    if request.method == 'GET':
        return  render_template('report/online.html')
    else:
        reportInfo = [request.form.get('title'), request.form.get('content'), request.form.get('informer'),
                      request.form.get('informerPhone'), request.form.get('informerAddress')]
        if reportInfo[0] == '' or reportInfo[1] == '' or reportInfo[2] == '' or reportInfo[3] == '':
            return render_template('report/online.html', status=500, msg='标题、内容、举报人和举报人电话不能为空!')

        imgs = saveimg(request.form.getlist('image[]'))
        print(imgs)
        host,user,password,db,charset = Config.MYSQL_CONNECTION
        connection = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset,cursorclass=pymysql.cursors.DictCursor)
        try:
            if imgs:#如果有上传图片
                img_ids = []
                for i in imgs:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO attach(filename) VALUES (%s)"
                        cursor.executemany(sql, (i,))
                    connection.commit()
                    img_ids.append(str(cursor.lastrowid))
                reportInfo.append(','.join(img_ids))
            else:
                reportInfo.append('')


            with connection.cursor() as cursor:
                sql = "INSERT INTO report(title,content,informer,informerPhone,informerAddress,Attach) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, reportInfo)
            connection.commit()
            return  render_template('report/online.html',status=200,msg='举报已提交')
        finally:
            connection.close()
        return  render_template('report/online.html',status=500,msg='举报提交失败')


def saveimg(base64Imgs):
    '''保存图片并返回路径列表'''
    #print(base64Imgs)
    paths = []
    for img in base64Imgs:
        extentions ,b64 = img.split(',')
        extentions = extentions[extentions.index('/')+1:extentions.index(';')]
        filename = str(uuid.uuid1()) + "." + extentions #生成文件名
        filepath = os.path.join(App.config['UPLOAD_FOLDER'], time.strftime("%Y-%m-%d", time.localtime())) #生成路径
        #print(filepath)
        #目录不存在在创建
        if not os.path.exists(filepath):
            os.mkdir(filepath)

        filepath = os.path.join(filepath,filename) #文件整体路径
        #写入硬盘
        file = open(filepath, 'wb')
        file.write(base64.b64decode(b64))
        file.close()
        paths.append((os.path.join(time.strftime("%Y-%m-%d", time.localtime()),filename)))
    return  paths
