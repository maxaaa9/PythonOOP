class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        valid_password = False
        if len(value) >= 8:
            is_upper = False
            digit_in = False
            for char in value:
                if char.isupper():
                    is_upper = True
                elif char.isdigit():
                    digit_in = True

            if is_upper and digit_in:
                valid_password = True

        if not valid_password:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__password)}'



profile_with_invalid_password = Profile('My_username', 'My-password1')
print(profile_with_invalid_password)


