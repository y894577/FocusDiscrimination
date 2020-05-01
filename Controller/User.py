from DataBase import UserDao


def login(userID, userPsw):
    conn = UserDao
    result = conn.selectUser(userID, userPsw)
    if result is not None:
        return result
    return


# if __name__ == '__main__':
#     print(login("123", "123"))
