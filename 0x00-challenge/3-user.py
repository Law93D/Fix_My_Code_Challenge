#!/usr/bin/python3
import bcrypt

class User:
    """User class"""

    def __init__(self, password):
        self.__password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def is_valid_password(self, pwd):
        return bcrypt.checkpw(pwd.encode('utf-8'), self.__password)

if __name__ == "__main__":
    user = User("password")
    print(user.is_valid_password("password"))
