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
        with open(HHManager.vac_file, encoding='utf-8') as file:
            read = file.read()
            data = json.loads(read)
            print(len(data))

        vac_list = []

        with open("data/obj_vacancies.json", 'w', encoding='utf-8') as file2:

            for vacancy in data:
                vac_list.append(Vacancy.new_vacancy(vacancy).__dict__)
                print(Vacancy.new_vacancy(vacancy).__dict__)

            json.dump(vac_list, file2, sort_keys=False, indent=4, ensure_ascii=False)



    def sort_vacancies(self):
        pass

    def delete_vacancies(self):
        pass
