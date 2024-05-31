from abc import ABC, abstractmethod
import requests
import json


class HHParser(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class VacancyGetter(HHParser):

    site = "https://api.hh.ru/vacancies"

    def __init__(self, vac_name):
        self.vac_name = vac_name
        if vac_name:
            VacancyGetter.site += f"?text={vac_name}"

    def get_vacancies(self):
        data = (requests.get(VacancyGetter.site)).json()
        with open("data.json", "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    get_vac = VacancyGetter('Python')
    get_vac.get_vacancies()
