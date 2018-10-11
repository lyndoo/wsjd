from flask import render_template,request
from . import out
import urllib

hrefs = ['http://www.hnwsjsw.gov.cn/4g/c.aspx?id=567',
        'http://wsjs.zhengzhou.gov.cn/tzgg/index.jhtml',
        'http://jdsp.kfwsjsw.gov.cn/tzgg/',
        'http://www.lyws.gov.cn/sort/sort_3.shtml',
        'http://pdswsjsw.gov.cn/',
        'https://www.aywsjd.cn/News.asp?BigClassName=%C9%F3%C5%FA%B9%AB%CA%BE',
        'http://www.hebi.gov.cn/wsjsw/1102792/1250263/index.html',
        'http://www.xxswjw.gov.cn/page193',
        'http://www.jzswsjd.com/tz/',
        'http://www.pyswjw.gov.cn/list.asp?classid=6',
        'http://www.xcsjsw.gov.cn/tzgg/secondpage.html',
        'http://www.lhwsjdw.com/articlecenter-86.aspx',
        'http://www.smxwsjd.com/list.asp?id=148',
        'http://www.nywsjd.cn/index.php?m=content&c=index&a=lists&catid=43',
        'http://www.sqwsjd.cn/plus/list.php?tid=8',
        'http://www.hnxywjw.gov.cn/a/xzcf/',
        'http://www.zkwsjd.com/NewsList.aspx?ParentId=13',
        'http://www.zmdwsj.gov.cn/pub/info/',
        'http://wjw.jiyuan.gov.cn/xxgk/',
        'http://zgcx.nhfpc.gov.cn/DoctorSearch_Mb.aspx',
        'http://zgcx.nhfpc.gov.cn/NurseSearch_Mb.aspx',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=1&sn=b83e965d0726506208a6fcc2e2122eee&chksm=7b393a524c4eb344c15fbd759a14ce9ce1e415426515548b08ad1e0e4f170d0fb0c9231b94fa#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=2&sn=0db3be152960b6f749e9143850b938ff&chksm=7b393a524c4eb3441e7a7ad44d7b8175d54f64d3a5bb235c37b6c87407d2357067461c974dd2#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=3&sn=14964d41e1e3d37590b056b50aa5c1a0&chksm=7b393a524c4eb3449df9f47490a92532de008fd9e05ec530af9f4ea2b27e8c12c8d48595a121#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=4&sn=8e244b1b96c9fae98962ba2a3d9aef7b&chksm=7b393a524c4eb34439908145c3c5d83100c82055b86f84d4430c87d4071a89dab9e5022b43f1#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=5&sn=453fd43c8b577a38591812e50747017c&chksm=7b393a524c4eb3446a1d84a226a6819b2f987a54167057751d02845561126ba11ecac2c52e00#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=6&sn=7c96cf58db9cd59dc66fbc7647d44942&chksm=7b393a524c4eb344b9196607ac7f029f12be6a05a4ddb227ca9c4f48c882c3ac4d866da19003#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=7&sn=0222687ca9353c353e5966cfaa829330&chksm=7b393a524c4eb344728fda5ae08ee96884fd472ecd840c040114d5f9e4265b01fe8ee95266be#rd',
'http://mp.weixin.qq.com/s?__biz=MzU0MDQ4Nzk5Mw==&mid=100000260&idx=8&sn=3a0285d2ca63becae1f0878afb707aea&chksm=7b393a524c4eb3444f3134e4116a7a942ac2c23d3b9d3334432305ee7fff37b08e275de8d5a7#rd',
         'http://www.nhfpc.gov.cn/zwgk/index.shtml',
         'http://www.nhfpc.gov.cn/zhjcj/pqt/new_list.shtml',
         'http://202.102.72.86:8100/index.html'
         ]



@out.route('/<int:ulrindex>')
def index(ulrindex):
    return render_template('out/index.html', urlpath=hrefs[ulrindex])


@out.route('/out/<int:ulrindex>')
def out(ulrindex):
    return render_template('out/out.html', urlpath=hrefs[ulrindex])