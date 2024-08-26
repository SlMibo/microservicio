from database.db import get_connection
from .entities.User import User


class UserModel():
    @classmethod
    def get_users(self):
        try:
            connection= get_connection()
            users= []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, surname, email, password FROM users')
                resultset= cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    users.append(user.to_JSON())
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_user(self, id):
        try:
            connection= get_connection()

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, surname, email, password FROM users WHERE id = %s', (id,))
                row= cursor.fetchone()

                user=None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)