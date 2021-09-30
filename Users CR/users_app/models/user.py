from users_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, firstN, lastN, diremail, createdDate = "SYSDATE()"):

        self.first_name =  firstN
        self.last_name = lastN
        self.email = diremail
        self.created_at = createdDate

    @classmethod
    def get_users_info(cls):
        query = "SELECT first_name, last_name, email, created_at FROM users;"
        results = connectToMySQL("users_schema").query_db( query )
        print(results)

        users = []
        for user in results:
            users.append( User(user['first_name'],user['last_name'],user['email'],user['created_at']) )

        return users

    @classmethod
    def addUser(cls,newUser):
        query = "INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, SYSDATE(),SYSDATE())"
        data = {
            "first_name" : newUser.first_name,
            "last_name" : newUser.last_name,
            "email" : newUser.email
        }
        result = connectToMySQL("users_schema").query_db( query, data )
        
        return result







