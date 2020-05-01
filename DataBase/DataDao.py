import pymysql.cursors
import datetime

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='python_user',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


def insertData(userID, data):
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor = connection.cursor()
        sql = "insert into data(ID,data,time) values('" + userID + "','" + data + "','" + currentTime + "')"
        result = cursor.execute(sql)
        connection.commit()
        connection.close()
        return result
    except Exception:
        print("error")
        connection.close()
        return
    return

def selectData(userID):
    try:
        cursor = connection.cursor()
        sql = "select * from data where ID = " + userID
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        connection.close()
        return results
    except Exception:
        print("error")
        connection.close()
        return

