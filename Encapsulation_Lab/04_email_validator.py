class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail: str) -> bool:
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain: str) -> bool:
        if domain in self.domains:
            return True
        return False

    def validate(self, email: str):
        username, mail = email.split("@")
        mail, domain = mail.split(".")

        if self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(username):
            return True
        return False