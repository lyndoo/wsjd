import os

class Config():
    CACHE_TYPE = 'simple'
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
    APP_STATIC_DATA = os.path.join(APP_ROOT, 'static' + os.sep + 'data')  # 数据文件夹位置