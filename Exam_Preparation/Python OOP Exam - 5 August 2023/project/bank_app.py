from typing import List

from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_LOAN_TYPES = ["StudentLoan",
                        "MortgageLoan"]

    VALID_CLIENT_TYPES = ["Student",
                          "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = None

        if loan_type == "StudentLoan":
            new_loan = StudentLoan()

        elif loan_type == "MortgageLoan":
            new_loan = MortgageLoan()

        if loan_type:
            self.loans.append(new_loan)
            return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if not self.capacity:
            return "Not enough bank capacity."

        new_client = None

        if client_type == "Student":
            new_client = Student(client_name, client_id, income)

        elif client_type == "Adult":
            new_client = Adult(client_name, client_id, income)

        if new_client:
            self.capacity -= 1
            self.clients.append(new_client)
            return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))

        if client.__class__.__name__ == "Student" and loan_type == "StudentLoan":
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        elif client.__class__.__name__ == "Adult" and loan_type == "MortgageLoan":
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type and loan_type in self.VALID_LOAN_TYPES:
                loan.increase_interest_rate()
                changed_loans += 1

        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                affected_clients += 1

        return f"Number of clients affected: {affected_clients}."

    def get_statistics(self):

        active_clients = len(self.clients)
        total_income = f"{sum([x.income for x in self.clients]):.2f}"
        granted_loans_to_client = sum(len(l.loans) for l in self.clients if l.loans)
        total_sum_loans = sum(loan.amount for client in self.clients for loan in client.loans)
        not_granted_loans = len(self.loans)
        total_sum_of_non_granted_loans = sum(x.amount for x in self.loans)
        divisor = len(self.clients) if self.clients else 0
        average_interest_rate = sum([x.interest for x in self.clients]) / divisor if self.clients else 0

        my_output = (f"Active Clients: {active_clients}"
                     f"\nTotal Income: {total_income}"
                     f"\nGranted Loans: {granted_loans_to_client}, Total Sum: {total_sum_loans:.2f}"
                     f"\nAvailable Loans: {not_granted_loans}, Total Sum: {total_sum_of_non_granted_loans:.2f}"
                     f"\nAverage Client Interest Rate: {average_interest_rate:.2f}")

        return my_output




