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
        with open("vacancies.json", "w") as file:
            json.dump(data, file)
        return data


if __name__ == "__main__":
    get_vac = VacancyGetter('Python')
    a = get_vac.get_vacancies()

    print(a["items"][0])
    print(a["items"][0]['name'])
    print(a["items"][0]['salary'])
    print(a["items"][0]['alternate_url'])
    print(f"{a['items'][0]['schedule']['name']}, {a['items'][0]['employment']['name']}")
    print(a["items"][0]['area']['name'])

