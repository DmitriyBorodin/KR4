from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy


class VacManager(ABC):

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def get_sorted_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy_by_id(self, vacancy_id):
        pass


class HHManagerJSON(VacManager):

    vac_file = "data/vacancies.json"

    def __init__(self, vacancies=None):
        self.vacancies = vacancies if vacancies else []

    def add_vacancies(self):
        with open(HHManagerJSON.vac_file, encoding='utf-8') as file:
            read = file.read()
            data = json.loads(read)

        vac_list = []

        with open("data/obj_vacancies.json", 'w', encoding='utf-8') as file2:

            vac_counter = 0
            for vacancy in data:
                vac_list.append(Vacancy.new_vacancy(vacancy).__dict__)
                vac_counter += 1
                # print(f"Вакансия #{vac_counter} добавлена")

            json.dump(vac_list, file2, sort_keys=False, indent=4, ensure_ascii=False)

    def get_sorted_vacancies(self, salary=None, schedule=None):

        result = []

        if not salary and not schedule:
            return "Критерии поиска вакансий не заданы"

        with open("data/obj_vacancies.json", encoding='utf-8') as file:
            data = json.load(file)

            if salary and not schedule:
                for vacancy in data:
                    if vacancy['salary'] >= salary:
                        result.append(vacancy)
                        print(vacancy)

            elif schedule and not salary:
                for vacancy in data:
                    if schedule.lower() in vacancy["schedule"].lower():
                        result.append(vacancy)

            else:
                for vacancy in data:
                    if vacancy['salary'] >= salary and schedule.lower() in vacancy["schedule"].lower():
                        result.append(vacancy)

        return result if result else "Нет вакансий с заданными критериями"

    def delete_vacancy_by_id(self, vacancy_id):

        with open("data/obj_vacancies.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            new_data = [vacancy for vacancy in data if str(vacancy_id) != vacancy["vac_id"]]

        with open("data/obj_vacancies.json", "w", encoding='utf-8') as file:
            json.dump(new_data, file, sort_keys=False, indent=4, ensure_ascii=False)
