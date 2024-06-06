from src.vacmanager import HHManagerJSON
from src.vacancy import Vacancy
from src.hhparser import HHVacancyGetter
import json
import requests

# if __name__ == "__main__":
#     get_vac = HHVacancyGetter('Python')
#     a = get_vac.get_vacancies()
#
#     i = 55
#
#     print(a["items"][i])
#     print(a["items"][i]['name'])
#     print(a["items"][i]['salary'])
#     print(a["items"][i]['alternate_url'])
#     print(f"{a['items'][i]['schedule']['name']}, {a['items'][i]['employment']['name']}")
#     print(a["items"][i]['area']['name'])
#     print(a["pages"])

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


# if __name__ == "__main__":
#     a = HHManagerJSON()
#     a.delete_vacancy_by_id("101367675")

# if __name__ == "__main__":
#     get_vac = HHVacancyGetter('Python')
#     a = get_vac.get_vacancies()
#     print(a[0])
#
#     b = HHManagerJSON()
#     b.add_vacancies()

# if __name__ == "__main__":
    # with open("data/vacancies.json", "r", encoding='utf-8') as file:
    #     data = json.load(file)
    #     print(data[0])
    #
    #     url = data[0]["url"]
    #     print(url)
    #
    #     desc_pls = requests.get(url).json()
    #     print(desc_pls["description"])
    #
    #     final = (requests.get(url).json())["description"]
    #     print(final)

        # mega_final = ''.join([x for x in final if x.isalnum()])
        # print(mega_final)
        #
        # super_mega_final = re.sub(CLEANR, '', mega_final)
        # print(super_mega_final)
        #не работает бл