from src.vacmanager import HHManager
from src.vacancy import Vacancy
from src.hhparser import HHVacancyGetter


# if __name__ == "__main__":
#     get_vac = HHVacancyGetter('Python')
#     a = get_vac.get_vacancies()

#     # i = 55
#     #
#     # print(a["items"][i])
#     # print(a["items"][i]['name'])
#     # print(a["items"][i]['salary'])
#     # print(a["items"][i]['alternate_url'])
#     # print(f"{a['items'][i]['schedule']['name']}, {a['items'][i]['employment']['name']}")
#     # print(a["items"][i]['area']['name'])
#     # print(a["pages"])
#

if __name__ == "__main__":
    a = HHManager
    a.add_vacancies(a)
