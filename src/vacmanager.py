from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy

class VacManager(ABC):

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def sort_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class HHManager(VacManager):

    vac_file = "data/vacancies.json"

    def __init__(self, vacancies=None):
        self.vacancies = vacancies if vacancies else []

    def add_vacancies(self):
        with open(HHManager.vac_file) as file:

            read = file.read()
            data = json.loads(read)
            print(data[0])
