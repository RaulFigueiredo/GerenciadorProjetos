class LoginLogic:
    """
    Class to handle the login logic.
    """

    @staticmethod
    def login(username, password):
        """
        Handle user login logic.

        Args:
        username (str): The username of the user.
        password (str): The password of the user.

        Returns:
        bool: True if login is successful, False otherwise.
        """
        if username == "admin" and password == "admin":
            return True
        print(f"Attempting/ to log in with username: {username} and password: {password}")
        return False


class RegisterLogic:
    """
    Class to handle the registration logic.
    """

    @staticmethod
    def register(username, password, email):
        """
        Handle user registration logic.

        Args:
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email of the user.

        Returns:
        bool: True if registration is successful, False otherwise.
        """
        print(f"Attempting to register with username: {username}, password: {password}, and email: {email}")
        # Add registration logic here
        return True