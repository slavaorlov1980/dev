from users import Users


class Auth:

    def register_user(self, login: str, password: str) -> bool:
        
        if Users.create_user(login, password):
            return True
        return False

    def check_auth(self, login: str, password: str) -> bool:
        try:
            user = Users(login)

        except ValueError:
            print("Auth Value Error")
            return False
        
        if password == user.password:
            return True
        return False
        
