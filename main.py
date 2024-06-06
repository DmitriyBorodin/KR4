from src.vacmanager import HHManager
from src.vacancy import Vacancy
from src.hhparser import HHVacancyGetter
import json


# if __name__ == "__main__":
#     get_vac = HHVacancyGetter('Python')
#     a = get_vac.get_vacancies()

    # i = 55
    #
    # print(a["items"][i])
    # print(a["items"][i]['name'])
    # print(a["items"][i]['salary'])
    # print(a["items"][i]['alternate_url'])
    # print(f"{a['items'][i]['schedule']['name']}, {a['items'][i]['employment']['name']}")
    # print(a["items"][i]['area']['name'])
    # print(a["pages"])

#
# if __name__ == "__main__":
#     a = HHManager()
#     a.add_vacancies()

    # with open("data/obj_vacancies.json", encoding='utf-8') as file:
    #     data = json.loads("data/obj_vacancies.json")
    #     print(data)

# if __name__ == "__main__":
#     a = HHManager()
#     list_of_vacs = a.get_sorted_vacancies(schedule="Частичная", salary=100000)
#
#     for vac in list_of_vacs:
#         print(vac)
#     print(f"Всего вакансий - {len(list_of_vacs)}")


if __name__ == "__main__":
    a = HHManager()
    a.delete_vacancy_by_id("101312604")
