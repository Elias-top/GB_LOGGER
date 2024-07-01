import logging
import argparse

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age
        logger.info(f"Initialized Person: {self.full_name()}, Age: {self._age}")

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1
        logger.info(f"Happy Birthday {self.full_name()}! Age is now {self._age}")

    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary
        logger.info(f"Initialized Employee: {self.full_name()}, Position: {self.position}, Salary: {self.salary}")

    def raise_salary(self, percent: float):
        if percent < 0:
            logger.error("Raise percent cannot be negative")
            raise ValueError("Percent must be non-negative")
        self.salary *= (1 + percent / 100)
        logger.info(f"Raised salary by {percent}%. New salary: {self.salary}")

    def __str__(self):
        return f'{self.full_name()} ({self.position})'

class TestEmployee:
    def test_employee_full_name(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        assert emp.full_name() == "Ivanov Ivan Ivanovich"
        
    def test_employee_birthday(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        emp.birthday()
        assert emp.get_age() == 31
    
    def test_employee_raise_salary(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        emp.raise_salary(10)
        assert emp.salary == 55000.0
    
    def test_employee_str(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        assert str(emp) == "Ivanov Ivan Ivanovich (Manager)"
    
    def test_employee_last_name_title(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        assert emp.last_name == "Ivanov"

def main(args):
    emp = Employee(args.last_name, args.first_name, args.patronymic, args.age, args.position, args.salary)
    logger.info(str(emp))

    if args.birthday:
        emp.birthday()
        logger.info(f"New age after birthday: {emp.get_age()}")

    if args.raise_salary:
        emp.raise_salary(args.raise_salary)
        logger.info(f"New salary after raise: {emp.salary}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Employee Management System")
    parser.add_argument("last_name", type=str, help="Employee's last name")
    parser.add_argument("first_name", type=str, help="Employee's first name")
    parser.add_argument("patronymic", type=str, help="Employee's patronymic")
    parser.add_argument("age", type=int, help="Employee's age")
    parser.add_argument("position", type=str, help="Employee's position")
    parser.add_argument("salary", type=float, help="Employee's salary")
    parser.add_argument("--birthday", action="store_true", help="Increment age by one year")
    parser.add_argument("--raise_salary", type=float, help="Raise salary by given percent")

    args = parser.parse_args()
    main(args)