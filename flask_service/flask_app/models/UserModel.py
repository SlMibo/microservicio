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
        
    @classmethod
    def add_user(self, user):
        try:
            connection= get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users (id, name, surname, email, password) VALUES (%s, %s, %s, %s, %s)""", (user.id, user.name, user.surname, user.email, user.password))
                affected_rows = cursor.rowcount
                connection.commit()
                

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_user(self, user):
        try:
            connection= get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM users WHERE id = %s""", (user.id, ))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_user(self, user):
        try:
            connection= get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE users SET name = %s, surname = %s, email = %s, password = %s WHERE id = %s""", (user.name, user.surname, user.email, user.password, user.id))
                affected_rows = cursor.rowcount
                connection.commit()
                

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)