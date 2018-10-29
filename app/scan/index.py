from flask import render_template,request
from . import scan
import requests
from app import Sign
from main import cache

#AppId = 'wx9c05576f1b274ddf'
#app_Secret = '333a34b141992e89619587114a1aa34a'

#testappid
AppId = 'wx0740bc697491a6fd'
app_Secret = '566721fef2289a59020795c5deb8bce6'

@scan.route('/')
def index():
    AppInfo = getWxData(request.base_url)
    AppInfo['appID'] = AppId
    AppInfo['appSecret'] = app_Secret
    print(AppInfo)
    return render_template('scan/index.html',AppInfo=AppInfo)


def getWxData(url):
    access_token = create_AccessToken() # 获取access_token
    jsp_api_tikcet = create_JsApiTicket(access_token) # 获取ticket
    sign = Sign.Sign(jsp_api_tikcet,url)
    return sign.sign()

@cache.memoize(timeout=7200)
def create_AccessToken():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+AppId+"&secret="+ app_Secret  # 这里是需要获取的网页
    res = requests.get(url)  # 使用urllib模块获取网页内容
    content = res.json()
    return content['access_token']


@cache.memoize(timeout=7200)
def create_JsApiTicket(accesstoken):
    url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token='+accesstoken+'&type=jsapi'  # 这里是需要获取的网页
    res = requests.get(url)  # 使用urllib模块获取网页内容
    content = res.json()
    return content['ticket']


