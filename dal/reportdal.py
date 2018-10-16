import pymysql,time
from config import Config
from dal.base_dal import mysql

class Report:
    '''举报投诉管理类'''

    def add_report(self,imgs,reportInfo):
        try:
            if imgs:  # 如果有上传图片
                img_ids = []
                for i in imgs:
                    with mysql() as cursor:
                        sql = "INSERT INTO attach(filename) VALUES (%s)"
                        cursor.executemany(sql, (i,))
                    img_ids.append(str(cursor.lastrowid))
                reportInfo.append(','.join(img_ids))
            else:
                reportInfo.append('')

            with mysql() as cursor:
                sql = "INSERT INTO report(title,content,informer,informerPhone,informerAddress,Attach) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, reportInfo)
            return 200, '举报已提交'
        except Exception as ex:
            return 500,'举报提交失败'


    def list_report(self,index,rows):
        with mysql() as cursor:
            sql = 'SELECT * FROM report order by ser desc limit %s,%s'
            cursor.execute(sql, (index,rows))
            result = cursor.fetchall()
            sql = 'SELECT count(1) as count FROM report'
            cursor.execute(sql)
            count = cursor.fetchone()
            # 获取查询结果
            return count,result

    def reply_report(self,ser):
        with mysql() as cursor:
            sql = 'update report set IsReply = True,ReplyTime = %s where ser = %s'
            curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return cursor.execute(sql, (curtime,ser))


    def get_report(self,ser):
        with mysql() as cursor:
            sql = 'SELECT * FROM report where ser = %s'
            cursor.execute(sql,(ser,))
            result = cursor.fetchone()
            # 获取查询结果
            return result

if __name__ == '__main__':
    r = Report()
    # print(r.list_report(0,2))
    print(r.get_report(2))
    print(r.reply_report(2))
    print(r.get_report(2))