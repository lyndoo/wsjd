import os


class Config():
    CACHE_TYPE = 'simple'
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
    APP_STATIC_DATA = os.path.join(APP_ROOT, 'static' + os.sep + 'data')  # 数据文件夹位置
    MYSQL_CONNECTION = ('localhost','root','123456','wsjd','utf8mb4')
    UPLOAD_FOLDER = os.path.abspath('.')+ os.path.sep+ 'static'+os.path.sep+'Uploads'  # 文件下载路径
    ADMIN_PWD = 'wsjdadmin123$'
    PAGE_SIZE = 20
    #UPLOAD_FOLDER = 'static' + os.path.sep + 'Uploads'  # 文件下载路径