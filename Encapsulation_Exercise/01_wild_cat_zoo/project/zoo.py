from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__animal_capacity and self.__budget < price:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salary = sum([s.salary for s in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_cost = sum([a.money_for_care for a in self.animals])
        if self.__budget >= animals_cost:
            self.__budget -= animals_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        output_str = f"You have {len(self.animals)} animals\n"

        output_str += f"----- {len(lions)} Lions:"
        for lion in lions:
            output_str += f"\n{lion}"

        output_str += f"\n----- {len(tigers)} Tigers:"
        for tiger in tigers:
            output_str += f"\n{tiger}"

        output_str += f"\n----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            output_str += f"\n{cheetah}"

        return output_str

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        output_str = f"You have {len(self.workers)} workers\n"

        output_str += f"----- {len(keepers)} Keepers:"
        for keeper in keepers:
            output_str += f"\n{keeper}"

        output_str += f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            output_str += f"\n{caretaker}"

        output_str += f"\n----- {len(vets)} Vets:"
        for vet in vets:
            output_str += f"\n{vet}"

        return output_str

