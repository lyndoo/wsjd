import pymysql
from config import Config
from dal.base_dal import mysql

class Attach():
    '''附件类'''

    def list_attachs(self,sers):
        with mysql() as cursor:
            sql = 'SELECT filename FROM attach where ser in (%s)' % ','.join(['%s']* len(sers))
            cursor.execute(sql, sers)
            result = cursor.fetchall()
            # 获取查询结果
            return result

if __name__ == '__main__':
    r = Attach()
    # print(r.list_report(0,2))
    print(r.list_attachs((1,2,3)))