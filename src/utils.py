from src.hhparser import HHVacancyGetter


def user_interface():

    user_input = input("Введите поисковой запрос: ")
    get_vac = HHVacancyGetter(user_input)
    get_vac.get_vacancies()

    user_input = input("Сколько лучших по зарплате вакансий вывести: ")
    pass

