import pymysql.cursors

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='python_user',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


def selectUser(userID, userPsw):
    try:
        cursor = connection.cursor()
        sql = "select * from user where ID = " + userID + " and password= " + userPsw;
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        connection.close()
        return results
    except Exception:
        print("error")
        connection.close()
        return


def insertData():
    return

# if __name__ == '__main__':
#     print(selectUser("123",123))
