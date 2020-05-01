from DataBase import DataDao

conn = DataDao


def addNewData(userID, data):
    result = conn.insertData(userID, data)
    if result is not None:
        return result
    return


def showAllData(userID):
    result = conn.selectData(userID)
    if result is not None:
        return result
    return


if __name__ == '__main__':
    print(showAllData("123"))
