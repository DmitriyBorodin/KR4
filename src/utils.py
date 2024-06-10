from src.hhparser import HHVacancyGetter
from src.vacmanager import HHManagerJSON
from src.vacancy import Vacancy
import json


def user_interface():

    # Парсим вакансии в json
    user_search = input("Введите поисковой запрос: ")
    get_vac = HHVacancyGetter(user_search)
    get_vac.get_vacancies()

    # Из json'a с вакансиями создаём новый json через инициализацию экземпляров
    # класса Vacancy
    vac_mng = HHManagerJSON()
    vac_mng.add_vacancies()

    with open("data/obj_vacancies.json", encoding='utf-8') as file:
        data = file.read()
        vac_list = json.loads(data)

    while True:

        user_pay_range = input("Введите диапозон зарплаты "
                               "(пример: 50000-200000)\n")

        try:
            user_low_pay, user_max_pay = user_pay_range.split('-')
            user_low_pay = int(user_low_pay)
            user_max_pay = int(user_max_pay)

            if user_low_pay > user_max_pay:
                raise ValueError
        except ValueError:
            print("Введите корректный диапозон запрлаты в формате X-Y")
        else:
            break

    vac_list = delete_vacancies_in_list_by_pay_range(vac_list, user_low_pay, user_max_pay)
    print(f"Кол-во вакансий, подходящих под условия - {len(vac_list)}")

    while True:

        user_number = input("Сколько лучших по зарплате вакансий вывести"
                            "(введите цифру): ")

        try:
            int(user_number)
            if int(user_number) <= 0:
                raise ValueError
        except ValueError:
            print("Введите положительное ненулевое число цифрой, не прописью")
        else:
            break

    sorted_vac_list = sort_list_of_vacancies_by_pay(vac_list)
    vac_obj_list = []
    for vacancy in sorted_vac_list:
        vac_obj_list.append(Vacancy(**vacancy))

    for num in range(int(user_number)):
        print(f"Вакансия #{num+1}")
        print(vac_obj_list[num].__str__())


def sort_list_of_vacancies_by_pay(vac_list):
    new_list = sorted(vac_list, key=lambda x: x["salary"], reverse=True)
    return new_list


def delete_vacancies_in_list_by_pay_range(vac_list, pay_low, pay_high):
    new_list = [vac for vac in vac_list if pay_low < vac['salary'] < pay_high]
    return new_list
