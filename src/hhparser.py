from abc import ABC, abstractmethod
import requests
import json


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HHVacancyGetter(Parser):

    def __init__(self, vac_name, current_page=0, max_page=1,
                 site="https://api.hh.ru/vacancies", area=113):

        self.vac_name = vac_name
        self.current_page = current_page
        self.max_page = max_page
        self.site = site
        self.area = area
        self.url = f"{self.site}?text={self.vac_name}&page={self.current_page}&area={self.area}&per_page=100"

    def get_vacancies(self):
        with open("data/vacancies.json", "w") as file:
            for page in range(self.max_page):
                data = (requests.get(f"{self.site}?text={self.vac_name}&page={self.current_page}&area={self.area}&per_page=100")).json()
                json.dump(data, file, sort_keys=True, indent=4)
                print(f"Страница = {self.current_page}")
                self.current_page += 1
                print(self.url)
        return data

