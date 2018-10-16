import pymysql,contextlib
from config import Config

host, user, password, db, charset = Config.MYSQL_CONNECTION

@contextlib.contextmanager
def mysql():
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset,
                    cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()
